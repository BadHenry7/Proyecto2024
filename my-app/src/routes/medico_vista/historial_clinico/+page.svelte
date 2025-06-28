<script>
    import Navbarmedico from "$lib/Navbarmedico.svelte";
    import { onMount } from "svelte";

    let loading = true;
    onMount(async () => {
        try {
            const response = await fetch(
                "http://127.0.0.1:8000/get_cita_admin/",
                {
                    method: "GET",
                },
            );
            const data = await response.json();
            citas = data.resultado;
            console.log("citas", citas);
        } catch (e) {
            error = e.message;
            console.log(error);
        } finally {
        }
    });

    let todos = {};
    let todos2 = {};
    let citas = {};
    let error = null;
    let comprobar = false;

    async function buscar() {
        let buscardocument_v =
            document.getElementById("buscardocument_v").value;
        console.log("documento a buscar: ", buscardocument_v);
        const response = await fetch(
            "http://127.0.0.1:8000/get_user_document",
            {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                },
                body: JSON.stringify({
                    documento: buscardocument_v,
                }),
            },
        );
        loading = false;
        const data = await response.json();
        console.log(data);
        todos = data;
        console.log("Nombre del usuario: ", todos.nombre);
        document.getElementById("nombre").textContent = todos.nombre;
        document.getElementById("documento").textContent = todos.documento;
        document.getElementById("telefono").textContent = todos.telefono;
        nombre_v = todos.nombre;
        let v_id = todos.id;
        console.log("id del usuario", v_id);

        setTimeout(() => {
            globalThis.$("#myTable").DataTable(); // Para convertrlo en datatable :D
        }, 0);
        try {
            const response = await fetch(
                "http://127.0.0.1:8000/historia_clinica",
                {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json",
                    },
                    body: JSON.stringify({
                        id_paciente: v_id,
                    }),
                },
            );
            const data = await response.json();
            console.log("Data de cita");
            console.log(data);
            todos2 = data.resultado;
            console.log(todos2);
            comprobar = true;
        } catch (e) {
            error = e.message;
            console.log(error);
        }
    }
    var nombre_v = "";
    async function editar() {
        console.log("Entro a todos");
        document.getElementById("nombre_v").textContent = nombre_v;

        //Mostrar el card que permite añadir otro historial clinico
        const v_editar = document.getElementById("nav-listado");
        v_editar.removeAttribute("class");

        //Ocultar historial clinico
        let ocultar = document.getElementById("Mostrarhistorial");
        ocultar.setAttribute("class", "fade");

        //cambiar de posicion
        const cambiar = ocultar.parentElement;
        cambiar.insertBefore(v_editar, ocultar);

        const v_edit_sintomas = document.getElementById("sintomas");
        v_edit_sintomas.removeAttribute("readonly");
        v_edit_sintomas.focus();

        const v_edit_descripcion_sintomas = document.getElementById(
            "descripcion_sintomas",
        );
        v_edit_descripcion_sintomas.removeAttribute("readonly");

        const v_edit_diagnostico = document.getElementById("diagnostico");
        v_edit_diagnostico.removeAttribute("readonly");

        const v_edit_descripciond = document.getElementById(
            "descripcion_diagnostico",
        );
        v_edit_descripciond.removeAttribute("readonly");

        const v_edit_Observaciontratamiento = document.getElementById(
            "Observaciontratamiento",
        );
        v_edit_Observaciontratamiento.removeAttribute("readonly");
    }

    async function guardar() {
        console.log("entra a actualizar");
        console.log(todos);
        let sintomas_v = document.getElementById("sintomas").value;
        let descripcions_v = document.getElementById( "descripcion_sintomas").value;
        let estado_v = 1;
        let v_id_paciente = todos.id;
        console.log(v_id_paciente);
        try {
            let id_cita_v=document.getElementById('citas').value;
            console.log("id de la cita", id_cita_v)
            const response = await fetch("http://127.0.0.1:8000/create_sintomas", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    nombre: sintomas_v,
                    descripcion: descripcions_v,
                    estado: estado_v,
                    id_cita: id_cita_v,
                }),
            });
        } catch (e) {
            error = e.message;
            console.log(error);
        }

        try {
            let id_cita_v=document.getElementById('citas').value;
            console.log("id de la cita", id_cita_v)

            let diagnostico_v=document.getElementById('diagnostico').value;
            let descripcions_d = document.getElementById( "descripcion_diagnostico").value;
            let Observacion_v = document.getElementById( "Observaciontratamiento").value;
            let v_estado=1
            
            

            const response = await fetch("http://127.0.0.1:8000/create_diagnosticos", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id_cita: id_cita_v,//mano ya estas ahi?
                    resultado: diagnostico_v,
                    descripcion: descripcions_d,
                    Observacion: Observacion_v,
                    estado: v_estado
                }),
            });

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
          icon: "Success",
          iconColor: "white",
          color: "white",
          background: "green",
          title: "Historial clinico añadido",
        });


        setTimeout(() => {
        location.reload();
      }, 3000);

        } catch (e) {
            error = e.message;
            console.log(error);
        }
    }

    async function incapacidad() {
        try {

            let miStorage = window.localStorage;
            let usuario = JSON.parse(miStorage.getItem('usuario'));
            let v_id_doctor=usuario.id
    

            let v_id_paciente= todos.id
            console.log(v_id_paciente)

            
            let v_descripcion= document.getElementById('v_descripcion').value;
            console.log(v_descripcion)

            let v_observaciones= document.getElementById('v_observaciones').value;
            console.log(v_observaciones)

            let v_dia_incapacidad= document.getElementById('v_dia_incapacidad').value;
            console.log(v_dia_incapacidad)

            const response = await fetch("http://127.0.0.1:8000/incapacidad", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    descripcion: v_descripcion,
                    dias_de_incapacidad: v_dia_incapacidad,
                    id_usuario: v_id_paciente,
                    id_doctor: v_id_doctor,
                    observaciones: v_observaciones
                }),
            });

            alert("añadido :D")

        } catch (e) {
            error = e.message;
            console.log(error);
        } 
    }

    async function Camara() {
           let v_id = todos.id;
    

        const img = document.getElementById('video');
        img.src = ''; 
        setTimeout(() => {
            img.src = 'http://127.0.0.1:8000/video_feed?id=' + v_id + '&cache=' + Date.now();
        }, 200); 

        
//     navigator.mediaDevices.getUserMedia({audio: false, video: true}).then(async(stream)=>{
//    console.log("Stream",stream)
//    let video= document.getElementById('video');
//    video.srcObject = stream

   
//     video.onloadedmetadata =(ev)=>video.play()

//     }).catch((err)=>console.log(err))
    
        
    }

