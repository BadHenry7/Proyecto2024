<script>
  import Navbaradmin from "../../../../lib/Navbaradmin.svelte";
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
    console.log(v_editar);
    vid = id;
    console.log(Number.isInteger(vid));

    console.log(vid);
    let ocultar = document.getElementById("Mostrarcitas");
    ocultar.setAttribute("class", "fade");
    console.log(ocultar);

    const cambiar = ocultar.parentElement;
    console.log(cambiar);

    cambiar.insertBefore(v_editar, ocultar);
    console.log("NO Entra al try de buscar");

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
      console.log(data);
      console.log("_____________________");
      /*   
                    'fecha':data[0],
                    'hora':str(data[1]),
                    'medico':data[2],
                    'paciente':data[3],
                    'id':data[4]
*/
      todos = data.resultado;
      console.log(todos[0].paciente);
      console.log(todos[0].hora);
      console.log("Buscando la cita seleccionada");

     
      document.getElementById("paciente").value = todos[0].paciente;
      document.getElementById("Fecha_cita").value = todos[0].fecha;
      document.getElementById("hora_cita").value = todos[0].hora;

      const v_edit_Fecha_cita = document.getElementById("Fecha_cita");
      v_edit_Fecha_cita.removeAttribute("readonly");

      const v_edit_hora_cita = document.getElementById("hora_cita");
      v_edit_hora_cita.removeAttribute("readonly");

      try {
        console.log("entra al try de /getmedico");

        //    const v_edit_Doctor_cita = document.getElementById("Doctor_cita");
        // v_edit_Doctor_cita.removeAttribute("readonly");
        //v_edit_Doctor_cita.focus();
        const response = await fetch("http://127.0.0.1:8000/getmedico");
        if (!response.ok) throw new Error("Error al cargar los datos");
        const data = await response.json();
        medico = data.resultado;
        
        console.log(medico);
        console.log("todos.usuario");

        const Selectdoctor = document.getElementById("Doctor_cita");
        for (let i = 0; i < data.resultado.length; i++) {
          console.log("entra al for de /getmedico ")
          console.log(data.resultado.length)
          const user = data.resultado[i];
          console.log(data.resultado[i])      
          
          const option = document.createElement("option");
          option.value = user.id;

          option.textContent = user.nombre;
          Selectdoctor.appendChild(option);      
          
        }
        console.log(Selectdoctor);
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

  function actualizar() {

  }

  function Eliminar(){
    
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
                <td class="px-4 py-2 border">
                  <button class="btn btn-info" on:click={() => editar(todo.id)}
                    >Editar</button
                  >
                  <button class="btn btn-danger" on:click={() => Eliminar()}
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
      <h5 class="card-title col-lg-11"><b>Editando Usuario</b></h5>
      <button class="btn btn-close col-lg-1" on:click={() => Ocultar()}
      ></button>
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
            readonly
          />
        </div>
      </div>

      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Doctor:</b></p>
        </div>

        <div class="col-lg-10">
          <select class="form-select" id="Doctor_cita" required>
            <option selected>Seleccione</option>
          </select>
        </div>
      </div>

      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Fecha:</b></p>
        </div>
        <div class="col-lg-10">
          <input
            type="date"
            id="Fecha_cita"
            placeholder="Fecha de la cita"
            style="border: none; width: 55%;"
            readonly
          />
        </div>
      </div>

      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Hora:</b></p>
        </div>
        <div class="col-lg-10">
          <input
            type="time"
            id="hora_cita"
            placeholder="hora de la cita"
            maxlength="20"
            style="border: none; width: 55%;"
            readonly
          />
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
