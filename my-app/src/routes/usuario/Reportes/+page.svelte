<script>
    import Navbarusuario from "../../../lib/Navbarusuario.svelte";

    let todos = {};
    let todos2 = {};
    let loading = true;
    let error = null;
   
    async function Generar() {
        let opcion = document.getElementById("opcion").value;
        let miStorage = window.localStorage;
        let usuario = JSON.parse(miStorage.getItem("usuario"));
        let id_v = usuario.id;
        let nombre_v = usuario.name;
        console.log("El id del usuario es", id_v);
        console.log("El nombre del usuario es", nombre_v);
        console.log("''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''");
        let print=console.log
        print("XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
        try {
            if (opcion == 1) {
                const response = await fetch(
                    "http://127.0.0.1:8000/historia_clinica_user",
                    {
                        method: "POST",
                        headers: {
                            "Content-type": "application/json",
                        },
                        body: JSON.stringify({
                            id_paciente: id_v,
                        }),
                    },
                );
                const data = await response.json();
                console.log("Data de cita");
                console.log(data);
                todos2 = data.resultado;
                console.log(todos2);
                let fecha_v = new Date(todos2[0].fecha_diagnostico);
                let descsin_v = (todos2[0].descripcion_sintomas);
                let diag_v = (todos2[0].diagnostico);
                let sin_v = (todos2[0].sintomas);
                let obsr_v= (todos2[0].Observaciontratamiento);
                let doctor_v= (todos2[0].doictor);
                //console.log("la fecha es", fecha_v)
                //let hora = fecha_v.getHours()
                //let minutos = fecha_v.getMinutes()
                //let tiempo = hora + ":" + minuto + ":";
                //let fecha = 
                let paciente_v=nombre_v;

                console.log("---------------------------------------------------------");
                console.log(paciente_v)
                
                const { jsPDF } = window.jspdf; // Accede a jsPDF desde el objeto global
                const doc = new jsPDF();
                console.log("´probando el response.length");
                // Encabezado
                doc.setFontSize(35);
                doc.setFont("helvetica", "normal");
                doc.addImage('/favicon.png', 'PNG', 10, 10, 20, 20); // x, y, width, height
                doc.setFontSize(14);
                doc.setFont("helvetica", "bold");
                doc.text("HOSTIPAL", 105, 20, { align: "center" });
                // Fin del encabezado

                // Detalles de la cita
                doc.setFontSize(12);
                doc.setFont("helvetica", "bold");
                doc.text ("Cita del dia: ",10, 50)
                doc.setFont("helvetica", "normal");
                doc.text(""+fecha_v, 50, 50, { maxWidth: 150});

                doc.setFont("helvetica", "bold");
                doc.text("Paciente:", 10,70,);
                doc.setFont("helvetica", "normal");
                doc.text(paciente_v, 50,70, { maxWidth: 150});
                
                // Descripcion del sintoma
                doc.setFontSize(12);
                doc.setFont("helvetica", "bold");
                doc.text("Descripcion de sintomas:", 10, 90, { maxWidth: 40})
                doc.setFont("helvetica", "normal");
                doc.text(descsin_v, 50, 90, { maxWidth: 150});


                // Diagnostico
                doc.setFontSize(12);
                doc.setFont("helvetica", "bold");
                doc.text("Diagnostico:", 10, 110);
                doc.setFont("helvetica", "normal");
                doc.text(diag_v, 50, 110, { maxWidth: 150});

                // Síntomas
                doc.setFontSize(12);
                doc.setFont("helvetica", "bold");
                doc.text("Sintomas:", 10, 130);
                doc.setFont("helvetica", "normal");
                doc.text(sin_v, 50, 130, { maxWidth: 150});
                
               // Observaciones
                doc.setFontSize(12);
                doc.setFont("helvetica", "bold");
                doc.text("Observaciones: ",10, 150);
                doc.setFont("helvetica", "normal");
                doc.text(obsr_v, 50, 150, { maxWidth: 150});

                // Pie de página
                doc.setFontSize(10);
                doc.setFont("helvetica", "bold");
                doc.text("Doctor", 10, 280)
                doc.setFont("helvetica", "normal");
                doc.text(doctor_v, 25, 280);

                doc.text("Derechos reservados", 105, 280, { align: "center" });

                doc.save("Ultima_cita_Medica.pdf");
                //doc.save("Cita_usuario.pdf");
                const Toast = Swal.mixin({
                    toast: true,
                    position: "bottom-end",
                    showConfirmButton: false,
                    timer: 4000,
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

            } else if (opcion == 2) {
                const response = await fetch(
                    "http://127.0.0.1:8000/post_citas_users/",
                    {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            id_paciente: id_v,
                        }),
                    },
                );
                if (!response.ok) throw new Error("Error al cargar los datos");
                const data = await response.json();
                todos = data.resultado;
                let name = data.paciente;
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
                    body.push([todos[i].fecha, todos[i].hora, todos[i].medico]);
                }
                doc.setFontSize(35);
                doc.setFont("helvetica");
                doc.text(76, 20, "Hostipal");
                const docWidth = doc.internal.pageSize.getWidth();
                doc.line(0, 30, docWidth, 30);
                doc.setFontSize(18);
                doc.text(12, 40, "Las citas medicas pendientes que tienes son");
                var columns = ["fecha", "hora", "medico"];
                doc.autoTable(columns, body, { margin: { top: 70 } });

                doc.save("Cita_usuario.pdf");
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
                    title: "Reporte generado",
                });
            }
        } catch (e) {
            error = e.message;
            console.log(error)
            alert("No hay datos para mostrar...");
        } finally {
            loading = false;
        }
    }
</script>

<Navbarusuario></Navbarusuario>

<div class="container">
    <div>
        <div class="text-center">
            <div class="pt-2 mt-1">
                <p class="fs-3">Reportes</p>
                <p>Seleccione el reporte que desea generar:</p>
                <form class="mb-5">
                    <select class="mt-1" id="opcion" required>
                        <option value="1">Ultima cita medica</option>
                        <option value="2">Citas agendadas</option>
                    </select>
                </form>
                <button class="btn btn-success mt-1" on:click={Generar}
                    >Generar</button
                >
            </div>
        </div>
    </div>
</div>
