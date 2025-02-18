<script>
    import Navbarusuario from "../../../../lib/Navbarusuario.svelte";
    import { onMount } from "svelte";

    let todos = {};
    let loading = true;
    let error = null;

    onMount(async () => {
        try {
            
            let miStorage = window.localStorage;
            let vid = JSON.parse(miStorage.getItem("usuario"));
            let n = vid.id;
            console.log("agendamos cita");
            console.log(n);

            const response = await fetch("http://127.0.0.1:8000/post_citas_users/", {
                
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id_paciente: n
                   
                }),
            });
            if (!response.ok) throw new Error("Error al cargar los datos");

            const data = await response.json();
            

                todos = data.resultado;
                console.log(todos);
                setTimeout(() => {
                    globalThis.$("#myTable").DataTable(); // Para convertrlo en datatable :D
                }, 0);
        } catch (e) {
            error = e.message;
            alert("Error en la solicitud: " + error);
        }finally {
      loading = false;
    }
    });
</script>

<Navbarusuario></Navbarusuario>

<div id="Mostrarusuario">
    <div class="container py-4">
        <h2 class="mb-4">Citas agendadas</h2>
        {#if loading}
            <p class="text-center">Cargando datos...</p>
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
                            <th class="px-4 py-2 border">Paciente</th>
                            <th class="px-4 py-2 border">Doctor</th>
                            <th class="px-4 py-2 border">Fecha</th>
                            <th class="px-4 py-2 border">Hora</th>
                            <th class="px-4 py-2 border">Ubicacion</th>
                            <th class="px-4 py-2 border">Salas</th>

                        </tr>
                    </thead>

                    <tbody>
                        {#each todos as todo}
                            <tr class="hover:bg-gray-50">
                                <td class="px-4 py-2 border">{todo.paciente}</td>
                                <td class="px-4 py-2 border">{todo.medico}</td>
                                <td class="px-4 py-2 border">{todo.fecha}</td>
                                <td class="px-4 py-2 border">{todo.hora}</td>
                                <td class="px-4 py-2 border">{todo.ubicacion}</td>
                                <td class="px-4 py-2 border">{todo.salas}</td>

                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>
        {/if}
    </div>
</div>
