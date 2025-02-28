<script>
    import Navbadmin from "$lib/Navbaradmin.svelte";
    import Footer from "../../../../lib/Footer.svelte";
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
    let v_rol = 3;
    let v_estado = 1;
    let v_genero="";
    let v_edad="";
    let r_pass="";
    let v_same_password=false;
    let passwordInsegura = false;


    onMount(async () => {
        try {
            const response = await fetch("https://api-nodejs-buxf.onrender.com/api/especialidades/getespecialidades");
            if (!response.ok) throw new Error("Error al cargar los datos");
           const data = await response.json();
          let  todos_node=data.data
          console.log("esto es data de node", data)

            console.log("esto es node", todos_node)
            console.log(todos_node[1])
            console.log(todos_node.length)
            

            const Selectespecialidad = document.getElementById("especialista");
            for (let i = 0; i < todos_node.length; i++) {
                const user = todos_node[i];

                const option = document.createElement("option");

                option.value = user.nombre;

                option.textContent = user.nombre;

                Selectespecialidad.appendChild(option);
            }
            

        } catch (e) {
            error = e.message;
            console.log(error)
        } finally {
            loading = false;
        }
    });

    const serviceID = "service_acpug5r";
    const templateID = "template_0hvvaww";
    const apikey = "3bmpPn1S0SLhgotWj";

    function sendEmail() {
        emailjs.init(apikey);
        emailjs
            .send(serviceID, templateID, {
                nombre: v_nombre,
                email: v_usuario,
            })
            .then((result) => {
                alert("Correo enviado con éxito!");
            })
            .catch((error) => {
                console.log("Error al enviar el correo:", error.text);
            });
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

    async function Register() {
        try {

            event.preventDefault(); // Evita que el formulario se envíe automáticamente
        
           
      
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







            console.log("si entra?")
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

            let id_atributo_v=1
            let estado_v=1

            console.log(data);
            todos= data
            console.log(todos);
            
            let v_id=todos[0];
            console.log("----Este es el v_id")

            console.log(v_id)
            let v_especialidad= document.getElementById("especialista").value;
            console.log("Este es el valor que tiene v_especialidad")
            console.log(v_especialidad)
            if (data.Informacion != "Ya_existe") {
                const response = await fetch("http://127.0.0.1:8000/create_atributoxusuario", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    valor: v_especialidad,
                    descripcion: v_especialidad,
                    id_usuario: v_id,
                    id_atributo: id_atributo_v,
                    estado: estado_v
                }),
            });







            Swal.fire({
                    title: "Registrado!",
                    text: "Usuario ha sido registrado",
                    icon: "success",
                });
                setTimeout(() => {
                    location.reload();
                    }, 3000);
                
                //sendEmail()
            } else {
                alert("Usuario ya registrado");
            }
        } catch (e) {
            error = e.message;
            console.log("Error en la solicitud: " + error);
        }
    }
</script>

<Navbadmin></Navbadmin>

<div class="container-fluid vh-100">
    <div class="row h-100">
        <!-- Sección de la imagen -->
        <div class="col-md-6 d-none d-md-block p-0">
            <!--d-md-block significa que a partir del tamaño md (≥768px), el div se vuelve visible y se muestra como un bloque (display: block;).
            Junto con d-none, esto hace que el div esté oculto en móviles pero visible en pantallas medianas y grandes.-->
            <img src="/doctoregister.png" alt="Hospital" class="img-fluid w-100 h-100" style="object-fit: cover;">
        </div>

        <!-- Sección del formulario -->
        <div class="col-md-6 d-flex align-items-center justify-content-center">
            <div class="w-75">
                <h2 class="text-center fw-bold mb-4">Registro de doctor</h2>

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
                            <span class="input-group-text"><i class="bi bi-hospital"></i> </span>
                            <select class="form-select form-control " id="especialista" required>
                                <option selected>Seleccione</option>
                            </select>
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





<!--
<div class="container pt-3">
    <div class="text-center fs-1"><b> 🚑Registro de medico 🚑</b></div>

    //<div class="text-end fs-3  text-a-secondary ">
       // ¿Ya tienes una cuenta?<a href="/Login" class="text-secondary">Click aqui</a>
    //</div>
    
    //<border ; ; para redondearlo

    <form
        name="formulario"
        id="formulario"
        class="container"
        on:submit={Register}
    >
        <div class="container py-5 ps-4 px-5 mt-5 border border-info">
            border-danger
            <div class="row mt-5 mx-5">
                <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6">
                    <label for="nombre">Nombre</label>
                    <input
                        type="text"
                        id="nombre"
                        name="name"
                        placeholder="Escriba el nombre completo"
                        autocomplete="off"
                        class="form-control "
                        required
                        bind:value={v_nombre}
                    />
                </div>
                <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6">
                    El autocomplete off, es para que no te salga sugerencia de cosas que ya registraste
                    <label for="apellido">Apellido</label>
                    <input
                        type="text"
                        id="apellido"
                        name="lastname"
                        placeholder="Escriba su apellido completo"
                        autocomplete="off"
                        class="form-control "
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
                        class="form-control "
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
                        class="form-control "
                        required
                        bind:value={v_telefono}
                    />
                </div>
            </div>

            <div class="row mt-4 mx-5">
                <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6 py-2">
                    <label for="genero">Genero</label>
                    <select id="genero" class="form-select"  bind:value={v_genero}>
                        <option value="" disabled selected>Seleccione un genero</option>
                        <option value="Masculino">Masculino</option>
                        <option value="Femenino">Femenino</option>

                    </select>
                    

                </div>
                <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6 py-2">
                    <label for="edad">Edad</label>
                    <input
                        type="number"
                        id="edad"
                        placeholder="Escriba la edad"
                        required
                        class="form-control"
                        bind:value={v_edad}
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
                        class="form-control "
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
                        class="form-control "
                        bind:value={v_password}
                    />
                </div>
            </div>
            <div class="row mt-4 mx-5">
                <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6">
                    <label for="">Ocupacion</label>
                    <select class="form-select form-control " id="especialista" required>
                        <option selected>Seleccione</option>
                    </select>
                </div>
            </div>
            <div class="row mt-3 mx-5">
                <div class="row mt-4 mx-5">
                    <div
                        class="col-lg-5 col-md-5 col-sm-5 col-12 col-xl-5 py-2"
                    >
                       <input type="checkbox" id="terminos" required />
                        <label
                            ><a
                                href="#"
                                data-bs-toggle="modal"
                                data-bs-target="#TerminosCondiciones"
                            >
                                Acepto los términos y condiciones</a
                            ></label
                        > 
                    </div>
                    <div class="col-lg-6 col-md-6 col-sm-6 col-12 col-xl-6">
                        <input
                            type="submit"
                            value="Enviar"
                            class="btn text-black btn-info "
                        />
                    </div>
                </div>
            </div>
        </div>
    </form>

    <div><br /></div>
</div>
 -->