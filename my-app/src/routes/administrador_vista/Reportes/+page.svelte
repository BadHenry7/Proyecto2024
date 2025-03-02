

<!--
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
    const serviceID = 'service_yev294m'
    const templateID = 'template_833f5mc'
    const apikey = 'gVmq9ZyZNWP2_LzXW'

    onMount(() => {
        const modalElement = document.getElementById("sendpdf");
        if (modalElement) {
            exportesModal = new bootstrap.Modal(modalElement);
        }
    });

    function showModal() {
        if (exportesModal) {
            exportesModal.show();
        }
        
        select_doctor()
    }

    function Ocultar() {
        location.reload();
    }

    async function generar() {
        let opcion = document.getElementById("opcion").value;
        console.log(opcion);
        try { 

            if (opcion == 1) {
                let fecha_de = document.getElementById("desde_citas").value;
                let fecha_hasta = document.getElementById("hasta_citas").value;
                
                if (fecha_de==""){
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




    function sendEmail() {
        let as = document.getElementById("asunto_c").value;
        let ms = document.getElementById("mensaje_c").value;
        let enlace = document.getElementById("linking").value;
    
        for (let i = 0; i < seleccion_doctor.length; i++) {
            let ce = seleccion_doctor[i]    
        
            emailjs.init(apikey); 
            emailjs.send(serviceID, templateID, {
                asunto: as,
                email: ce, 
                file: enlace,
                message: ms
            })
            .then(result => {
                    console.log('Correo enviado con éxito a ',ce);
            })
            .catch(error => {
                console.log('Error al enviar el correo:', error.text);
            })
        }
    }

    function formSubmit(event) {
        event.preventDefault();
        sendEmail()
    }
    
let seleccion_doctor=[]
let seleccionado=[]
let loading_select=false
    async function select_doctor() {
        try{
            
            const response = await fetch("http://127.0.0.1:8000/getmedico")
            const data = await response.json();
            doctores = data.resultado;
            console.log("eu",doctores);

            const select_doctor= document.getElementById("select_email");
             select_doctor.innerHTML= "<option>Eliga un medico</option>";

            console.log(doctores[0])
            for (let i = 0; i < doctores.length; i++) {
                const doctor_v = doctores[i];
                const option= document.createElement("option");
                option.value=doctor_v.usuario
                option.textContent=doctor_v.nombre
                select_doctor.appendChild(option);
            } 
                   

        }catch(e){
            error=e.message
            console.log(error)
        }
    }

    let a={}
    async function select_change() {
        try{
            loading_select=false 
            let v_change= document.getElementById("select_email").value;
            console.log("funcion select_change",v_change)
            seleccion_doctor.push(v_change)
            a=seleccion_doctor
            console.log("funcion push",seleccion_doctor)
            

        }catch(e){
           
            error=e.message;
            console.log(error)
        }finally{
            loading_select=true
        }
    }

</script>
-->

<link
rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/@coreui/coreui-pro@5.10.0/dist/css/coreui.min.css"
/>
<Navbaradmin></Navbaradmin>


<script>
    import { onMount } from "svelte";
    import Navbaradmin from "../../../lib/Navbaradmin.svelte";
    
    let calendarElement;
  
    onMount(() => {
      if (calendarElement) {
        new coreui.Calendar(calendarElement, {
          locale: "en-US",
          calendars: 1,
          range: true
        });
      }
    });
  </script>
  
  <div class="d-flex justify-content-center">
    <div bind:this={calendarElement} class="border rounded"></div>
  </div>
  
  







<!--


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
        <div class="col-xl-6 text-start">
            Desde:
            <input type="date" name="citas" id="desde_citas" class="form-control"/>
        </div>
        <div class="col-xl-6">              
            Hasta:
            <input type="date" name="citas" id="hasta_citas" class="form-control"/>
        </div>
    </div>

    <div class="row">
        <button type="button" class="btn btn-dark mt-4"   on:click={generar}>Generar</button>
        <button type="button" class="btn btn-dark mt-4"   on:click={showModal} >Enviar correo</button>

    </div>
</div>


<div class="modal fade" id="sendpdf" tabindex="-1" aria-labelledby="rModalLabel" data-bs-backdrop="static" data-bs-keyboard="false" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <div>
                    <h3>Enviar correo</h3>
                </div>
                <button  type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close" on:click={Ocultar()}></button>
            </div>
            <div class="modal-body row">
                
                <label>Doctores
                    <select class="form-control" name="" id="select_email" on:change={select_change}>
                        <option value="" disabled selected class="form-select">Seleccione un medico</option>
                    </select>
                </label>

                {#if loading_select}
                    <p style="margin-top: 2%;">Correos a los cuales se les enviara:</p>
                    {#each a as todos_d, i}
                        {console.log("aca entro o no",a)}
                        <span class="mt-1" style="font-weight: bold;">{todos_d}</span>
                    {/each}
                {/if}
                
                <label class="mt-3">Asunto del mensaje:
                    <input type="text" id="asunto_c" class="form-control">
                </label>

                <label>Mensaje:
                    <input type="text" name="" id="mensaje_c" class="form-control">
                </label>

                <label for="">Link:
                    <input type="text" id="linking" class="form-control">
                </label>
                
                <input type="submit" value="Enviar" class="mt-3 btn btn-info" on:click={formSubmit}>
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


-->


