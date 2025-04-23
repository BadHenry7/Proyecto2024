<script>
    import Navbarusuario from "../../../../lib/Navbarusuario.svelte";
    import { onMount } from "svelte";

    
    let todos = {};
    let todos_citas={}
    let loading = true;
    let error = null;
    const serviceID = 'service_yev294m'
    const templateID = 'template_i73qkfa'
    const apikey = 'gVmq9ZyZNWP2_LzXW'

   


    onMount(async () => {

        try {
            
            let miStorage = window.localStorage;
            let vid = JSON.parse(miStorage.getItem("usuario"));
            let n = vid.id;
            console.log("agendamos cita");
            console.log(n);

            const response = await fetch("http://127.0.0.1:8000/post_citas_users/", {
                
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id_paciente: n
                   
                }),
            });
            if (!response.ok) throw new Error("Error al cargar los datos");

            const data = await response.json();
            

            todos_citas = data.resultado;
                
                setTimeout(() => {
        globalThis.$("#myTable").DataTable({

            stripeClasses: ["bg-white", "bg-light"], 
            language: {
            url: "//cdn.datatables.net/plug-ins/1.13.4/i18n/es-ES.json",
      },
        }); // Para convertrlo en datatable :D
      
      }, 0);


        } catch (e) {
            error = e.message;
            alert("Error en la solicitud: " + error);
        }finally {
      loading = false;
    }


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

    let date = new Date();
    let  horas= date.getHours()
    if (horas<10){
    console.log("entro",horas)

        horas= "0"+horas
    }

    let v_horas= horas+":00"
    console.log("acacac",v_horas)


//-----------------------------------------------------
//Calculo de fecha:
const year = date.getFullYear();
let month = date.getMonth() + 1;  
let day = date.getDate();
month = month < 10 ? '0' + month : month;
day = day < 10 ? '0' + day : day;

date= year + '-' + month + '-' + day;

//-----------------------------------------------------



    console.log("esto imprine la fecha", date)

    

    let hours=["06:30", "07:00", "07:30", "08:00","08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", 
"12:30", "13:00","13:30", "14:00", "14:30", "15:00","15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30"]
    // fecha actual
    var vhora=""

    function mostrar_horas(hora_onclick){
        vhora = hora_onclick;
        mostrar_fecha()
    }

    function mostrar_fecha() {
        
        

        console.log("entro a mostrar fecha")
        const vfecha = document.getElementById("c_m_d").value;

        if (vfecha>date){
            v_horas="05:00"
        }else{
            v_horas=horas+":00"
        }

    
        //medico
        const vmedico = document.getElementById("medico");
        const nombreMedico= vmedico.options[vmedico.selectedIndex].text;

         const v_ubicacion=document.getElementById("ubicacion").value;
         console.log("aaaaaaa", v_ubicacion)
        

        if (vfecha!=""){
        document.getElementById("mostrar_fecha").innerHTML=vfecha;
        }else{
            document.getElementById("mostrar_fecha").innerHTML="No hay fecha seleccionada";
        }
        if (vhora!="[object Event]" & vhora!=""){
            document.getElementById("mostrar_hora").innerHTML=vhora;
        }else{
            document.getElementById("mostrar_hora").innerHTML="No hay hora seleccionada";
        } if (nombreMedico!="Seleccione" ){
        document.getElementById("mostrar_doctor").innerHTML=nombreMedico;
        }else{
            document.getElementById("mostrar_doctor").innerHTML="No hay doctor seleccionada";
        } 
        if (v_ubicacion!="Seleccione" ){
        document.getElementById("mostrar_ubicacion").innerHTML=v_ubicacion;
        }else{
            document.getElementById("mostrar_ubicacion").innerHTML="No hay ubicacion seleccionada";
        } 

         
    }

   
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
        
        const v_ubicacion = document.getElementById("ubicacion").value;

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
                        ubicacion: v_ubicacion
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


            <!--Eliga la ubicacion-->
          
            <div class="mt-5">
                <label for=""><b>Elija una ubicacion</b></label>
            </div>
            <select  id="ubicacion" class="form-select" required on:change={mostrar_fecha}>
                <option selected>Seleccione</option>
            </select>

        </div>


        <!--Segunda columna-->
        <div class="col-lg-5 col-md-4 col-sm-4 col-4 col-xl-4">
            <label for=""><b>Seleccione una hora</b></label>
            <div class="row">
         {#each hours as hour, i}
          
                {#if hour>v_horas}
                <div class="col-lg-6 col-md-6 col-sm-6 col-6 col-xl-6">
                    <div class="input-group">   
                        <i class="input-group-text bi bi-clock time-icon bg-primary" style="color: aliceblue;  "></i>
                        <input type="time" value="{hour}" on:click={()=>mostrar_horas(hour)} class="form-control" readonly>
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
           
            <p><b>Ubicacion seleccionada:</b><span class="mx-3" id="mostrar_ubicacion"> No hay ubicacion seleccionado</span></p>
            

            <div class="d-flex" style="justify-content: center; align-items: center;">
            <button class="btn btn-primary "  on:click={ConfirmarAgendar}>
                Agendar
            </button>
              </div>
           
        </div>
        <div class="mt-5 fs-5">
            
        <p class="text-center text-muted">Asegúrate de revisar cuidadosamente la información antes de confirmar la cita. Verifica que los datos de la fecha y la hora sean correctos para evitar inconvenientes.</p>
            
        </div>

    </div>

    <br>

    <p class="text-center fs-3"><b>Ver citas programadas</b></p>
    <div id="Mostrarusuario">
        <div class="container ">
            
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
                                <th class="px-4 py-2 border">Ubicacion</th>
                                <th class="px-4 py-2 border">Salas</th>
    
                            </tr>
                        </thead>
    
                        <tbody>
                            {#each todos_citas as todo}
                                <tr class="hover:bg-gray-50">
                                    <td class="px-4 py-2 border">{todo.paciente}</td>
                                    <td class="px-4 py-2 border">{todo.medico}</td>
                                    <td class="px-4 py-2 border">{todo.fecha}</td>
                                    <td class="px-4 py-2 border">{todo.hora}</td>
                                    <td class="px-4 py-2 border">{todo.ubicacion}</td>
                                    <td class="px-4 py-2 border">{todo.salas}</td>
    
                                </tr>
                            {/each}
                        </tbody>
                    </table>
                </div>
            {/if}
        </div>
    </div>
    

</div>


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