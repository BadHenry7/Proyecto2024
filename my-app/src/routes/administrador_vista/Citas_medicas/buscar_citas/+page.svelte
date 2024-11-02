<script>
    import Navbaradmin from "../../../../lib/Navbaradmin.svelte";
    import { onMount } from "svelte";

    let todos = {};
    let loading = true;
    let error = null;

    onMount(async () => {
        try {
            console.log("2");
            const response = await fetch("http://127.0.0.1:8000/get_citas/");
            if (!response.ok) throw new Error("Error al cargar los datos");
            const data = await response.json();
            todos = data.resultado;
            console.log(todos);

            setTimeout(() => {
                globalThis.$("#myTable").DataTable(); // Para convertrlo en datatable :D
            }, 0);
        } catch (e) {
            error = e.message;
        } finally {
            loading = false;
        }
    });
</script>

<Navbaradmin></Navbaradmin>
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
                        </tr>
                    </thead>

                    <tbody>
                        {#each todos as todo}
                            <tr class="hover:bg-gray-50">
                                <td class="px-4 py-2 border">{todo.medico}</td>
                                <td class="px-4 py-2 border">{todo.paciente}</td
                                >
                                <td class="px-4 py-2 border">{todo.fecha}</td>
                                <td class="px-4 py-2 border">{todo.hora}</td>
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>
        {/if}
    </div>
</div>

