<script>
    import Navbarmedico from "../../../lib/Navbarmedico.svelte";
    import { onMount } from "svelte";

    let todos = {};
    let loading = true;
    let error = null;
    let exportesModal;
    let opcion;
    let fecha_de = "";
    let fecha_hasta = "";

    onMount(() => {
        const modalElement = document.getElementById("Exported_modal");
        if (modalElement) {
            exportesModal = new bootstrap.Modal(modalElement);
        }
    });

    function showModal() {
        if (exportesModal) {
            exportesModal.show();
        }
    }

    function Ocultar() {
        exportesModal.hide();
    }

    async function generar() {
        let opcion = document.getElementById("opcion").value;
        console.log(opcion);

        let miStorage = window.localStorage;
        let v_id = JSON.parse(miStorage.getItem('usuario'));
        let id_v=v_id.id
        console.log("El id del medico es", id_v)


        try {
            if (opcion == 1) {
                let fecha_de = document.getElementById("desde_citas").value;
                let fecha_hasta = document.getElementById("hasta_citas").value;
                console.log("----Comprando el generar------");
                console.log(fecha_de);
                console.log(fecha_hasta);

                let miStorage = window.localStorage;
                let vid = JSON.parse(miStorage.getItem("usuario"));
                let n = vid.id;
                console.log("agendamos cita");
                console.log(n);

                const response = await fetch(
                    "http://127.0.0.1:8000/reportes_citas_medicos",
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            fecha: fecha_de,
                            fecha2: fecha_hasta,
                            id: id_v                           
                        }),
                    },
                );
                if (!response.ok) throw new Error("Error al cargar los datos");
                const data = await response.json();

                todos = data.resultado;
                console.log(todos);
                setTimeout(() => {
                    globalThis.$("#myTable").DataTable(); // Para convertrlo en datatable :D
                });
                const { jsPDF } = window.jspdf; // Accede a jsPDF desde el objeto global
                const doc = new jsPDF();
                console.log("´probando el response.length");
                console.log(todos.length);

                var body = [];
                for (let i = 0; i < todos.length; i++) {
                    console.log("´probando el for ");
                    console.log(todos[i].fecha);
                    body.push([
                        todos[i].fecha,
                        todos[i].hora,
                        todos[i].medico,
                        todos[i].paciente,
                    ]);
                    console.log("´probando el for 2");
                }
                doc.setFontSize(35);
                doc.setFont("helvetica");
                doc.text(76, 20, "Hostipal");
                const docWidth = doc.internal.pageSize.getWidth();
                doc.line(0, 30, docWidth, 30);
                doc.setFontSize(18);
                doc.text(
                    12,
                    40,
                    "Informacion de las citas registradas en el sistema",
                );
                var columns = ["fecha", "hora", "medico", "paciente"];
                doc.autoTable(columns, body, { margin: { top: 70 } });

                doc.save("Cita_dia.pdf");
                //Popup window position, can be 'top', 'top-start', 'top-end', 'center', 'center-start', 'center-end', 'bottom', 'bottom-start', or 'bottom-end'.
                const Toast = Swal.mixin({
                    toast: true,
                    position: "bottom-start",
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
                    title: "Reporte generado",
                });
            } //fin de la opcion 1
            else if (opcion == 2) {
                let fecha_de = document.getElementById("desde_citas").value;
                let fecha_hasta = document.getElementById("hasta_citas").value;
                console.log("----Comprando el generar 2------");
                console.log(fecha_de);
                console.log(fecha_hasta);
                const response = await fetch(
                    "http://127.0.0.1:8000/reportes_diagnosticos/",
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            fecha: fecha_de,
                            fecha2: fecha_hasta,
                        }),
                    },
                );
                if (!response.ok) throw new Error("Error al cargar los datos");
                const data = await response.json();

                todos = data.resultado;
                console.log(todos);
                setTimeout(() => {
                    globalThis.$("#myTable").DataTable(); // Para convertrlo en datatable :D
                });
                const { jsPDF } = window.jspdf; // Accede a jsPDF desde el objeto global
                const doc = new jsPDF();
                console.log("´probando el response.length");
                console.log(todos.length);
                var body2 = [];
                for (let i = 0; i < todos.length; i++) {
                    console.log("´probando el for ");
                    console.log(todos[i].fecha_diagnostico);
                    body2.push([
                        todos[i].nombre_paciente,
                        todos[i].resultado,
                        todos[i].fecha_diagnostico,
                    ]);
                    console.log("´probando el for 2");
                }
                doc.setFontSize(35);
                doc.setFont("helvetica");
                doc.text(76, 20, "Hostipal");
                const docWidth = doc.internal.pageSize.getWidth();
                doc.line(0, 30, docWidth, 30);
                doc.setFontSize(18);
                doc.text(
                    12,
                    40,
                    "Informacion de los diagnosticos ",
                );
                var columns2 = ["nombre del paciente", "resultado", "fecha del diagnostico",];
                doc.autoTable(columns2, body2, { margin: { top: 70 } });

                doc.save("diagnostico.pdf");
                //Popup window position, can be 'top', 'top-start', 'top-end', 'center', 'center-start', 'center-end', 'bottom', 'bottom-start', or 'bottom-end'.
                const Toast = Swal.mixin({
                    toast: true,
                    position: "bottom-start",
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
                    title: "Reporte de diagnostico generado",
                });
              
            } else {
                let fecha_de = document.getElementById("desde_citas").value;
                let fecha_hasta = document.getElementById("hasta_citas").value;
                console.log("----Comprando el generar 3------");
                console.log(fecha_de);
                console.log(fecha_hasta);
                const response = await fetch(
                    "http://127.0.0.1:8000/reportes_historial/",
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            fecha: fecha_de,
                            fecha2: fecha_hasta,
                        }),
                    },
                );
                if (!response.ok) throw new Error("Error al cargar los datos");
                const data = await response.json();

                todos = data.resultado;
                console.log(todos);
                setTimeout(() => {
                    globalThis.$("#myTable").DataTable(); // Para convertrlo en datatable :D
                });
                const { jsPDF } = window.jspdf; // Accede a jsPDF desde el objeto global
                const doc = new jsPDF();
                console.log("´probando el response.length");
                console.log(todos.length);
                var body3 = [];
                for (let i = 0; i < todos.length; i++) {
                    console.log("´probando el for ");
                    console.log(todos[i].Ultimodiagnostio);
                    body3.push([
                        todos[i].nombre,
                        todos[i].numero_citas,
                        todos[i].Ultimodiagnostio,
                    ]);
                    console.log("´probando el for 2");
                }
                doc.setFontSize(35);
                doc.setFont("helvetica");
                doc.text(76, 20, "Hostipal");
                const docWidth = doc.internal.pageSize.getWidth();
                doc.line(0, 30, docWidth, 30);
                doc.setFontSize(18);
                doc.text(
                    12,
                    40,
                    "Informacion de todas las citas que han tenido los usuarios",
                );
                var columns3 = ["nombre del paciente", "numero de citas", "fecha del ultimo diagnostico",];
                doc.autoTable(columns3, body3, { margin: { top: 70 } });

                doc.save("Historial_citas.pdf");
                //Popup window position, can be 'top', 'top-start', 'top-end', 'center', 'center-start', 'center-end', 'bottom', 'bottom-start', or 'bottom-end'.
                const Toast = Swal.mixin({
                    toast: true,
                    position: "bottom-start",
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
                    title: "Reporte de historial de usuario generado",
                });
            }
        } catch (e) {
            error = e.message;
            alert("No hay datos para mostrar...");
        } finally {
            loading = false;
        }
    }
