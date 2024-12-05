<script>
    import Footer from "../../lib/Footer.svelte";
    import { onMount } from "svelte";
  

    let todos = {};
    let loading = true;
    let error = null;
    let v_usuario = "";
    let v_password = "";
    let v_nombre = "";
    let v_apellido = ""; //por que mano anda mucha gente aca haciendo bulla entonces no puedo entrar a teams
    let v_documento = "";
    let v_telefono = "";
    let v_rol = 2;
    let v_estado = 1;

    onMount(async () => {
        try {
            const response = await fetch("");
            if (!response.ok) throw new Error("Error al cargar los datos");
            todos = await response.json();
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

    async function Register() {
        try {
            const response = await fetch("http://127.0.0.1:8000/create_user", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    usuario: v_usuario,
                    password: v_password,
                    nombre: v_nombre,
                    apellido: v_apellido,
                    documento: v_documento,
                    telefono: v_telefono,
                    id_rol: v_rol,
                    estado: v_estado,
                }),
            });

            const data = await response.json();
            console.log(data);
            console.log(data.Informacion);

            if (data.Informacion != "Ya_existe") {
                alert("Usuario registrado");
                document.getElementById("nombre").value = "";
                document.getElementById("apellido").value = "";
                document.getElementById("documento").value = "";
                document.getElementById("telefono").value = "";
                document.getElementById("usuario").value = "";
                document.getElementById("password").value = "";
                sendEmail()
            } else {
                alert("Usuario ya registrado");
            }
        } catch (e) {
            error = e.message;
            alert("Error en la solicitud: " + error);
        }
    }
</script>

<div class="container pt-3">
    <div class="text-center fs-1"><b> REGISTRO USUARIO </b></div>
    <div class="mb-5 px-2">
        <a href="/" class="btn btn-outline-info">Volver</a>
    </div>
    <!--<div class="text-end fs-3  text-a-secondary ">
        ¿Ya tienes una cuenta?<a href="/Login" class="text-secondary">Click aqui</a>
    </div>
    
    <border ; rounded-pill; para redondearlo-->

    <form name="formulario" id="formulario" class="container" on:submit={Register}>
        <div class="container py-5 ps-4 px-5 mt-5 border border-info">
            <!-- border-danger -->
            <div class="row mt-5 mx-5">
                <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6">
                    <label for="nombre">Nombre</label>
                    <input
                        type="text"
                        id="nombre"
                        name="name"
                        placeholder="Escriba el nombre completo"
                        autocomplete="off"
                        class="form-control rounded-pill"
                        required
                        bind:value={v_nombre}
                    />
                </div>
                <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6">
                    <!--El autocomplete off, es para que no te salga sugerencia de cosas que ya registraste-->
                    <label for="apellido">Apellido</label>
                    <input
                        type="text"
                        id="apellido"
                        name="lastname"
                        placeholder="Escriba su apellido completo"
                        autocomplete="off"
                        class="form-control rounded-pill"
                        required
                        bind:value={v_apellido}
                    />
                </div>
            </div>

            <div class="row mt-4 mx-5">
                <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6">
                    <label for="documento">Documento</label>
                    <input
                        type="text"
                        id="documento"
                        name="document"
                        placeholder="Escriba el numero de documento"
                        autocomplete="off"
                        class="form-control rounded-pill"
                        required
                        bind:value={v_documento}
                    />
                </div>
                <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6">
                    <label for="telefono">Telefono</label>
                    <input
                        type="text"
                        id="telefono"
                        name="phone"
                        placeholder="Escriba el numero de telefono o celular"
                        autocomplete="off"
                        class="form-control rounded-pill"
                        required
                        bind:value={v_telefono}
                    />
                </div>
            </div>

            <div class="row mt-4 mx-5">
                <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6 py-2">
                    <label for="usuario">Usuario</label>
                    <input
                        type="text"
                        id="usuario"
                        name="user"
                        placeholder="Escriba su usuario"
                        required
                        class="form-control rounded-pill"
                        bind:value={v_usuario}
                    />
                </div>
                <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6 py-2">
                    <label for="password">Contraseña</label>
                    <input
                        type="password"
                        id="password"
                        placeholder="Escriba la contraseña"
                        required
                        class="form-control rounded-pill"
                        bind:value={v_password}
                    />
                </div>
            </div>

            <div class="row mt-4 mx-5">
                <div class="row mt-4 mx-5">
                    <div
                        class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6 py-2"
                    >
                        <input type="checkbox" id="terminos" required />
                        <label
                            ><button class="btn btn-link p-0"
                                href="#"
                                data-bs-toggle="modal"
                                data-bs-target="#TerminosCondiciones"
                            >
                                Acepto los términos y condiciones</button
                            ></label
                        >
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6">
                        <input
                            type="submit"
                            value="Enviar"
                            class="btn text-black btn-info rounded-pill"
                        />
                    </div>
                </div>
            </div>
        </div>

    </form>

    <div><br /></div>
</div>

<div
    class="modal fade"
    id="TerminosCondiciones"
    tabindex="-1"
    aria-labelledby="rModalLabel"
    aria-hidden="true"
>
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="mleModalLabel">
                    <b>Términos y Condiciones</b>
                </h5>
                <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                ></button>
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

<Footer></Footer>
