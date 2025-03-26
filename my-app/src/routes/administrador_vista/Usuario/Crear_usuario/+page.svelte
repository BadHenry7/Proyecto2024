<script>
    import Navbaradmin from "../../../../lib/Navbaradmin.svelte";

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
    let v_edad ="";
    let v_genero ="";
    let r_pass=""
    let v_rol = 2;
    let v_estado = 1;
    let passwordInsegura = false;
    let v_same_password=false;


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
 
    function Confirmacion() {
        Swal.fire({
            title: "¿Estas seguro de registrar este usuario?",
            text: "¡tu no podras revertir esto!",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#3085d6",
            cancelButtonColor: "#d33",
            confirmButtonText: "¡si, registralo!",
        }).then((result) => {
            if (result.isConfirmed) {
               

                Register();
            }
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
                    genero: v_genero,
                    edad: v_edad
                }),
            });

            const data = await response.json();
            console.log(data);
            console.log(data.Informacion);

            if (data.Informacion != "Ya_existe") {
                Swal.fire({
                    title: "Registrado!",
                    text: "Usuario ha sido registrado",
                    icon: "success",
                });
                document.getElementById("nombre").value = "";
                document.getElementById("apellido").value = "";
                document.getElementById("documento").value = "";
                document.getElementById("telefono").value = "";
                document.getElementById("usuario").value = "";
                document.getElementById("password").value = "";
                document.getElementById("genero").value = "";
                document.getElementById("edad").value = "";

            } else {
                Swal.fire({
                    title: "Error",
                    text: "Usuario ya se encuentra registrado",
                    icon: "error",
                });
            }
        } catch (e) {
            error = e.message;
            alert("Error en la solicitud: " + error);
        }
    }
</script>

<Navbaradmin></Navbaradmin>


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
                <h2 class="text-center fw-bold mb-4">Registro de paciente</h2>

                <form name="formulario" id="formulario" class="container" on:submit={Register}>
                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-person"></i></span>
                            <input type="text" class="form-control" required autocomplete="off" bind:value={v_nombre} placeholder="Nombre">
                        </div>
                    </div>

                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-person"></i></span>
                            <input type="text" class="form-control" required autocomplete="off" bind:value={v_apellido} placeholder="Apellido">
                        </div>
                    </div>

                    <div class="mb-3">
                        <div class="input-group">
                            <span class="input-group-text"><i class="bi bi-card-list"></i></span>
                            <input type="text" class="form-control" required autocomplete="off" bind:value={v_documento} placeholder="Documento">
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
                            <input type="text" class="form-control" required autocomplete="off" bind:value={v_usuario} placeholder="Usuario">
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


<!--
            
<div class="row mt-4 mx-5">

                    <input type="submit" value="Enviar " class="btn text-black btn-info "/>

                    <div
                        class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6 py-2"
                    ></div>
                    <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6">
                        <input
                            type="submit"
                            value="Enviar "
                            class="btn text-black btn-info "
                        />
                    </div>
                </div>

-->

      