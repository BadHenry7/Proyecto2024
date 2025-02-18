<script>
import Navbaradmin from "$lib/Navbar.svelte";

  import { onMount } from "svelte";

  let todos = {};
  let loading = true;
  let error = null;
  let medico = {};
  

  onMount(async () => {
    try {
      console.log("2");
      const response = await fetch("http://127.0.0.1:8000/get_cita_admin/");
      if (!response.ok) throw new Error("Error al cargar los datos");
      const data = await response.json();
      todos = data.resultado;
      console.log(todos);

      setTimeout(() => {
        globalThis.$("#myTable").DataTable(); // Para convertrlo en datatable :D
      }, 0);
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  });

  async function Ocultar() {
    const v_editar = document.getElementById("nav-listado");
    v_editar.setAttribute("class", "fade");

    let mostrar = document.getElementById("Mostrarcitas");
    mostrar.removeAttribute("class");

    location.reload();
  }

  var vid = 1;
  async function editar(id) {
    const v_editar = document.getElementById("nav-listado");
    v_editar.removeAttribute("class");
    vid = id;

    let ocultar = document.getElementById("Mostrarcitas");
    ocultar.setAttribute("class", "fade");

    const cambiar = ocultar.parentElement;

    cambiar.insertBefore(v_editar, ocultar);
 

    try {
      console.log("Entra al try de buscar");

      const response = await fetch("http://127.0.0.1:8000/editar_cita/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id: vid,
        }),
      });
      console.log("Sale del try de buscar");
      const data = await response.json();
      console.log("____________________________");
      /*   
                    'fecha':data[0],
                    'hora':str(data[1]),
                    'medico':data[2],
                    'paciente':data[3],
                    'id':data[4]
      */
      todos = data.resultado;
      console.log("Buscando la cita seleccionada", todos);

     
      document.getElementById("paciente").value = todos[0].paciente;
      //document.getElementById("Doctor_cita").textContent = todos[0].medico;

      document.getElementById("Fecha_cita").value = todos[0].fecha;
      document.getElementById("hora_cita").value = todos[0].hora;
     // document.getElementById("ubicacion").textContent = todos[0].ubicacion;
     // document.getElementById("salas").textContent = todos[0].salas;


      // const Selectsalas = document.getElementById("salas");
      // const option = document.createElement("option");
      // option.value =todos[0].salas;
      // option.textContent = todos[0].salas;
      // Selectsalas.appendChild(option);

      //  const Selectubicacion = document.getElementById("ubicacion");
      //  const option_ubicacion = document.createElement("option");
      //  option_ubicacion.value =todos[0].ubicacion;
      //  option_ubicacion.textContent = todos[0].ubicacion;
      //  Selectubicacion.appendChild(option_ubicacion);


      //  const Selectmedico = document.getElementById("Doctor_cita");
      //  const option_medico = document.createElement("option");
      //  option_medico.id =todos[0].medico;
      //  option_medico.textContent = todos[0].medico;
      //  Selectmedico.appendChild(option_medico);



      try {
        //    const v_edit_Doctor_cita = document.getElementById("Doctor_cita");
        // v_edit_Doctor_cita.removeAttribute("");
        //v_edit_Doctor_cita.focus();
        const response = await fetch("http://127.0.0.1:8000/getmedico");
        if (!response.ok) throw new Error("Error al cargar los datos");
        const data = await response.json();
        medico = data.resultado;

        const Selectdoctor = document.getElementById("Doctor_cita");
        for (let i = 0; i < data.resultado.length; i++) {
  
          const user = data.resultado[i];   
          const option = document.createElement("option");
          option.value = user.id;

          option.textContent = user.nombre;
          Selectdoctor.appendChild(option);      
          
        }
        console.log("todos")
        console.log(todos)

        Selectdoctor.value=todos[0].id_usuario;

        console.log(Selectdoctor);
        
        
        //-----------------------------aca va el codigo para node----------------------------------------------------------------------------------

        const response_node = await fetch("https://api-nodejs-buxf.onrender.com/api/hospitales/gethospitales");
        const data_node= await response_node.json()
        console.log(data_node)//ubicacion
        let todos_node= data_node.data
        console.log("esto es data de node", todos_node)

        const Select_hospitales = document.getElementById("ubicacion");

        for (let i = 0; i < todos_node.length; i++) {
  
          const hospital = todos_node[i];   
          const option = document.createElement("option");
          option.value = hospital.nombre_hospital;

          option.textContent = hospital.nombre_hospital;
          Select_hospitales.appendChild(option);      
          
        }
        Select_hospitales.value=todos[0].ubicacion

        console.log(Select_hospitales);  

        mostrar_salas(todos[0].salas)

      } catch (e) {
        error = e.message;
      } finally {
        loading = false;
      }
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }

  async function actualizar() {
    let vfecha_cita = document.getElementById("Fecha_cita").value;
    let vhora_cita = document.getElementById("hora_cita").value;
    let vdoctor = document.getElementById("Doctor_cita").value;
    let v_ubicacion= document.getElementById("ubicacion").value;
    let v_salas= document.getElementById("salas").value;

    console.log("la id que esta aca en la fn actualzar es"+vid)
    console.log("la id que esta aca en la fn actualzar es"+vhora_cita)
    console.log("la ubicacion es"+v_ubicacion)


    try {

      const response = await fetch("http://127.0.0.1:8000/update_cita", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          fecha: vfecha_cita,
          hora: vhora_cita,
          id_usuario: vdoctor,
          id: vid,
          ubicacion: v_ubicacion,
          salas: v_salas,

        }),
      });
      console.log("Actualizado");

      const Toast = Swal.mixin({
          toast: true,
          position: "top-end",
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
          iconColor: "white",
          color: "white",
          background: "#00bdff",
          title: "cita actualizada con exito",
        });
     
        setTimeout(() => {
          const v_editar = document.getElementById("nav-listado");
          v_editar.setAttribute("class", "fade");

          let ocultar = document.getElementById("Mostrarcitas");
          ocultar.removeAttribute("class");
          const cambiar = v_editar.parentElement;
          cambiar.insertBefore(ocultar, v_editar);
          location.reload();
          }, 3000);

    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }
  function Confirmar_eliminar(id){
    Swal.fire({
                title: "De verdad quieres eliminar esta cita?",
                text: "Esto no se puede deshacer",
                icon: "question",
                showCancelButton: true,
                confirmButtonColor: "#3085d6",
                cancelButtonColor: "#d33",
                confirmButtonText: "Si, cancelar cita",
            }).then((result) => {
                if (result.isConfirmed) {
                    Eliminar(id)
                }
            });
  }


  async function Eliminar(id){
    vid = id;   
    console.log("entra al eliminar de la cita numero "+vid)
    try {
    const response = await fetch("http://127.0.0.1:8000/eliminar_cita", {
      method: "PUT",
      headers: {
        "Content-Type": "application/json", // Asegúrate de especificar que envías JSON
      },
      body: JSON.stringify({
         id: vid 
        }), 
    }); const Toast = Swal.mixin({
          toast: true,
          position: "top-end",
          showConfirmButton: false,
          timer: 3000,
          timerProgressBar: true,
          didOpen: (toast) => {
            toast.onmouseenter = Swal.stopTimer;
            toast.onmouseleave = Swal.resumeTimer;
          },
        });
        Toast.fire({
          icon: "error",
          iconColor: "white",
          color: "white",
          background: "#e70202",
          title: "cita eliminada con exito",
        });
        
        setTimeout(() => {
          location.reload();
          }, 3000);
          
    console.log("entra aca")
      } catch (e) {
          error = e.message;
          console.log(error)
      }finally {
          loading = false;
      }
  }
  

  async function mostrar_salas(t_salas) {
    console.log("salas", t_salas)
    
    let v_id_hospital= document.getElementById("ubicacion").value;
    console.log("la id del hospital seleccionado fue: ",v_id_hospital)//ALT 96= ``
  
    const response_node = await fetch(`https://api-nodejs-buxf.onrender.com/api/salas/getsalaByNombre/${v_id_hospital}`);
    // Selectsalas.innerHTML = "<option selected>Seleccione una sala</option>";
    if (!response_node.ok) throw new Error("Error al cargar los datos");
                 const data_node = await response_node.json();
                 console.log(data_node)
                 let  todos_node=data_node.data
                console.log("esto es data de node", data_node)

                console.log("esto es node MOSTRAR SALAS ", todos_node)
                console.log(todos_node)
                console.log(todos_node.length)

            const Selectsalas = document.getElementById("salas");
            
            Selectsalas.innerHTML = "<option selected>Seleccione una sala</option>";
                for (let i = 0; i < todos_node.length; i++) {

                    const user = todos_node[i];
                    const option = document.createElement("option");
                    option.value = user.salas_nombre;

                    option.textContent = user.salas_nombre; 
                    Selectsalas.appendChild(option);
                    
                }
                Selectsalas.value=t_salas

  }

