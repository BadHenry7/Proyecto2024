<script>
    import Navbaradmi from "$lib/Navbaradmin.svelte";
    import { onMount } from "Svelte";

    let todos = {};
    let loading = true;
    let error = null;

    onMount(async () => {
        try {
            const response = await fetch("http://127.0.0.1:8000/get_medicos");
            if (response) {
                const data = await response.json();
                todos = data.resultado;
                console.log(data);
                console.log(todos);

                setTimeout(() => {
                    globalThis.$("#myTable").DataTable(); // Para convertrlo en datatable :D
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

    function editar() {}

    async function activar(id, nombre) {
        alert(id);
        let v_estado = 1;
        let v_id = id;

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
        let v_id = id;

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
</script>

<Navbaradmi></Navbaradmi>

<div id="Mostrardoctores">
    <div class="container py-4">
        <h2 class="">Lista de doctores</h2>
        {#if loading}
            <h2>Cargando datos...</h2>
        {:else if error}
            <p>Error{error}</p>
        {:else}
            <div class="">
                <table
                    class="min-w-full bg-white border border-gray-300"
                    id="myTable"
                >
                    <thead>
                        <tr>
                            <th class="px-4 py-2 border">Usuario</th>
                            <th class="px-4 py-2 border">Nombre</th>
                            <th class="px-4 py-2 border">Apellido</th>
                            <th class="px-4 py-2 border">Documento</th>
                            <th class="px-4 py-2 border">Telefono</th>
                            <th class="px-4 py-2 border">Estado</th>
                            <th class="px-4 py-2 border">Opcion</th>
                        </tr>
                    </thead>
                    <tbody>
                        {#each todos as todo}
                            <tr class="hover:bg-gray-50">
                                <td class="px-4 py-2 border">{todo.usuario}</td>
                                <td class="px-4 py-2 border">{todo.nombre}</td>
                                <td class="px-4 py-2 border">{todo.apellido}</td
                                >
                                <td class="px-4 py-2 border"
                                    >{todo.documento}</td
                                >
                                <td class="px-4 py-2 border">{todo.telefono}</td
                                >
                                <td class="px-4 py-2 border">
                                    <span
                                        class={todo.estado
                                            ? "text-green-600"
                                            : "text-red-600"}
                                    >
                                        {todo.estado ? "Activo" : "Desactivado"}
                                    </span>
                                </td>
                                <td class="px-4 py-2 border">
                                    <button
                                        class="btn btn-info"
                                        on:click={() =>
                                            editar(todo.id, todo.nombre)}
                                        >Editar</button
                                    >
                                    {#if todo.estado}
                                        <!-- Mostrar botón "Desactivar" si el usuario está activo -->
                                        <button
                                            class="btn btn-danger"
                                            on:click={() =>
                                                desactivar(
                                                    todo.id,
                                                    todo.nombre,
                                                    todo.usuario,
                                                )}
                                        >
                                            Desactivar
                                        </button>
                                    {:else}
                                        <!-- Mostrar botón "Activar" si el usuario está desactivado -->

                                        <button
                                            class="btn btn-success"
                                            on:click={() =>
                                                activar(todo.id, todo.nombre)}
                                        >
                                            Activar
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
<div class="">
    <div class="container">
       <div class="card border-dark shadow"  style="width: 60%; margin-left: 20%;">
        <div class="card-header text-center">
            <b>Editando usuario</b>
        </div>
        
       </div> 
    </div>
</div>
