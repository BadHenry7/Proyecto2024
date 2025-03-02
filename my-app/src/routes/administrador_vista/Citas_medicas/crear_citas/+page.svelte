<script>
    import Navbaradmin from "../../../../lib/Navbaradmin.svelte";
    import { onMount } from "svelte";
    

    
    let todos = {};
    let loading = true;
    let error = null;
    let fechaseleccionada = "";
    const quitarfecha = [];
    let date = new Date();
    let  horas= date.getHours()
    if (horas<10){
    console.log("entro",horas)

        horas= "0"+horas
    }


    let v_horas= horas+":00"
    console.log("acacac",v_horas)
    



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


        try{


            const response_node = await fetch("https://api-nodejs-buxf.onrender.com/api/hospitales/gethospitales");
        const data_node= await response_node.json()
        console.log(data_node)//ubicacion
        let todos_node= data_node.data;
        console.log("esto es data de node", todos_node)

        const Select_hospitales = document.getElementById("ubicacion");

        for (let i = 0; i < todos_node.length; i++) {
  
          const hospital = todos_node[i];   
          const option = document.createElement("option");
          option.value = hospital.nombre_hospital;

          option.textContent = hospital.nombre_hospital;
          Select_hospitales.appendChild(option);      
          
        }
        
        console.log(Select_hospitales);  



        }catch(e){
            error=e.message;
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
        const v_ubicacion = document.getElementById("ubicacion").value;

        console.log("vhora de agendar",vhora)
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
                    ubicacion:v_ubicacion
                }),
            });
            Swal.fire({
                        title: "Cita añadida",
                        text: "Tu cita fue añadida con exito",
                        icon: "success",
                    });

                    setTimeout(()=>{
        location.reload();

                    },3000)

        } catch (e) {
            error = e.message;
            alert("Error en la solicitud: " + error);
        }
    }

let hours=["06:30", "07:00", "07:30", "08:00","08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", 
"12:30", "13:00","13:30", "14:00", "14:30", "15:00","15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30"]
    // fecha actual
  
    var vhora=""
    function mostrar_fecha(hora_onclick) {
        
        console.log("entro a mostrar fecha")
        const vfecha = document.getElementById("c_m_d").value;
        //paciente
        const vpaciente = document.getElementById("paciente");
        const nombrePaciente = vpaciente.options[vpaciente.selectedIndex].text;
        //medico
        const vmedico = document.getElementById("medico");
        const nombreMedico= vmedico.options[vmedico.selectedIndex].text;

         vhora = hora_onclick;
        console.log("bhora", vhora)

        if (vfecha!=""){
        document.getElementById("mostrar_fecha").innerHTML=vfecha;
        }else{
            document.getElementById("mostrar_fecha").innerHTML="No hay fecha seleccionada";
        }
        if (vhora!="[object Event]"){
            document.getElementById("mostrar_hora").innerHTML=vhora;
        }else{
            document.getElementById("mostrar_hora").innerHTML="No hay hora seleccionada";
        } if (nombreMedico!="Seleccione" ){
        document.getElementById("mostrar_doctor").innerHTML=nombreMedico;
        }else{
            document.getElementById("mostrar_doctor").innerHTML="No hay doctor seleccionada";
        } if (nombrePaciente!="Seleccione"){
        document.getElementById("mostrar_paciente").innerHTML=nombrePaciente;
        }else{
            document.getElementById("mostrar_paciente").innerHTML="No hay paciente seleccionada";
        }
       

         
    }

// 
  

    
</script>
    

<Navbaradmin></Navbaradmin>
<style>
    
   
  select:hover, input[type="time"]:hover {
    border-color: blue; /* Verde */
    }

    
    input[type="date"]:hover {
    border-color: blue ; /* Verde */
    }

  
    .time-icon {
    
      border-top-left-radius: 8px;
      border-bottom-left-radius: 8px;
    }
    
   
  
    .input-group-text {
      border: none;
    }
  
   
    input[type="time"] {
      background-color: white !important;
      color: black !important;
      cursor: pointer;
      border-radius: 8px;
      text-align: center;
    }
  </style>
  
