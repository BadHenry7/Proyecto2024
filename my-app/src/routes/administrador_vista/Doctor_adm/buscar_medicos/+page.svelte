

<script>
    import Navbaradmi from "$lib/Navbaradmin.svelte";
    import { onMount } from "svelte";

    let todos = {};
    let todos2 = {};
    let loading = true;
    let error = null;
    var v_id = 1;
    onMount(async () => {
        try {
            const response = await fetch("http://127.0.0.1:8000/get_medicos");
            const result = await fetch(
                "http://127.0.0.1:8000/get_atributoxusuarios",
            );
            if (response) {
                const data = await response.json();
                const datos = await result.json();
                todos = data.resultado;
                todos2 = datos.resultado;

                console.log("esta es de data:", data);
                console.log("esta es de datos", datos);
                console.log("esta es de todos", todos);
                console.log("esta es de todos2", todos2);

                setTimeout(() => {
                    globalThis.$("#myTable").DataTable({


                        stripeClasses: ["bg-white", "bg-light"], 
            language: {
            url: "//cdn.datatables.net/plug-ins/1.13.4/i18n/es-ES.json",}


                    }); // Para convertrlo en datatable :D
                }, 0);
            } else {
            }
        } catch (e) {
            error = e.menssage;
            console.log(error);
        } finally {
            loading = false;
        }
    });

    async function Ocultar() {
        const v_editar = document.getElementById("nav-listado");
        v_editar.setAttribute("class", "fade");

        let mostrar = document.getElementById("Mostrardoctores");
        mostrar.removeAttribute("class");

        location.reload();
    }

    async function editar(id, nombre) {
        v_id = id;
        const v_editar = document.getElementById("nav-listado");
        v_editar.removeAttribute("class");

        let ocultar = document.getElementById("Mostrardoctores");
        ocultar.setAttribute("class", "fade");

        const cambiar = ocultar.parentElement;

        cambiar.insertBefore(v_editar, ocultar);

        try {
            const response = await fetch("http://127.0.0.1:8000/get_user", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id: v_id,
                }),
            });
            const data = await response.json();
            console.log("data",data);

            if (response) {
                const result = await fetch(
                    "http://127.0.0.1:8000/get_atributoxusuario",
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            id_usuario: v_id,
                        }),
                    },
                );
                console.log("Entro al editar");
          
             

                const datos = await result.json();
                console.log("datos",datos);


                //codigo de node:
                const response = await fetch("https://api-nodejs-buxf.onrender.com/api/especialidades/getespecialidades");
                if (!response.ok) throw new Error("Error al cargar los datos");
                 const data_node = await response.json();
                 let  todos_node=data_node.data
                console.log("esto es data de node", data)

                console.log("esto es node", todos_node)
                console.log(todos_node[1])
                console.log(todos_node.length)

            const Selectespecialidad = document.getElementById("especialidad");
        
                for (let i = 0; i < todos_node.length; i++) {
                    const user = todos_node[i];
                    const option = document.createElement("option");
                    option.value = user.nombre;
                    option.textContent = user.nombre;
                    Selectespecialidad.appendChild(option);
                }



            document.getElementById("especialidad").value = datos.valor;



                document.getElementById("nombres").value = data.nombre;
                document.getElementById("apellidos").value = data.apellido;
                document.getElementById("documento").value = data.documento;
                document.getElementById("telefono").value = data.telefono;
                document.getElementById("correo").value = data.usuario;
              
                const v_estado = data.estado ? "1" : "0";
                document.getElementById("estado").value = v_estado;
            }

            
        } catch (e) {
            error = e.menssage;
            console.log(error);
        }
    }

    async function activar(id, nombre) {
        let v_estado = 1;
        v_id = id;

        try {
            const response = await fetch("http://127.0.0.1:8000/estado_user", {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id: v_id,
                    estado: v_estado,
                }),
            });

            const data = await response.json();

            if (response) {
                const Toast = Swal.mixin({
                    toast: true,
                    position: "bottom-end",
                    showConfirmButton: false,
                    timer: 3000,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.onmouseenter = Swal.stopTimer;
                        toast.onmouseleave = Swal.resumeTimer;
                    },
                });
                Toast.fire({
                    icon: "success",
                    iconColor: "#000000",
                    color: "black",
                    background: "#76fa78",
                    title: "usuario activado con exito",
                });

                setTimeout(() => {
                    location.reload();
                }, 3500);
            }
        } catch (e) {
            error = e.menssage;
            console.log(error);
        }
    }

    async function desactivar(id, nombre, usuario) {
        let v_estado = 0;
        v_id = id;

        try {
            const response = await fetch("http://127.0.0.1:8000/estado_user", {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id: v_id,
                    estado: v_estado,
                }),
            });

            if (response) {
                const Toast = Swal.mixin({
                    toast: true,
                    position: "bottom-end",
                    showConfirmButton: false,
                    timer: 3000,
                    timerProgressBar: true,
                    didOpen: (toast) => {
                        toast.onmouseenter = Swal.stopTimer;
                        toast.onmouseleave = Swal.resumeTimer;
                    },
                });
                Toast.fire({
                    icon: "error",
                    iconColor: "white",
                    color: "white",
                    background: "#ff4e4e",
                    title: "usuario desactivado con exito",
                });
                setTimeout(() => {
                    location.reload();
                }, 3500);
            }
        } catch (e) {
            error = menssage;
            console.log(error);
        }
    }

    async function actualizar() {
        let vnombre = document.getElementById("nombres").value;
        let vapellidos = document.getElementById("apellidos").value;
        let vdocumento = document.getElementById("documento").value;
        let vtelefono = document.getElementById("telefono").value;
        let vespecialidad = document.getElementById("especialidad").value;
    
        let vcorreo = document.getElementById("correo").value;
        let vestado = document.getElementById("estado").value;

        try {
            console.log("Entra al try de actualizar");

            const response = await fetch(
                "http://127.0.0.1:8000/actualizaruser",
                {
                    method: "PUT",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        id: v_id,
                        usuario: vcorreo,
                        nombre: vnombre,
                        apellido: vapellidos,
                        documento: vdocumento,
                        telefono: vtelefono,
                        estado: vestado,
                    }),
                },
            );

            try {
                console.log(v_id)
                console.log("entra al update atributoxusuario")
                console.log(vespecialidad)
                const result = await fetch(
                    "http://127.0.0.1:8000/updateatributoxusuario",
                    {
                        method: "PUT",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            valor: vespecialidad,
                            descripcion: vespecialidad,
                            id_usuario: v_id,
                        }),
                    },
                );
            } catch (e) {
                error = e.menssage;
                console.log(error);
            }

            console.log("Actualizado");

            const Toast = Swal.mixin({
                toast: true,
                position: "top-end",
                showConfirmButton: false,
                timer: 3000,
                timerProgressBar: true,
                didOpen: (toast) => {
                    toast.onmouseenter = Swal.stopTimer;
                    toast.onmouseleave = Swal.resumeTimer;
                },
            });
            Toast.fire({
                icon: "success",
                iconColor: "white",
                color: "white",
                background: "#00bdff",
                title: "usuario actualizado con exito",
            });

            setTimeout(() => {
                const v_editar = document.getElementById("nav-listado");
                v_editar.setAttribute("class", "fade");

                let ocultar = document.getElementById("Mostrardoctores");
                ocultar.removeAttribute("class");

                const cambiar = v_editar.parentElement;
                cambiar.insertBefore(ocultar, v_editar);
                location.reload();
            }, 3000);
        } catch (e) {
            error = e.message;
            console.log(error);
        }
    }
