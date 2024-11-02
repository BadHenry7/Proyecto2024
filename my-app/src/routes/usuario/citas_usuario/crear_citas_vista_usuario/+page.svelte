<script>
    import Navbarusuario from "../../../../lib/Navbarusuario.svelte";
    import { onMount } from "svelte";

    let todos = {};
    let loading = true;
    let error = null;
    onMount(async () => {
        

        try {
            console.log("yes");
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
            console.log(Selectpaciente)
        } catch (e) {
            error = e.message;
        } finally {
            loading = false;
        }


    });

    async function Agendar() {

        let miStorage = window.localStorage;
    let vid = JSON.parse(miStorage.getItem('usuario'));
    let n=vid.id
    console.log("agendamos cita")

    console.log(n)
    const vpaciente = n
    const vmedico = document.getElementById("medico").value;
    const vfecha = document.getElementById("c_m_d").value;
    const vhora = document.getElementById("c_m_h").value;
    const vestado=1
    //const vid_usuario=obtener id de esa seleccion
    console.log("Agendar cita al "+"Paciente "+vpaciente+" con el Medico "+vmedico)
    console.log("Agendar a la fecha  "+vfecha+" a la hora "+vhora)
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
                    id_usuario:vmedico,//medico
                    id_paciente:vpaciente,
                }),
            });

            alert("Usuario registrado");    
            document.getElementById("medico").value = "";
            document.getElementById("c_m_d").value = "";
            document.getElementById("c_m_h").value = "";
       
            
        } catch (e) {
            error = e.message;
            alert("Error en la solicitud: " + error);
        }
    
        
    }
</script>

<Navbarusuario></Navbarusuario>
<div class="row g-3">

    <div class="col-xl-4" style="margin-top: 7%; margin-left:5%">
        <div class="row text-center px-4">
            <div class=" ">
                <div class="form" style="margin-top: 9%;">
                <select class="form-select" id="medico" required>
                    <option selected>Elija un medico</option>
                
                </select>
                </div>
            </div>
        </div>
    </div>
    

    <div class="col-xl-3" style="margin-top: 7%;">
        <div class="row text-center px-5 py-2">
            <input type="date" name="citas" id="c_m_d" >
            <input type="time" name="hora_cita" id="c_m_h" style="margin-top: 15%;">
        </div>
    </div>

    <div class="col-xl-4">
        <div class="text-center" style="margin-top:25%;margin-right: 50%;">
            <button class="btn btn-info" on:click={Agendar}> Agendar </button> 
            <button class="btn btn-danger"> X </button>
        </div>
    </div>

</div>