<div class="container">
    <p class="fs-3 mt-4 text-center"><b>¡Agendar cita!</b></p>
    <hr>
    <p class="text-center">Aquí puedes agendar las citas de los pacientes. Después de seleccionar los datos, haz clic en "Agendar" para completar el registro</p>

    <div class="row pt-2">

        <!--Primera columna-->
        <div class="col-lg-3 col-md-4 col-sm-4 col-4 col-xl-4">
            <div class="" on:change={mostrar_fecha}>
                <label for=""><b>Seleccione una fecha</b></label>
                <input type="date" id="c_m_d" class="form-control">
            </div>
            <!--Eliga un doctor-->
            <div class="mt-5">
                <label for="" ><b>Elija un Doctor</b></label>
            </div>
            <select class="form-select" id="medico" required on:change={mostrar_fecha}>
                <option selected>Seleccione</option>
            </select>


            <!--Eliga un paciente-->
            <div class="mt-5">
                <label for=""><b>Elija un Paciente</b></label>
            </div>
            <select class="form-select" id="paciente" required on:change={mostrar_fecha}>
                <option selected>Seleccione</option>
            </select>

            <div class="mt-5">
                <label for=""><b>Elija una ubicacion</b></label>
            </div>
            <!--Eliga la ubicacion-->
            <select  id="ubicacion" class="form-select" required>
                <option selected>Seleccione</option>
            </select>

        </div>


        <!--Segunda columna-->
        <div class="col-lg-5 col-md-4 col-sm-4 col-4 col-xl-4">
            <label for=""><b>Seleccione una hora</b></label>
            <div class="row">
         {#each hours as hour, i}
          {console.log(v_horas)}
          {console.log(hour)}
                {#if hour>v_horas}
                <div class="col-lg-6 col-md-6 col-sm-6 col-6 col-xl-6">
                    <div class="input-group">   
                        <i class="input-group-text bi bi-clock time-icon bg-primary" style="color: aliceblue;  "></i>
                        <input type="time" value="{hour}" on:click={()=>mostrar_fecha(hour)} class="form-control" readonly>
                    </div>
                </div>
               
                {#if (i + 1) % 2 === 0 }
                <div class="mt-3"></div>
                {/if}
                {/if}

        {/each}
            </div>
        </div>
       


        <!--Tercera columna-->
        <div class="col-lg-4 col-md-4 col-sm-4 col-4 col-xl-4">

           
            <div class="text-center fs-4"><p><b>Detalles de la cita:</b></p></div>
           <p><span><b>Fecha seleccionada:</b></span><span class="mx-3" id="mostrar_fecha">No hay fecha seleccionada</span></p>
           
           <p><b>Hora seleccionada:</b><span class="mx-3" id="mostrar_hora"> No hay hora seleccionada</span></p>

            <p><b>Doctor seleccionado:</b><span class="mx-3" id="mostrar_doctor"> No hay doctor seleccionado</span></p>
            <p><b>Paciente seleccionado:</b><span class="mx-3" id="mostrar_paciente"> No hay paciente seleccionada</span></p>

            <div class="d-flex" style="justify-content: center; align-items: center;">
            <button class="btn btn-primary "  on:click={ConfirmarAgendar}>
                Agendar
            </button>
              </div>
           
        </div>
        <div class="mt-5 fs-5">
        <p class="text-center text-muted">Asegúrate de revisar cuidadosamente la información antes de confirmar la cita. Verifica que los datos del paciente, la fecha y la hora sean correctos para evitar inconvenientes.</p>
        </div>

    </div>


</div>





<!--
<div
    style="background-image: url('/'); background-size: cover; background-position: center;height: 100vh; width: 100vw;"
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
-->