<script>
    import Navbarindex from "$lib/Navbarindex.svelte";
    import { onMount } from "svelte";
  

    let todos = {};
    let loading = true;
    let error = null;
    let v_usuario = "";
    let v_password = "";
    let v_nombre = "";
    let v_apellido = "";
    let v_documento = "";
    let v_telefono = "";
    let v_rol = 2;
    let v_estado = 1;
    let passwordInsegura = false;
    let v_genero=""
    let v_edad="";
    let r_pass="";
    let v_same_password=false;


    onMount(async () => {
        try {
            let cookies = document.cookie
        .split("; ")
        .find(row => row.startsWith("sesionGoogle="));

    if (cookies) {
        let sesionGoogleRaw = cookies.split("=")[1];
        let sesionGoogle = JSON.parse(decodeURIComponent(sesionGoogleRaw));
        console.log("Sesión decodificada:", sesionGoogle);
        let miStorage = window.localStorage;
        let name = sesionGoogle.nombre;
        let apellido= sesionGoogle.apellido;
        let id = sesionGoogle.id;
        let correo = sesionGoogle.email;
        let encontrado = { name, id, correo};
        miStorage.setItem("usuario", JSON.stringify(encontrado));

        document.getElementById('v_nombre').value=name
        document.getElementById('v_apellido').value=apellido
        document.getElementById('v_usuario').value=correo


    } 
        } catch (e) {
            error = e.message;
        } finally {
            loading = false;
        }
    });

    const serviceID = 'service_acpug5r'
    const templateID = 'template_0hvvaww'
    const apikey = '3bmpPn1S0SLhgotWj'

    function sendEmail() {
        emailjs.init(apikey); 
        emailjs.send(serviceID, templateID, {
            nombre: v_nombre,
            email: v_usuario, 
        })
        .then(result => {
            alert('Correo enviado con éxito!');
        })
        .catch(error => {
            console.log('Error al enviar el correo:', error.text);
        });
    }

    async function Register(event) {
        try {
            event.preventDefault(); // Evita que el formulario se envíe automáticamente
        
            let miStorage = window.localStorage;
            let usuario = JSON.parse(miStorage.getItem("usuario"));
           let  v_id = usuario.id;
      

           
            let v_usuario = document.getElementById('v_usuario').value;
            let v_nombre =      document.getElementById('v_nombre').value;
            let v_apellido =   document.getElementById('v_apellido').value;
            if (v_password==r_pass){
                    v_same_password=false
            }else{
                v_same_password=true
                passwordInsegura=false
                return;
            }

            await checkPasswordSecurity(); // Verificar seguridad de la contraseña
             
        
            if (passwordInsegura) {
                alert("⚠️ El nivel de seguridad de la contraseña es debil, no olvides incluir mayuscula y caracter especiales");
                return;
            }else{
                passwordInsegura=false

            }

        
                const response = await fetch("http://127.0.0.1:8000/actualizaruser", {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        id:  v_id,
                        usuario: v_usuario,
                        password: v_password,
                        nombre: v_nombre,
                        apellido: v_apellido,
                        documento: v_documento,
                        telefono: v_telefono,
                        id_rol: v_rol,
                        estado: v_estado,
                        edad: v_edad,
                        genero: v_genero,
                    }),
                });

                const data = await response.json();
                console.log(data);
            

                if (data) {
                    Swal.fire({
                        title: "Registrado!",
                        text: "Usuario ha sido registrado",
                        icon: "success",
                    });
                    setTimeout(() => {
                    window.location.href = "/usuario";

                    }, 3000);
                
                    //sendEmail()
                } else {
                    alert("Usuario ya registrado");
                }
            } catch (e) {
                error = e.message;
                alert("Error en la solicitud: " + error);
            }
    }



    async function sha1(str) {
        const buffer = new TextEncoder().encode(str);
        const hashBuffer = await crypto.subtle.digest('SHA-1', buffer);
        const hashArray = Array.from(new Uint8Array(hashBuffer));
        return hashArray.map(b => b.toString(16).padStart(2, '0')).join('').toUpperCase();
    }


    async function checkPasswordSecurity() {
        if (!v_password) return;
        
        const hash = await sha1(v_password);
        const prefix = hash.substring(0, 5);
        const suffix = hash.substring(5).toUpperCase();

        try {
            const response = await fetch(`https://api.pwnedpasswords.com/range/${prefix}`);
            const data = await response.text();
            
            passwordInsegura = data.split("\n").some(line => line.split(":")[0] === suffix);
        } catch (error) {
            console.error("Error verificando la contraseña:", error);
        }
    }
</script>


<div class="container-fluid vh-100">
    <div class="row h-100">
        <!-- Sección de la imagen -->
        <div class="col-md-6 d-none d-md-block p-0">
            <!--d-md-block significa que a partir del tamaño md (≥768px), el div se vuelve visible y se muestra como un bloque (display: block;).
