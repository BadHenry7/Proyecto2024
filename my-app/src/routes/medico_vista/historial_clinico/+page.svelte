<script>
    import Navbarmedico from "$lib/Navbarmedico.svelte";
    import { onMount } from "svelte";

    let loading = true;
    onMount(() => {
        try {


        } catch (e) {
            error = e.message;
            console.log(error);
        } finally {
            
        }
    });

    let todos = {};
    let error = null;

    async function buscar() {
        let buscardocument_v =
            document.getElementById("buscardocument_v").value;
        console.log("documento a buscar: ", buscardocument_v);
        const response = await fetch(
            "http://127.0.0.1:8000/get_user_document",
            {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                },
                body: JSON.stringify({
                    documento: buscardocument_v,
                }),
            },
        );
        loading = false;
        const data = await response.json();
        console.log(data);
        todos = data;
        console.log("Nombre del usuario: ", todos.nombre);
        document.getElementById("nombre").textContent = todos.nombre;
        document.getElementById("documento").textContent = todos.documento;
        document.getElementById("telefono").textContent = todos.telefono;

        let v_id = todos.id;
        console.log("id del usuario", v_id);

        setTimeout(() => {
            globalThis.$("#myTable").DataTable(); // Para convertrlo en datatable :D
        }, 0);
        try {
            const response = await fetch(
                "http://127.0.0.1:8000/historia_clinica",
                {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json",
                    },
                    body: JSON.stringify({
                        id_paciente: v_id,
                    }),
                },
            );
            const data = await response.json();
            console.log("Data de cita");
            console.log(data);
            todos = data.resultado;
            console.log(todos);
        } catch (e) {
            error = e.message;
            console.log(error);
        }
    }
</script>

<Navbarmedico></Navbarmedico>

<div class="container">
    <div>
        <label for="">Cedula:</label>
        <input type="text" class="mt-3" id="buscardocument_v" />
        <button class="btn btn-outline-info" on:click={buscar}>Buscar</button>
    </div>
    <div class="card border-dark shadow mt-5">
        <div class="card-header">
            <!--Header-->
            <div class="fs-2 text-center">
                Historial clinico de <span class="" id="nombre">.</span>
            </div>
        </div>
        <!--Fin del Header-->

        <div class="card-body">
            <!--Body-->

            <div>
                <label for=""
                    ><b>Documento:</b> <span id="documento"> </span></label
                >
                <br />
                <label for=""
                    ><b>Telefono:</b> <span id="telefono"></span></label
                >
            </div>

            <div class="pt-4">
                <h3 style="color: steelblue;">Antecedentes medicos:</h3>

                <!--Aca estaria la tabla de antecedentes medicos-->
            </div>

            {#if loading}
                <!---->
                <div class="row g-2 justify-content-center">
                    <p
                        class="text-center col-lg-2 col-md-2 col-sm-2 col-12 col-xl-2"
                    >
                        Digita la cedula y dar clic en el boton de buscar...
                    </p>
                    <div
                        class="spinner-border col-lg-4 col-md-4 col-sm-4 col-12 col-xl-4"
                        role="status"
                    >
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </div>
            {:else if error}
                <p class="text-red-500">Error: {error}</p>
            {:else}
                <div class="overflow-x-auto">
                    <table
                        class="min-w-full bg-white border border-gray-300"
                        id="myTable"
                    >
                        <thead>
                            <tr>
                                <th class="px-4 py-2 border"
                                    >Fecha del diagnosticos​</th
                                >
                                <th class="px-4 py-2 border">Sintomas</th>
                                <th class="px-4 py-2 border">Descripcion</th>
                                <th class="px-4 py-2 border"
                                    >Observacion/tratamiento</th
                                >
                            </tr>
                        </thead>

                        <tbody>
                            {#each todos as todo}
                                <tr class="hover:bg-gray-50">
                                    <td class="px-4 py-2 border"
                                        >{todo.fecha_diagnostico}</td
                                    >
                                    <td class="px-4 py-2 border"
                                        >{todo.sintomas}</td
                                    >
                                    <td class="px-4 py-2 border"
                                        >{todo.descripcion}</td
                                    >
                                    <td class="px-4 py-2 border"
                                        >{todo.Observaciontratamiento}</td
                                    >
                                </tr>
                            {/each}
                        </tbody>
                    </table>
                </div>
            {/if}
        </div>
        <!--Fin del body-->

        <div class="card-footer">
            <!--Aca comienza en footer-->
            <div class="text-center">
                <button class="btn btn-outline-info" style="left: ;"
                    >Añadir historial medico</button
                >
            </div>
        </div>
        <!--Aca termina el footer-->
    </div>
</div>
