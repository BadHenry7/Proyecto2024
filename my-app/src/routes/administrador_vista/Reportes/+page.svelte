<script>
    import Navbaradmin from "../../../lib/Navbaradmin.svelte";
    import { onMount } from "svelte";

    let todos = {};
    let doctores = {};
    let loading = true;
    let error = null;
    let exportesModal;
    let opcion;
    let fecha_de = "";
    let fecha_hasta = "";
    const serviceID = "service_yev294m";
    const templateID = "template_833f5mc";
    const apikey = "gVmq9ZyZNWP2_LzXW";
    let pdfUrl = "";
    let calendarElement;
    let calendarInstance;
    let visualizar=null


    onMount(() => {
        const modalElement = document.getElementById("sendpdf");
        if (modalElement) {
            exportesModal = new bootstrap.Modal(modalElement);
        }

        if (calendarElement) {
            calendarInstance = new coreui.Calendar(calendarElement, {
                locale: "es-ES",
                calendars: 1,
                range: true,
            });
        }

        console.log("esto que es", calendarInstance);
    });

    function showModal() {
        if (exportesModal) {
            exportesModal.show();
        }

        select_doctor();
    }

    function Ocultar() {
        location.reload();
    }
    
    let fecha_desde = "";
    let hasta_fecha = "";

    async function generar() {
        visualizar=true
        console.log("esto tiene", calendarInstance);
        fecha_desde = calendarInstance._startDate;
        hasta_fecha = calendarInstance._endDate;
        console.log(
            "---------------------------- Separacion ----------------------------",
        );
        console.log(fecha_desde);
        console.log(hasta_fecha);

        let opcion = document.getElementById("opcion").value;
        console.log(opcion);
        try {
            if (opcion == 1) {
                let fecha_1 = new Date(fecha_desde);
                let fecha_de = fecha_1.toISOString().split("T")[0];

                let fecha_2 = new Date(hasta_fecha);
                let fecha_hasta = fecha_2.toISOString().split("T")[0];

                if (fecha_de == "") {
                    // return alert("no hay datos para mostrar"), window.location.href="/administrador_vista/Reportes"
                }

                console.log("----Comprando el generar------");
                console.log(fecha_de);
                console.log(fecha_hasta);

                let miStorage = window.localStorage;
                let vid = JSON.parse(miStorage.getItem("usuario"));
                let n = vid.id;
                console.log("agendamos cita");
                console.log(n);

                const response = await fetch(
                    "http://127.0.0.1:8000/reportes_citas/",
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
                doc.autoTable({
                    columns: columns,
                    body: body,
                    margin: { top: 70 },
                });

                //modal de previsualizacion de pdf
                const pdfBlob = doc.output("blob");
                pdfUrl = URL.createObjectURL(pdfBlob);

                document.getElementById("pdfvista").src = pdfUrl;
                
                const Toast = Swal.mixin({
                    toast: true,
                    position: "bottom-start",
                    showConfirmButton: false,
                    timer: 1500,
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
                let fecha_1 = new Date(fecha_desde);
                let fecha_de = fecha_1.toISOString().split("T")[0];

                let fecha_2 = new Date(hasta_fecha);
                let fecha_hasta = fecha_2.toISOString().split("T")[0];
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
                doc.text(12, 40, "Informacion de los diagnosticos ");
                var columns2 = [
                    "nombre del paciente",
                    "resultado",
                    "fecha del diagnostico",
                ];
                doc.autoTable({
                    columns: columns2,
                    body: body2,
                    margin: { top: 70 },
                });
                
                //modal de previsualizacion de pdf
                const pdfBlob = doc.output("blob");
                pdfUrl = URL.createObjectURL(pdfBlob);

                document.getElementById("pdfvista").src = pdfUrl;
                
                const Toast = Swal.mixin({
                    toast: true,
                    position: "bottom-start",
                    showConfirmButton: false,
                    timer: 1500,
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


                // doc.save("diagnostico.pdf");
                // //Popup window position, can be 'top', 'top-start', 'top-end', 'center', 'center-start', 'center-end', 'bottom', 'bottom-start', or 'bottom-end'.
                // const Toast = Swal.mixin({
                //     toast: true,
                //     position: "bottom-start",
                //     showConfirmButton: false,
                //     timer: 3000,
                //     timerProgressBar: true,
                //     didOpen: (toast) => {
                //         toast.onmouseenter = Swal.stopTimer;
                //         toast.onmouseleave = Swal.resumeTimer;
                //     },
                // });
                // Toast.fire({
                //     icon: "success",
                //     title: "Reporte de diagnostico generado",
                // });
                
            } else {
                let fecha_1 = new Date(fecha_desde);
                let fecha_de = fecha_1.toISOString().split("T")[0];

                let fecha_2 = new Date(hasta_fecha);
                let fecha_hasta = fecha_2.toISOString().split("T")[0];
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
                var columns3 = [
                    "nombre del paciente",
                    "numero de citas",
                    "fecha del ultimo diagnostico",
                ];
                doc.autoTable({
                    columns: columns3,
                    body: body3,
                    margin: { top: 70 },
                });

                //modal de previsualizacion de pdf
                const pdfBlob = doc.output("blob");
                pdfUrl = URL.createObjectURL(pdfBlob);

                document.getElementById("pdfvista").src = pdfUrl;
                
                const Toast = Swal.mixin({
                    toast: true,
                    position: "bottom-start",
                    showConfirmButton: false,
                    timer: 1500,
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

                // doc.save("Historial_citas.pdf");
                // //Popup window position, can be 'top', 'top-start', 'top-end', 'center', 'center-start', 'center-end', 'bottom', 'bottom-start', or 'bottom-end'.
                // const Toast = Swal.mixin({
                //     toast: true,
                //     position: "bottom-start",
                //     showConfirmButton: false,
                //     timer: 3000,
                //     timerProgressBar: true,
                //     didOpen: (toast) => {
                //         toast.onmouseenter = Swal.stopTimer;
                //         toast.onmouseleave = Swal.resumeTimer;
                //     },
                // });
                // Toast.fire({
                //     icon: "success",
                //     title: "Reporte de historial de usuario generado",
                // });
            }
        } catch (e) {
            error = e.message;
            alert("No hay datos para mostrar...");
        } finally {
            loading = false;
        }
    }

    function sendEmail() {
        let as = document.getElementById("asunto_c").value;
        let ms = document.getElementById("mensaje_c").value;
        let enlace = document.getElementById("linking").value;

        for (let i = 0; i < seleccion_doctor.length; i++) {
            let ce = seleccion_doctor[i];

            emailjs.init(apikey);
            emailjs
                .send(serviceID, templateID, {
                    asunto: as,
                    email: ce,
                    file: enlace,
                    message: ms,
                })
                .then((result) => {
                    console.log("Correo enviado con éxito a ", ce);
                })
                .catch((error) => {
                    console.log("Error al enviar el correo:", error.text);
                });
        }
    }

    function formSubmit(event) {
        event.preventDefault();
        sendEmail();
    }

    let seleccion_doctor = [];
    let seleccionado = [];
    let loading_select = false;
    async function select_doctor() {
        try {
            const response = await fetch("http://127.0.0.1:8000/getmedico");
            const data = await response.json();
            doctores = data.resultado;
            console.log("eu", doctores);

            const select_doctor = document.getElementById("select_email");
            select_doctor.innerHTML = "<option>Eliga un medico</option>";

            console.log(doctores[0]);
            for (let i = 0; i < doctores.length; i++) {
                const doctor_v = doctores[i];
                const option = document.createElement("option");
                option.value = doctor_v.usuario;
                option.textContent = doctor_v.nombre;
                select_doctor.appendChild(option);
            }
        } catch (e) {
            error = e.message;
            console.log(error);
        }
    }

    let a = {};
    async function select_change() {
        try {
            loading_select = false;
            let v_change = document.getElementById("select_email").value;
            console.log("funcion select_change", v_change);
            seleccion_doctor.push(v_change);
            a = seleccion_doctor;
            console.log("funcion push", seleccion_doctor);
        } catch (e) {
            error = e.message;
            console.log(error);
        } finally {
            loading_select = true;
        }
    }
</script>

<link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
/>
<link
    rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/@coreui/coreui-pro@5.10.0/dist/css/coreui.min.css"
/>


<Navbaradmin></Navbaradmin>

<div class="container d-flex justify-content-between mt-3">
    <!-- Tarjeta de Reportes -->
    <div class="card shadow-lg p-4" style="width: 500px; background: #f0f4f8; border-radius: 12px;">
        <h3 class="text-center mb-4 text-danger">Reportes</h3>

        <select class="form-select mb-3" id="opcion" required>
            <option value="1">Citas registradas</option>
            <option value="2">Diagnósticos de usuarios</option>
            <option value="3">Usuarios que han tenido citas</option>
        </select>

        <div class="d-flex justify-content-center">
            <div
                    bind:this={calendarElement}
                    class="border rounded p-2 bg-white calendar-container"
                ></div>
        </div>        

        <button on:click={generar} class="btn btn-success mt-3">Generar</button>
        <button on:click={showModal} class="btn btn-secondary mt-2">Enviar correo</button>
    </div>

    <!-- Contenedor del PDF alineado a la derecha -->
     {#if visualizar}
    <div id="pdfContainer" class="ms-4">
        <iframe title="pdf" id="pdfvista" style="width: 800px; height: 600px;"></iframe>
    </div>
    {:else}
    <div class="">
        <div class="card shadow-lg border-0 ms-4 " style="width: 800px; height: 600px;">
          <div class="card-body">
            <h3 class="text-center text-primary fw-bold">Vista previa de documentos PDF</h3>
            <p class="text-secondary mt-3" style="text-align: justify; line-height: 1.6;">
              Aquí podrás visualizar tus archivos PDF antes de proceder con la descarga. Esta función te permitirá revisar cada detalle del documento para asegurarte de que toda la información es correcta y está bien organizada.  
              <br /><br />
              Antes de descargarlo, puedes verificar nombres, fechas, contenido y cualquier otro dato relevante. De esta manera, evitamos errores y garantizamos que el documento final sea exactamente lo que necesitas.  
              <br /><br />
              Si encuentras algún error o necesitas hacer modificaciones, puedes regresar y realizar los ajustes necesarios antes de obtener tu versión definitiva. La visualización previa también te ayudará a ahorrar tiempo, evitando descargas innecesarias y asegurando que solo almacenes los archivos correctos en tu dispositivo.  
              <br /><br />
              Una vez estés seguro de que todo está en orden, podrás proceder a la descarga del PDF con total confianza. Recuerda que esta herramienta está diseñada para facilitar tu trabajo y brindarte una experiencia más eficiente y sin inconvenientes.
            </p>
          </div>
        </div>
      </div>
      
    {/if}

</div>

<div
    class="modal fade"
    id="sendpdf"
    tabindex="-1"
    aria-labelledby="rModalLabel"
    data-bs-backdrop="static"
    data-bs-keyboard="false"
    aria-hidden="true"
>
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <div>
                    <h3>Enviar correo</h3>
                </div>
                <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                    on:click={Ocultar()}
                ></button>
            </div>
            <div class="modal-body row">
                <label
                    >Doctores
                    <select
                        class="form-control"
                        name=""
                        id="select_email"
                        on:change={select_change}
                    >
                        <option value="" disabled selected class="form-select"
                            >Seleccione un medico</option
                        >
                    </select>
                </label>

                {#if loading_select}
                    <p style="margin-top: 2%;">
                        Correos a los cuales se les enviara:
                    </p>
                    {#each a as todos_d, i}
                        {console.log("aca entro o no", a)}
                        <span class="mt-1" style="font-weight: bold;"
                            >{todos_d}</span
                        >
                    {/each}
                {/if}

                <label class="mt-3"
                    >Asunto del mensaje:
                    <input type="text" id="asunto_c" class="form-control" />
                </label>

                <label
                    >Mensaje:
                    <input
                        type="text"
                        name=""
                        id="mensaje_c"
                        class="form-control"
                    />
                </label>

                <label for=""
                    >Link:
                    <input type="text" id="linking" class="form-control" />
                </label>

                <input
                    type="submit"
                    value="Enviar"
                    class="mt-3 btn btn-info"
                    on:click={formSubmit}
                />
            </div>
        </div>
    </div>
</div>

<!-- <div id="Mostrarusuario">
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
</div> -->

<!-- <style>
    .container {
        max-width: 600px; /* Limita el ancho del contenedor */
        margin: auto; /* Centra el contenedor horizontalmente */
        padding: 20px; /* Agrega padding interno */
        border-radius: 10px; /* Bordes redondeados */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Sombra para profundidad */
        background-color: #f9f9f9; /* Color de fondo claro */
    }
</style> -->