</script>

<Navbaradmi></Navbaradmi>

<div id="Mostrardoctores">
    <div class="container py-4">
        <h2 class="text-center"><b>¡Lista de doctores!</b></h2>
        <hr>
        {#if loading}
            <h2>Cargando datos...</h2>
        {:else if error}
            <p>Error{error}</p>
        {:else}
            <div class="">
                <table
                    class="min-w-full bg-white border border-gray-300"
                    id="myTable">
                    <thead class="bg-primary text-white">
                        <tr>
                            <th class=" py-2 border">Usuario</th>
                            <th class=" py-2 border">Nombre</th>
                            <th class=" py-2 border">Apellido</th>
                            <th class=" py-2 border">Documento</th>
                            <th class=" py-2 border">Telefono</th>
                            <th class=" py-2 border">Especialidad</th>
                            <th class=" py-2 border">Estado</th>
                            <th class=" py-2  border" >Opciones</th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each todos as todo}
                            <tr class="hover:bg-gray-50">
                                <td class=" py-2 border">{todo.usuario}</td>
                                <td class=" py-2 border">{todo.nombre}</td>
                                <td class=" py-2 border">{todo.apellido}</td
                                >
                                <td class=" py-2 border"
                                    >{todo.documento}</td
                                >
                                <td class=" py-2 border">{todo.telefono}</td
                                >
                                {#each todos2 as todo2}
                                    {#if todo2.id_usuario === todo.id}
                                        <td class=" py-2 border"
                                            >{todo2.valor}</td
                                        >
                                    {/if}
                                {/each}
                                <td class=" py-2 mx-5 border">

                                    <span
                                        class={todo.estado
                                            ? "text-green-600"
                                            : "text-red-600"}
                                    >
                                        {todo.estado ? "Activo" : "Desactivado"}
                                    </span>
                                </td>
                                <td class=" py-2 mx-5  border">

                                   
                                    <button aria-label="Para editar"
                                        class="btn btn-info"
                                        on:click={() =>
                                            editar(todo.id, todo.nombre)} 
                                        > <i class="bi bi-pencil-square"></i></button>
                                            
                                    {#if todo.estado}
                                        <!-- Mostrar botón "Desactivar" si el usuario está activo -->
                                        <button aria-label="para desactivar"
                                            class="btn btn-success"
                                            on:click={() =>
                                                desactivar(
                                                    todo.id,
                                                    todo.nombre,
                                                    todo.usuario,
                                                )}
                                        >
                                              <i class="bi bi-toggle-on"></i>
                                        </button>
                                    {:else}
                                        <!-- Mostrar botón "Activar" si el usuario está desactivado -->

                                        <button aria-label="para activar"
                                            class="btn btn-danger"
                                            on:click={() =>
                                                activar(todo.id, todo.nombre)}
                                        >
                                        <i class=" bi bi-toggle-off"></i>
                                        </button>
                                    {/if}
                                  
                                </td>
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>
        {/if}
    </div>
</div>

<!--Hola-->
<div
    class="fade"
    id="nav-listado"
    role="tabpanel"
    aria-labelledby="nav-listado-tab"
>
    <div class="container text-center">
        <p class="text-orange"></p>
    </div>
    <div class="card border-dark shadow" style="width: 60%; margin-left: 20%;">
        <div class="card-header row g-2">
            <h5 class="card-title col-lg-11"><b>Editando Usuario</b></h5>
            <button
                class="btn btn-close col-lg-1"
                aria-label="Cerrar"
                on:click={() => Ocultar()}
            ></button>
        </div>
        <div class="card-body" style="margin-left: 10%;">
            <div class="row">
                <div class="col-lg-2">
                    <p class="card-text"><b>Nombre:</b></p>
                </div>

                <div class="col-lg-10">
                    <input
                        type="text"
                        placeholder="Nombres"
                        id="nombres"
                        maxlength="100"
                        style="border: none; width: 55%;"
                    />
                </div>
            </div>

            <div class="row pt-3">
                <div class="col-lg-2">
                    <p class="card-text"><b>Apellido:</b></p>
                </div>

                <div class="col-lg-10">
                    <input
                        type="text"
                        placeholder="Apellidos"
                        id="apellidos"
                        style="border: none; width: 55%;"
                    />
                </div>
            </div>

            <div class="row pt-3">
                <div class="col-lg-2">
                    <p class="card-text"><b>documento:</b></p>
                </div>
                <div class="col-lg-10">
                    <input
                        type="text"
                        id="documento"
                        placeholder="Documento de identidad"
                        style="border: none; width: 55%;"
                    />
                </div>
            </div>

            <div class="row pt-3">
                <div class="col-lg-2">
                    <p class="card-text"><b>Telefono:</b></p>
                </div>
                <div class="col-lg-10">
                    <input
                        type="text"
                        id="telefono"
                        placeholder="Telefono"
                        maxlength="20"
                        style="border: none; width: 55%;"
                    />
                </div>
            </div>

            <div class="row pt-3">
                <div class="col-lg-2">
                    <p class="card-text"><b>Correo:</b></p>
                </div>
                <div class="col-lg-10">
                    <input
                        type="text"
                        placeholder="Correo electronico"
                        id="correo"
                        style="border: none; width: 55%;"
                    />
                </div>
            </div>

            <div class="row pt-3">
                <div class="col-lg-2">
                    <p class="card-text"><b>Estado:</b></p>
                </div>
                <div class="col-lg-10">
                    <select
                        id="estado"
                        name="opciones"
                        style="border: none; width: 55%;"
                    >
                        <option value="1">Activar</option>
                        <option value="0">Desactivar</option>
                    </select>
                </div>
            </div>

            <div class="row pt-3">
                <div class="col-lg-2">
                    <p class="card-text"><b>Especialidad:</b></p>
                </div>
                <div class="col-lg-10">
                    <select id="especialidad"  name="opciones" style="border: none; width: 55%;">
                        <option  selected></option>
     
                    </select>
                </div>
            </div>

            <div class="row" style="margin-top: 4%;">
                <div class="col-lg-9">
                    ¡Al terminar de editar, darle click en actualizar para
                    guardar los cambios!
                </div>
                <div class="col-lg-3 text-end">
                    <button on:click={actualizar} class="btn btn-outline-info"
                        ><b>Actualizar</b></button
                    >
                </div>
                <div id="estado" class="col-lg-10"></div>
            </div>
        </div>
    </div>
</div>
