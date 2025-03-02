<script>
    import Navbarusuario from "../../../../lib/Navbarusuario.svelte";
    import { onMount } from "svelte";

    let todos = {};
    let loading = true;
    let error = null;
    const serviceID = 'service_yev294m'
    const templateID = 'template_i73qkfa'
    const apikey = 'gVmq9ZyZNWP2_LzXW'

    onMount(async () => {
        try {
            const response = await fetch("http://127.0.0.1:8000/getmedico");
            if (!response.ok) throw new Error("Error al cargar los datos");
            const data = await response.json();
            todos = data.resultado;
            console.log("eu",todos);

            const Selectpaciente = document.getElementById("medico");
            for (let i = 0; i < data.resultado.length; i++) {
                const user = data.resultado[i];

                const option = document.createElement("option");

                option.value = user.id;

                option.textContent = user.nombre;

                Selectpaciente.appendChild(option);
            }
            console.log(Selectpaciente);
        } catch (e) {
            error = e.message;
        } finally {
            loading = false;
        }
    });

   
    function ConfirmarAgendar() {
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
                    Agendar()
                }
            });
}


    async function Agendar() {
        let miStorage = window.localStorage;
        let vid = JSON.parse(miStorage.getItem("usuario"));
        console.log("Contenido del localStorage:", vid);
        let n = vid.id;
        let nb = vid.name;
        let ce = vid.correo;

        console.log("1----------------------------------"+n)
        console.log("2----------------------------------"+nb)
        console.log("3----------------------------------"+ce)

        const vpaciente = n;
        const vmedico = document.getElementById("medico").value;

        const medico_v = document.getElementById("medico");

        var selectedOption = medico_v.options[medico_v.selectedIndex].text;
        console.log("name:",selectedOption)
     
        const vfecha = document.getElementById("c_m_d").value;
        const vhora = document.getElementById("c_m_h").value;
        const vestado = 1;
        //const vid_usuario=obtener id de esa seleccion
        console.log(
            "Agendar cita al " +
                "Paciente " +
                vpaciente +
                " con el Medico " +
                vmedico,
        );
        console.log("Agendar a la fecha  " + vfecha + " a la hora " + vhora);


         

        try {
            const response = await fetch(
                "http://127.0.0.1:8000/create_cita/",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        fecha: vfecha,
                        hora: vhora,
                        estado: vestado,
                        id_usuario: vmedico, //medico
                        id_paciente: vpaciente,
                    }),
                },
            );
            Swal.fire({
                        title: "Cita añadida",
                        text: "Tu cita fue añadida con exito",
                        icon: "success",
                    });
            sendEmail()

            document.getElementById("medico").value = "";
            document.getElementById("c_m_d").value = "";
            document.getElementById("c_m_h").value = "";

            function sendEmail() {
                emailjs.init(apikey); 
                emailjs.send(serviceID, templateID, {
                    nombre: nb,
                    email: ce, 
                    hora: vhora,
                    fecha: vfecha,
                    doctor: selectedOption
                })
                .then(result => {
                        alert('Correo enviado con éxito!');
                    })
                    .catch(error => {
                        console.log('Error al enviar el correo:', error.text);
                    });
            }

        } catch (e) {
            error = e.message;
            alert("Error en la solicitud: " + error);
        }
    }
</script>

<Navbarusuario></Navbarusuario>



<!--
<div
    style="background-image: url('/fondoR.jpg'); background-size: cover; background-position: center;height: 100vh; width: 100vw;"
>
    <h2 class="col-xl-3" style="margin-left: 39%; ">
        AGENDAR CITA
    </h2>

    <div class="row g-3" style="margin-top: 1%; margin-left: 38%;">
        <div class="col-md-3">
            <div>
                <label for="medico">Elija un Doctor</label>
            </div>
            <select class="form-select" id="medico" required>
                <option selected>Seleccione</option>
            </select>
        </div>

        <div>
            <div class="col-md-3" style="margin-right: 9%;">
                <div>
                    <label for="fech">Elija una fecha</label>
                </div>
                <input
                    type="date"
                    class="form-control"
                    name="citas"
                    id="c_m_d"
                    style="margin-top: 10px;"
                />
            </div>
        </div>

        <div>
            <div style="margin-right: 9%;">
                <div>
                    <label for="hora">Elija una hora</label>
                </div>
                <input
                    style="width: 28%;"
                    type="time"
                    name="hora_cita"
                    id="c_m_h"
                />
            </div>
        </div>

        <div class="mb-3">
            <button class="btn btn-success" on:click={ConfirmarAgendar}>
                Agendar
            </button>
            <button class="btn btn-outline-danger"> volver </button>
        </div>
    </div>
</div>
-->