</script>

<Navbaradmin></Navbaradmin>
<div id="Mostrarcitas">
  <div class="container py-4">
    <h2 class="mb-4">Citas agendadas</h2>
    {#if loading}
      <div class="row g-2 justify-content-center">
        <p class="text-center col-lg-2 col-md-2 col-sm-2 col-12 col-xl-2">
          Cargando datos...
        </p>
        <div
          class="spinner-border col-lg-4 col-md-4 col-sm-4 col-12 col-xl-4"
          role="status"
        >
          <span class="visually-hidden">Loading...</span>
        </div>
      </div>
    {:else if error}
      <p class="text-red-500">Error: {error}</p>
    {:else}
      <div class="overflow-x-auto">
        <table class="min-w-full bg-white border border-gray-300" id="myTable">
          <thead>
            <tr>
              <th class="px-4 py-2 border">Paciente</th>
              <th class="px-4 py-2 border">Doctor</th>
              <th class="px-4 py-2 border">Fecha</th>
              <th class="px-4 py-2 border">Hora</th>
              <th class="px-4 py-2 border">Hospital</th>
              <th class="px-4 py-2 border">Ubicacion</th>

              <th class="px-4 py-2 border">Opcion</th>
            </tr>
          </thead>

          <tbody>
            {#each todos as todo}
              <tr class="hover:bg-gray-50">
                <td class="px-4 py-2 border">{todo.paciente}</td>
                <td class="px-4 py-2 border">{todo.medico}</td>
                <td class="px-4 py-2 border">{todo.fecha}</td>
                <td class="px-4 py-2 border">{todo.hora}</td>
                <td class="px-4 py-2 border">{todo.ubicacion}</td>
                <td class="px-4 py-2 border">{todo.salas}</td>

                <td class="px-4 py-2 border">
                  <button class="btn btn-info" on:click={() => editar(todo.id)}
                    >Editar</button
                  >
                  <button class="btn btn-danger" on:click={() => Confirmar_eliminar(todo.id)}
                    >Cancelar</button
                  >
                </td>
              </tr>
            {/each}
          </tbody>
        </table>
      </div>
    {/if}
  </div>
</div>

<div
  class="fade"
  id="nav-listado"
  role="tabpanel"
  aria-labelledby="nav-listado-tab"
  >
  <div class="container text-center">
    <p class="text-orange"></p>
  </div>
  <div class="card border-dark shadow" style="width: 60%; margin-left: 20%;">
    <div class="card-header row g-2">
      <h5 class="card-title col-lg-11"><b>Editando cita</b></h5>
      <button class="btn btn-close col-lg-1" on:click={() => Ocultar()}
        aria-label="Cerrar edición de usuario"></button>
    </div>
    <div class="card-body" style="margin-left: 10%;">
      <div class="row">
        <div class="col-lg-2">
          <p class="card-text"><b>Paciente:</b></p>
        </div>
        <div class="col-lg-10">
          <input
            type="text"
            placeholder="Nombres"
            id="paciente"
            maxlength="100"
            style="border: none; width: 55%;"
            
          />
        </div>
      </div>

      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Doctor:</b></p>
        </div>

        <div class="col-lg-10">
          <select class="form-select" id="Doctor_cita" style=" width: 55%;" required>
            <option selected>Seleccione</option>
          </select>
        </div>
      </div>

      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Fecha:</b></p>
        </div>
        <div class="col-lg-10">
          <input class="form-control"
            type="date"
            id="Fecha_cita"
            placeholder="Fecha de la cita"
            style="width: 55%;"
            
          />
        </div>
      </div>

      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Hora:</b></p>
        </div>
        <div class="col-lg-10">
          <input class="form-control"
            type="time"
            id="hora_cita"
            placeholder="hora de la cita"
            maxlength="20"
            style="width: 55%;"
            
          />
        </div>
      </div>


      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Ubicacion:</b></p>
        </div>
        <div class="col-lg-10">
         <select name="opciones" id="ubicacion" class="form-select" style="width: 55%;" on:change={mostrar_salas}>
          <option selected>Seleccione</option>
         </select>
        </div>
      </div>


      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Sala:</b></p>
        </div>
        <div class="col-lg-10">
         <select name="opciones" id="salas" class="form-select" style="width: 55%;">
          <option selected >Seleccione</option>
          
         </select> 
        </div>
      </div>




      <div class="row" style="margin-top: 4%;">
        <div class="col-lg-9">
          ¡Al terminar de editar, darle click en actualizar para guardar los
          cambios!
        </div>
        <div class="col-lg-3 text-end">
          <button on:click={actualizar} class="btn btn-outline-info"
            ><b>Actualizar</b></button
          >
        </div>
        <div id="estado" class="col-lg-10"></div>
      </div>
    </div>
  </div>
</div>
