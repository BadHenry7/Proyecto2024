import { redirect } from '@sveltejs/kit';
import { MICROSOFT_CLIENT_ID, MICROSOFT_CLIENT_SECRET } from '$env/static/private';

var rol_v=0
let estado_v=0
let v_estado=0
let error=null;

async function getMicrosoftUserData(access_token) {
    const response = await fetch("https://graph.microsoft.com/v1.0/me", {
        headers: { Authorization: `Bearer ${access_token}` }
    });
    return response.json();
}

async function verificarUsuarioEnBD(user) {
    console.log("Verificando usuario en BD:", user);
    const res = await fetch("http://localhost:8000/verif_user", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            google_id: user.microsoft_id,
            foto: user.foto,
            access_token: user.access_token,
            estado: 1,
            usuario: user.email,
            nombre: user.given_name,
            apellido: user.family_name,
        })
    });
    return await res.json();
}

export const GET = async ({ url, cookies }) => {
    const redirectURL = 'http://localhost:5173/oauth-microsoft';
    const code = url.searchParams.get('code');

    console.log('Código de autenticación Microsoft:', code);
    console.log(MICROSOFT_CLIENT_ID)
    console.log(MICROSOFT_CLIENT_SECRET)

    try {
        const tokenResponse = await fetch('https://login.microsoftonline.com/common/oauth2/v2.0/token', {
            method: 'POST',
            headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
            body: new URLSearchParams({
                client_id: MICROSOFT_CLIENT_ID,
                client_secret: MICROSOFT_CLIENT_SECRET,
                code,
                redirect_uri: redirectURL,
                grant_type: 'authorization_code',
               scope: 'User.Read'
            })
        });

        const tokens = await tokenResponse.json();
        console.log("Tokens obtenidos:", tokens);

        const user = await getMicrosoftUserData(tokens.access_token);
        console.log('Usuario Microsoft:', user);

        const usuarioBD = await verificarUsuarioEnBD({
            microsoft_id: user.id,
            nombre: user.displayName,
            email: user.mail || user.userPrincipalName,
            foto: "https://graph.microsoft.com/v1.0/me/photo/$value",
            access_token: tokens.access_token,
            given_name: user.givenName,
            family_name: user.surname
        });
     console.log("Respuesta del backend:", usuarioBD);
     let v_id= usuarioBD.id?usuarioBD.id:1;
     rol_v= usuarioBD.rol_v?usuarioBD.rol_v:1;
      v_estado= usuarioBD.estado?usuarioBD.estado:false;


     estado_v = usuarioBD.Informacion;

        cookies.set('sesionGoogle', JSON.stringify({
            google_id: user.id,
            nombre: user.givenName,
            apellido: user.surname,
            email: user.mail,
            foto: "https://graph.microsoft.com/v1.0/me/photo/$value",
            access_token: tokens.access_token,
            estado: usuarioBD.Informacion,
            id: usuarioBD.id || 1,
            rol_v: usuarioBD.rol_v || 1
        }), {
            path: '/',
            httpOnly: false,
            secure: true,
            sameSite: "None",
            maxAge: 60 * 60 * 24 * 7 // 1 semana
        });

      
    } catch (err) {
        console.log('Error en la autenticación de Microsoft:', err);
        throw redirect(303, '/Login');
    }
    finally{
    
          if (error){
    
           throw redirect(303, '/Login');
    
          }
    
          if (estado_v==="Ya_existe" && v_estado!=false){
            if (rol_v==1){
              throw redirect(303, '/administrador_vista');
            }
            else if (rol_v==2){
              throw redirect(303, '/usuario');
            }
            else if (rol_v==3){
              throw redirect(303, '/doctor_adm');
            }
            else {
              throw redirect(303, '/vista_main');
            }
          }else if (estado_v==="Registrada" ){
            console.log("Estado actual:", estado_v, "Rol:", rol_v);
    
            throw redirect(303, '/completar_informacion');
          }else if (estado_v==="Ya_existe" && v_estado==false){
    
            throw redirect(303, '/completar_informacion');
          }
        }
};
