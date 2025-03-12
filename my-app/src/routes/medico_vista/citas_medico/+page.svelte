<script>
    import Navbarmedico from "$lib/Navbarmedico.svelte";

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

            const response = await fetch(
                "http://127.0.0.1:8000/post_citas_doctor",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        id_paciente: n,
                    }),
                },
            );
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
        } finally {
            loading = false;
        }
    });

    function ConfirmarCita(id) {
        let v_id = id;
    Swal.fire({
                title: "¿Confirmas que quieres agendar esta cita?",
                text: "",
                icon: "question",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Si, añadir cita",
            }).then((result) => {
                if (result.isConfirmed) {
                    cita_realizada(v_id)
                }
            });
}

    


    async function cita_realizada(id) {
        let v_id = id;

        const response = await fetch("http://127.0.0.1:8000/eliminar_cita", {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                id: v_id,
            }),
        });

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
          title: "cita actualizada con exito",
        });

        setTimeout(() => {
            location.reload();
        }, 3000);
    }
</script>

<Navbarmedico></Navbarmedico>

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
                    <thead class="bg-primary text-white">
                        <tr>
                            <th class="px-4 py-2 border">Paciente</th>
                            <th class="px-4 py-2 border">Doctor</th>
                            <th class="px-4 py-2 border">Fecha</th>
                            <th class="px-4 py-2 border">Hora</th>
                            <th class="px-4 py-2 border">Opciones</th>
                        </tr>
                    </thead>

                    <tbody>
                        {#each todos as todo}
                            <tr class="hover:bg-gray-50">
                                <td class="px-4 py-2 border">{todo.paciente}</td
                                >
                                <td class="px-4 py-2 border">{todo.medico}</td>
                                <td class="px-4 py-2 border">{todo.fecha}</td>
                                <td class="px-4 py-2 border">{todo.hora}</td>

                                <td class="px-4 py-2 border">
                                    <button
                                        class="btn btn-outline-warning"
                                        on:click={() => ConfirmarCita(todo.id_cita)}
                                        >  <i class="bi bi-check-circle-fill"></i> Cita Realizada</button
                                    >
                                </td>
                            </tr>
                        {/each}
                    </tbody>
                </table>
            </div>
        {/if}
    </div>
</div>