Junto con d-none, esto hace que el div esté oculto en móviles pero visible en pantallas medianas y grandes.-->
            <img src="/image4.png" alt="Hospital" class="img-fluid w-100 h-100" style="object-fit: cover;">
        </div>

        <!-- Sección del formulario -->
        <div class="col-md-6 d-flex align-items-center justify-content-center">
            <div class="w-75">
                <h2 class="text-center fw-bold mb-4">Completa tu informacion</h2>

                <form name="formulario" id="formulario" class="container" on:submit={Register}>
                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-person"></i></span>
                            <input type="text" class="form-control" id="v_nombre"  required autocomplete="off" bind:value={v_nombre} placeholder="Nombre">
                        </div>
                    </div>

                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-person"></i></span>
                            <input type="text" class="form-control" id="v_apellido"  required autocomplete="off" bind:value={v_apellido} placeholder="Apellido">
                        </div>
                    </div>

                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-card-list"></i></span>
                            <input type="text" class="form-control"  required autocomplete="off" bind:value={v_documento} placeholder="Documento">
                        </div>
                    </div>

                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-telephone"></i></span>
                            <input type="text" class="form-control" required autocomplete="off"  bind:value={v_telefono} placeholder="Teléfono">
                        </div>
                    </div>

                    <div class="mb-3">
                      <div class="input-group">
                        <span class="input-group-text"> <i class="bi bi-gender-neuter"> </i></span>
                        <select class="form-select" bind:value={v_genero} required>
                            <option value="">Seleccione Género</option>
                            <option value="Masculino">Masculino</option>
                            <option value="Femenino">Femenino</option>
                            <option value="Otro">Otro</option>
                        </select>
                    </div>
                    </div>

                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-calendar"></i></span>
                            <input type="number" class="form-control" required autocomplete="off" bind:value={v_edad} placeholder="Edad">
                        </div>
                    </div>

                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-person-circle"></i></span>
                            <input type="text" class="form-control" id="v_usuario" readonly required autocomplete="off" bind:value={v_usuario} placeholder="Usuario">
                        </div>
                    </div>

                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-lock"></i></span>
                            <input type="password" class="form-control" required autocomplete="off" bind:value={v_password} placeholder="Contraseña">
                        </div>
                    </div>


                     <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-lock"></i></span>
                            <input type="password" class="form-control" required autocomplete="off" bind:value={r_pass} placeholder="Repetir la contraseña">
                        </div>
                    </div>

                    {#if passwordInsegura}
                    <p class="text-danger">⚠️ El nivel de seguridad de la contraseña es debil, no olvides incluir mayuscula y caracter especiales</p>
                     {/if}

                     {#if v_same_password}
                    <p class="text-danger">⚠️Las contraseñas no son las mismas  </p>
                     {/if}

                    <div class="mb-3 ">
                        <input type="checkbox" id="terminos" required />
                        <button class="btn btn-link p-0" href="#" data-bs-toggle="modal" data-bs-target="#TerminosCondiciones">
                                Acepto los términos y condiciones</button>
                      
                    </div>

                    <button type="submit" class="btn btn-primary w-100">Registrar</button>
                </form>
            </div>
        </div>
    </div>
</div>


<div class="modal fade" id="TerminosCondiciones" tabindex="-1" aria-labelledby="rModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="mleModalLabel">
                    <b>Términos y Condiciones</b>
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <p>
                    <b>1. Aceptación de los Términos: </b>

                    Al acceder y utilizar hospital, aceptas cumplir con estos
                    términos y condiciones. Si no estás de acuerdo con alguno de
                    los términos, te recomendamos que no utilices nuestros
                    servicios.
                </p>
                <p>
                    <b>2. Uso del Contenido: </b>

                    Todo el contenido proporcionado en nuestra pagina y base de
                    datos, incluyendo pero no limitado a texto, imágenes,
                    videos, gráficos y logotipos, está protegido por derechos de
                    autor y otros derechos de propiedad intelectual. No puedes
                    copiar, reproducir, distribuir o modificar dicho contenido
                    sin nuestro permiso expreso por correo.
                </p>
                <p>
                    <b>3. Privacidad: </b>

                    Nuestra política de privacidad describe cómo recopilamos,
                    usamos y protegemos tu información personal. Al utilizar
                    nuestros servicios, aceptas las sgtes practicas:
                    <br />
                    - Los datos registrados no son vendidos ni utilizados para fines
                    comerciales mas allá de estar en esta pagina.
                    <br />
                    - No tratamos con datos de manera intrinseca, por lo que no registramos
                    datos tales como tarjetas de creditos o numeros de cuentas todos
                    los datos que obtenemos son exlusivamente para funcionar la pagina
                    y base de datos.
                    <br />
                    - Su Privacidad es nuestra prioridad, por lo que garantizamos
                    que nadie mas allá de los mismos administradores del gimnasio
                    y nuestros ingenieros tienen acceso a sus datos personales
                </p>

                <p>
                    <b>4. Responsabilidad: </b>

                    No nos hacemos responsables por cualquier pérdida, daño o
                    lesión resultante del uso en el gimnasio, solamente somos un
                    medio facilitador de este. Utiliza los servicios bajo tu
                    propio riesgo.
                </p>
                <p>
                    <b>5. Enlaces a Terceros: </b>

                    Nuestro sitio web puede contener enlaces a sitios web o
                    recursos de terceros. No tenemos control sobre el contenido
                    o las prácticas de privacidad de estos sitios y no asumimos
                    responsabilidad por ellos.
                </p>
                <p>
                    <b>6. Modificaciones de los Términos: </b>

                    Nos reservamos el derecho de modificar estos términos y
                    condiciones en cualquier momento. Cualquier modificación
                    entrará en vigencia inmediatamente después de su publicación
                    por este mismo medio. Es tu responsabilidad revisar
                    periódicamente estos términos.
                </p>
                <p>
                    <b>7. Ley Aplicable: </b>

                    Estos términos y condiciones se rigen por las leyes de
                    colombia y cualquier disputa que surja estará sujeta a la
                    jurisdicción exclusiva de los tribunales de colombia.
                </p>
            </div>
            <div class="modal-footer">
                <button
                    type="button"
                    class="btn btn-secondary"
                    data-bs-dismiss="modal">Cerrar</button
                >
            </div>
        </div>
    </div>
</div>