//     async function capturar() {
//          const canvas = document.createElement("canvas");

//   canvas.width = video.videoWidth;
//   canvas.height = video.videoHeight;
//   const context = canvas.getContext("2d");
//   context.drawImage(video, 0, 0, canvas.width, canvas.height);

//   // Convierte el canvas a base64
//   const dataUrl = canvas.toDataURL("image/jpeg");
//   const base64Image = dataUrl.split(',')[1]; // Solo los datos

//     const response = await  fetch ('http://127.0.0.1:8000/Altura_paciente',{

//         "method": "POST",
//         headers: {
//                     "Content-Type": "application/json",
//                 },
//                 body: JSON.stringify({
//                    image: base64Image
//                 }),
//     });
//     const data = await response.json();
//     console.log("Estamos haciendo prueba con la altura", data)


//     }
 
</script>

<Navbarmedico></Navbarmedico>
<style>
    .Input_buscar:hover{
        border-color: blue;
    }
</style>
<div class="container mt-3" id="Mostrarhistorial">
    <label for=""><b>Ingrese el número  de documento</b></label>
    <div class="row">
        <div class="col-xl-6 ">
            <div class="input-group">
                <button class="input-group-text" on:click={buscar} aria-label="Buscar"><i class="bi bi-search"  style="color: steelblue" ></i></button>
                <input type="text" class="form-control Input_buscar" id="buscardocument_v" style="">
            </div>
        </div>

       
    </div>

    
    
    <div class="card border-dark shadow mt-5" >
        <div class="card-header" style="background-color: cornflowerblue; color: white;">
            <!--Header-->
            <div class="fs-2 text-center" >
                Historial clinico de <span class="" id="nombre"></span>
            </div>
        </div>
        <!--Fin del Header-->

        <div class="card-body">
            <!--Body-->

            <div>
                <label for=""
                    ><b>Documento:</b> <span id="documento">----------</span></label
                >
                <br />
                <label for=""
                    ><b>Telefono:</b> <span id="telefono">-------------</span></label
                >
            </div>

            <div class="pt-4">
                <h3 style="color: steelblue;">Antecedentes medicos:</h3>

             
            </div>

            {#if loading}
                <!---->
                <div class="row g-2 justify-content-center">
                    <p
                        class="text-center col-lg-2 col-md-2 col-sm-2 col-12 col-xl-2"
                    >
                        <b>Digita la cedula y dar clic en el boton de buscar para cargar el antecedentes...</b>
                    </p>
                   

                    <!---------------------------------------------------------------------------------->

                        <div class="text-center">
                        <div class="spinner-grow text-primary" role="status">
                        <span class="visually-hidden">Loading...</span>
                        </div>
                        <div class="spinner-grow text-secondary" role="status">
                        <span class="visually-hidden">Loading...</span>
                        </div>
                        <div class="spinner-grow text-success" role="status">
                        <span class="visually-hidden">Loading...</span>
                        </div>
                        <div class="spinner-grow text-danger" role="status">
                        <span class="visually-hidden">Loading...</span>
                        </div>
                        <div class="spinner-grow text-warning" role="status">
                        <span class="visually-hidden">Loading...</span>
                        </div>
                        <div class="spinner-grow text-info" role="status">
                        <span class="visually-hidden">Loading...</span>
                        </div>
                        <div class="spinner-grow text-light" role="status">
                        <span class="visually-hidden">Loading...</span>
                        </div>
                        <div class="spinner-grow text-dark" role="status">
                        <span class="visually-hidden">Loading...</span>
                        </div>
                        </div>
                    <!---------------------------------------------------------------------------------->

                    <img src="/Cargando.svg" alt="" class="img-fluid" style="width: 380px;">

                </div>
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
                                <th class="px-4 py-2 border"
                                    >Fecha del diagnosticos​</th
                                >
                                <th class="px-4 py-2 border">Sintomas</th>
                                <th class="px-4 py-2 border"
                                    >Descripcion del sintomas</th
                                >

                                <th class="px-4 py-2 border">Diagnostico</th>
                                <th class="px-4 py-2 border"
                                    >Descripcion del diagnostico</th
                                >
                                <th class="px-4 py-2 border"
                                    >Observacion/tratamiento</th
                                >
                            </tr>
                        </thead>

                        <tbody>
                            {#each todos2 as todo}
                                <tr class="hover:bg-gray-50">
                                    <td class="px-4 py-2 border"
                                        >{todo.fecha_diagnostico}</td
                                    >
                                    <td class="px-4 py-2 border"
                                        >{todo.sintomas}</td
                                    >
                                    <td class="px-4 py-2 border"
                                        >{todo.descripcion_sintomas}</td
                                    >

                                    <td class="px-4 py-2 border"
                                        >{todo.diagnostico}</td
                                    >
                                    <td class="px-4 py-2 border"
                                        >{todo.descripcion}</td
                                    >
                                    <td class="px-4 py-2 border"
                                        >{todo.Observaciontratamiento}</td
                                    >
                                </tr>
                            {/each}
                        </tbody>
                    </table>
                </div>
            {/if}
        </div>
        <!--Fin del body-->
        {#if comprobar}
            <div class="card-footer">
                <!--Aca comienza en footer-->
                <div class="text-center">
                    <button class="btn btn-outline-info" on:click={editar}
                        >Añadir historial medico</button
                    >
                    <button class="btn btn-outline-info"
                    data-bs-toggle="modal"
                    data-bs-target="#incapacidad_modal">Añadir incapacidad medica</button
                >
                </div>
            </div>
        {/if}
        <!--Aca termina el footer-->
    </div>
</div>
<div class="fade" id="nav-listado">
  <div class="container py-5">
    <div class="card shadow-sm">
      <div class="card-header text-center fw-bold fs-5" style="background-color: cornflowerblue; color: white;">
        Historial clínico de <span id="nombre_v"></span>
      </div>

      <div class="card-body">

        
        <div class="mb-3">
          <label class="form-label fw-bold">Síntomas:</label>
          <div class="input-group">
            <span class="input-group-text text-danger"><i class="bi bi-heart-pulse"></i></span>
            <input type="text" class="form-control" id="sintomas" placeholder="Síntomas del paciente" readonly />
          </div>
        </div>

        
        <div class="mb-3">
          <label class="form-label fw-bold">Descripción de los síntomas:</label>
          <div class="input-group">
            <span class="input-group-text text-warning"><i class="bi bi-file-earmark-text" ></i></span>
            <input type="text" class="form-control" id="descripcion_sintomas"  placeholder="Descripción detallada" readonly />
          </div>
        </div>

        
        <div class="mb-3">
          <label class="form-label fw-bold">Diagnóstico:</label>
          <div class="input-group">
            <span class="input-group-text text-primary"><i class="bi bi-clipboard2-pulse"  ></i></span>
            <input type="text" class="form-control" id="diagnostico" placeholder="Diagnóstico del usuario" readonly />
          </div>
        </div>

        
        <div class="mb-3">
          <label class="form-label fw-bold">Descripción del diagnóstico:</label>
          <div class="input-group">
            <span class="input-group-text text-info"><i class="bi bi-journal-text" ></i></span>
            <input type="text" class="form-control" id="descripcion_diagnostico" placeholder="Explicación del diagnóstico" readonly />
          </div>
        </div>

        
        <div class="mb-3">
          <label class="form-label fw-bold">Observación o tratamiento:</label>
          <div class="input-group">
            <span class="input-group-text"><i class="bi bi-capsule-pill" style="color: cadetblue;"></i></span>
            <input type="text" class="form-control" id="Observaciontratamiento"  placeholder="Recomendaciones médicas" readonly />
          </div>
        </div>

        
        <div class="mb-4">
          <label class="form-label fw-bold">Seleccione la cita:</label>
          <div class="input-group">
            <span class="input-group-text"><i class="bi bi-calendar-check" style="color: #6f42c1;"></i></span>
            <select id="citas" class="form-select">
              <option value="">Selecciona una cita</option>
              {#each citas as cita}
                <option value={cita.id}>Fecha: {cita.fecha} - Hora: {cita.hora}</option>
              {/each}
            </select>
          </div>
        </div>

        
        <div class="text-center my-4">
          
          <button on:click={() => Camara()} class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#Camara">
            <i class="bi bi-camera-fill me-1"></i> Calcular estatura
          </button>
        </div>

        <!-- Modal -->
        <div class="modal fade" id="Camara" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="CamaraLabel" aria-hidden="true">
          <div class="modal-dialog modal-lg">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="CamaraLabel">Calculando estatura...</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Cerrar"></button>
              </div>
              <div class="modal-body">
                <img src="" id="video" class="img-fluid w-100 object-fit-cover" style="height: 400px;" />
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cerrar</button>
                <button type="button" class="btn btn-primary">Aceptar</button>
              </div>
            </div>
          </div>
        </div>

        <!-- Guardar -->
        <div class="text-center mt-5">
            <p class="text-muted">¡Al terminar, dale click en guardar para aplicar los cambios!</p>
            <button class="btn btn-success px-4" on:click={guardar}>
                <i class="bi bi-save me-1"></i> Guardar
            </button>
        </div>

      </div>
    </div>
  </div>
</div>



<div class="modal fade"  id="incapacidad_modal" tabindex="-1" aria-labelledby="rModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="mleModalLabel">
                    <b>Incapacidad medica</b>
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
             <p>Ingrese los datos de la incapacidad medica:</p>
            
                <div class="row">
                    <div class="col-xl-12 text-center">
                    <label for="">Duracion de la incapacidad:
                        <input type="text" class="form-control" id="v_dia_incapacidad">
                    </label>
                       
                </div>
                    <div class="col-xl-12 text-center">
                        <label for="">Descripcion:
                        </label>
                            <textarea type="text" class="form-control" id="v_descripcion"></textarea>
                    </div>
                    
                </div>
                <div class=" text-center"><!--Y como se pondria-->
                        <label for="">Observaciones
                        </label>
                        <textarea type="text" class="form-control" id="v_observaciones"></textarea>
                </div>
                
            </div>

            <div class="modal-footer justify-content-center">
                <button class="btn btn-outline-info" on:click={incapacidad}>Añadir incapacidad medica</button>
            </div>
          
        </div>
    </div>
</div>