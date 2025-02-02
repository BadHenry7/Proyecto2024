<script>
    import Navbaradmin from "$lib/Navbar.svelte";

    import { onMount } from "svelte";

    let todos = {};
    let loading = true;
    let error = null;
    let fechaseleccionada = "";
    const quitarfecha = [];

    function verificarFecha() {
        if (quitarfecha.includes(fechaseleccionada)) {
            console.log("Fecha no disponible");
            fechaseleccionada = "";
        }
    }
    onMount(async () => {
        try {
            console.log("entra al try de /getpaciente");
            const response = await fetch("http://127.0.0.1:8000/getpaciente");
            if (!response.ok) throw new Error("Error al cargar los datos");
            const data = await response.json();
            todos = data.resultado;
            console.log(todos);
            console.log(todos.usuario);

            const Selectpaciente = document.getElementById("paciente");
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

        try {
            console.log("entra al try de /getmedico");
            const response = await fetch("http://127.0.0.1:8000/getmedico");
            if (!response.ok) throw new Error("Error al cargar los datos");
            const data = await response.json();
            todos = data.resultado;
            console.log(todos);
            console.log(todos.usuario);

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
        const vpaciente = document.getElementById("paciente").value;
        const vmedico = document.getElementById("medico").value;
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
            
            const response = await fetch("http://127.0.0.1:8000/create_cita/", {
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
            });
            Swal.fire({
                        title: "Cita añadida",
                        text: "Tu cita fue añadida con exito",
                        icon: "success",
                    });

        document.getElementById("paciente").value="";
        document.getElementById("medico").value="";
        document.getElementById("c_m_d").value=""
        document.getElementById("c_m_h").value="";

        } catch (e) {
            error = e.message;
            alert("Error en la solicitud: " + error);
        }
    }

    //no se si servira pero me gustaria pensar que si llega a servir las horas sera el mismo funcionamiento las mismas
</script>

<Navbaradmin></Navbaradmin>

<!-- Aquí puedes colocar contenido adicional -->

<div
    style="background-image: url('/fondoR.jpg'); background-size: cover; background-position: center;height: 100vh; width: 100vw;"
>
    <h2 class="col-xl-3" style="margin-left: 39%; ">AGENDAR CITA</h2>
    <div class="row g-3" style="margin-top: 1%; margin-left: 38%;">
        <div>
            <div class="col-md-3">
                <div>
                    <label for="">Elija un Doctor</label>
                </div>
                <select class="form-select" id="medico" required>
                    <option selected>Seleccione</option>
                </select>
            </div>
        </div>

        <div>
            <div class="col-md-3">
                <div>
                    <label for="">Elija un Paciente</label>
                </div>
                <select class="form-select" id="paciente" required>
                    <option selected>Seleccione</option>
                </select>
            </div>
        </div>

        <div class="">
            <div class="col-md-3" style="margin-right: 9%;">
                <div>
                    <label for="">Elija una fecha</label>
                </div>
                <input
                    type="date"
                    class="form-control"
                    name="citas"
                    id="c_m_d"
                    style="margin-top: 10px;"
                    bind:value={fechaseleccionada}
                    on:input={verificarFecha}
                />
            </div>
        </div>

        <div class="">
            <div style="margin-right: 9%;">
                <div>
                    <label for="">Elija una Hora</label>
                </div>
                <input
                    style="width: 28%;"
                    type="time"
                    name="hora_cita"
                    id="c_m_h"
                />
            </div>
        </div>

        <div class="mb-3 mx-5 px-5 text-start">
            <button class="btn btn-success" on:click={ConfirmarAgendar}>
                Agendar
            </button>
          
        </div>
    </div>
</div>