</script>

<Navbarmedico></Navbarmedico>

<div class="container" style="margin-top: 5%;">
    <div class="text-center pt-1 fs-3">
        <p>Reportes</p>
    </div>
    <div class="row g-2">
        <div class="col-xl-1"></div>
        <div class=" col-xl-10 text-center fs-3 py-5">
            <select class="form-select" id="opcion" style="" required>
                <option value="1">Citas registradas</option>
                <option value="2">Diagnosticos de usuarios</option>
                <option value="3">Usuarios que han tenido citas</option>
            </select>
        </div>
    </div>

    <div class="row">
        <div class="col-xl-6 text-end">
            Desde:
            <input type="date" name="citas" id="desde_citas" />
        </div>
        <div class="col-xl-6">
            Hasta:
            <input type="date" name="citas" id="hasta_citas" />
        </div>
    </div>

    <div class="row">
        <button type="button" class="btn btn-dark mt-4" on:click={generar}
            >Generar</button
        >
    </div>
</div>

<div
    class="modal fade"
    id="Exported_modal"
    tabindex="-1"
    aria-labelledby="rModalLabel"
    aria-hidden="true"
>
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                ></button>
            </div>
            <div class="modal-body row">
                <h3>Como quieres exportar los datos?</h3>
                <button
                    on:click={generar}
                    class="col-md-4 text-decoration-none btn btn-outline-dark"
                    style="margin-left: 4%; margin-top:2%">PDF</button
                >
                <div class="col-md-3" style="color: white;">relleno :D</div>
                <button
                    on:click={Ocultar}
                    class="col-md-4 text-decoration-none btn btn-outline-dark"
                    style="margin-top:2%">Excel</button
                >
            </div>
        </div>
    </div>
</div>

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
                                <td class="px-4 py-2 border">{todo.paciente}</td
                                >
                                <td class="px-4 py-2 border">{todo.medico}</td>
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

<style>
    .container {
        max-width: 600px; /* Limita el ancho del contenedor */
        margin: auto; /* Centra el contenedor horizontalmente */
        padding: 20px; /* Agrega padding interno */
        border-radius: 10px; /* Bordes redondeados */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Sombra para profundidad */
        background-color: #f9f9f9; /* Color de fondo claro */
    }

    @media (max-width: 768px) {
        .col-md-4 {
            width: 100%; /* Hace que los inputs ocupen el 100% en pantallas pequeñas */
        }
    }
</style>