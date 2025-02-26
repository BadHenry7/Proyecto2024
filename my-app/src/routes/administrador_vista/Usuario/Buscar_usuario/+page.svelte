<script>
  import Navbaradmin from "../../../../lib/Navbaradmin.svelte";
  import { onMount } from "svelte";

  let todos = {};
  let loading = true;
  let error = null;

  onMount(async () => {
    try {
      console.log("2");
      const response = await fetch("http://127.0.0.1:8000/get_users");
      if (!response.ok) throw new Error("Error al cargar los datos");
      const data = await response.json();
      todos = data.resultado;
      console.log(todos);
      console.log(todos.usuario);

      setTimeout(() => {
        globalThis.$("#myTable").DataTable({
          stripeClasses: ["bg-white", "bg-light"], 
          language: {
            url: "//cdn.datatables.net/plug-ins/1.13.4/i18n/es-ES.json",}
        }); // Para convertrlo en datatable :D
      }, 0);
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  });
  var id = 1;

  var a = "";

  async function Ocultar() {
    const v_editar = document.getElementById("nav-listado");
    v_editar.setAttribute("class", "fade");

    let mostrar = document.getElementById("Mostrarusuario");
    mostrar.removeAttribute("class");

    location.reload();
  }

  var vid = 1;
  async function editar(id, a) {
    console.log("Editando a " + a);
    //
    const v_editar = document.getElementById("nav-listado");
    v_editar.removeAttribute("class");
    console.log(v_editar);
    vid = id;
    console.log(Number.isInteger(vid));

    console.log(vid);
    let ocultar = document.getElementById("Mostrarusuario");
    ocultar.setAttribute("class", "fade");
    console.log(ocultar);

    const cambiar = ocultar.parentElement;
    console.log(cambiar);

    cambiar.insertBefore(v_editar, ocultar);
    console.log("NO Entra al try de buscar");

    try {
      console.log("Entra al try de buscar");

      const response = await fetch("http://127.0.0.1:8000/get_user", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id: vid,
        }),
      });
      const data = await response.json();
      console.log(data);
      console.log("Buscando al usuario seleccionado");

      document.getElementById("nombres").value = data.nombre;
      document.getElementById("apellidos").value = data.apellido;
      document.getElementById("documento").value = data.documento;
      document.getElementById("telefono").value = data.telefono;
      document.getElementById("correo").value = data.usuario;
      const estado_v = data.estado ? "1" : "0";//condicion ? valorSiVerdadero : valorSiFalso
      document.getElementById("estado").value = estado_v;
      
      console.log("el nombre es ",data.roles_name)
      console.log("el id del rol es ",data.id_rol)
      
      //document.getElementById("roles").value = data.roles_name;

      const selectRol = document.getElementById("roles");
      selectRol.innerHTML = "";

      const defaultOption = document.createElement("option");
      defaultOption.value = data.id_rol;
      defaultOption.textContent = data.roles_name;
      defaultOption.selected = true;
      selectRol.appendChild(defaultOption);


      const roless = await fetch ("http://127.0.0.1:8000/roles_get",{
        method:"GET",
        headers: { "Content-Type": "application/json" },
      });
      const dataroles = await roless.json();
      console.log(dataroles);
      console.log("Roles obtenidos:", dataroles);
      
      for (let i = 0; i < dataroles.resultado.length; i++) {
            const rol = dataroles.resultado[i];

            if (rol.id !== data.id_rol) {  
                const option = document.createElement("option");
                option.value = rol.id;
                option.textContent = rol.nombre;
                selectRol.appendChild(option);
            }
        }

      selectRol.value = data.id_rol;

      const v_edit_nombre = document.getElementById("nombres");
      v_edit_nombre.removeAttribute("readonly");
      v_edit_nombre.focus();

      const v_edit_apellido = document.getElementById("apellidos");
      v_edit_apellido.removeAttribute("readonly");

      const v_edit_documento = document.getElementById("documento");
      v_edit_documento.removeAttribute("readonly");

      const v_edit_telefono = document.getElementById("telefono");
      v_edit_telefono.removeAttribute("readonly");

      const v_edit_usuario = document.getElementById("correo");
      v_edit_usuario.removeAttribute("readonly");

      const v_edit_estado = document.getElementById("estado");
      v_edit_estado.removeAttribute("readonly");

    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }

  async function actualizar() {
    console.log(vid);
    let vnombre = document.getElementById("nombres").value;
    let vapellidos = document.getElementById("apellidos").value;
    let vdocumento = document.getElementById("documento").value;
    let vtelefono = document.getElementById("telefono").value;
    let vcorreo = document.getElementById("correo").value;
    let vrol = document.getElementById('roles').value;
    let vestado = document.getElementById("estado").value;

    console.log("IDE DE vrol ENVADO A LA BASE DE DATOS ES " + vrol);
    

    try {
      console.log("Entra al try de actualzar");

      const response = await fetch("http://127.0.0.1:8000/actualizaruser", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id: vid,
          usuario: vcorreo,
          nombre: vnombre,
          apellido: vapellidos,
          documento: vdocumento,
          telefono: vtelefono,
          id_rol: vrol,
          estado: vestado,
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
        title: "usuario actualizado con exito",
      });

      setTimeout(() => {
        location.reload();
      }, 3000);
    } catch (e) {
      error = e.message;
    } finally {
      loading = false;
    }
  }

  const serviceID = "service_acpug5r";
  const templateID = "template_bloqueouser";
  const apikey = "3bmpPn1S0SLhgotWj";

  async function desactivar(id, nombre, usuario) {
    let vestado = 0;
    let vid = id;
    console.log("Correo" + usuario);
    try {
      const response = await fetch("http://127.0.0.1:8000/estado_user", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id: vid,
          estado: vestado,
        }),
      });

      const data = await response.json();
      if (response.ok) {
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
          icon: "error",
          iconColor: "white",
          color: "white",
          background: "#ff4e4e",
          title: "usuario desactivado con exito",
        });
        //sendEmail()

        function sendEmail() {
          emailjs.init(apikey);
          emailjs
            .send(serviceID, templateID, {
              nombre: nombre,
              email: usuario,
            })
            .then((result) => {
              console.log("Corro enviado con exito");
            })
            .catch((error) => {
              console.log("Error al enviar el correo:", error.text);
            });
        }

        setTimeout(() => {
          location.reload();
        }, 3500);
      } else {
        alert("Error al desactivar: " + data.message || "Error desconocido");
      }
    } catch (e) {
      alert("Error en la solicitud: " + e.message);
    }
  }

  async function activar(id, nombre) {
    let vestado = 1;
    let vid = id;

    try {
      const response = await fetch("http://127.0.0.1:8000/estado_user", {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id: vid,
          estado: vestado,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        console.log(`Usuario ${nombre} Activado`);
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
          iconColor: "#000000",
          color: "black",
          background: "#76fa78",
          title: "usuario activado con exito",
        });

        setTimeout(() => {
          location.reload();
        }, 3500); //en milisegundos
      } else {
        alert("Error al Activar: " + data.message || "Error desconocido");
      }
    } catch (e) {
      alert("Error en la solicitud: " + e.message);
    }
  }
</script>

<Navbaradmin></Navbaradmin>

<div id="Mostrarusuario">
  <div class="container py-4">
    <h2 class="mb-4 text-center"><b>¡Lista de usuarios!</b></h2>
    <hr>  
    {#if loading}
      <!---->
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
            <tr class="bg-primary text-white">
              <th class="px-4 py-2 border">Usuario</th>
              <th class="px-4 py-2 border">Nombre</th>
              <th class="px-4 py-2 border">Apellido</th>
              <th class="px-4 py-2 border">Documento</th>
              <th class="px-4 py-2 border">Telefono</th>
              <th class="px-4 py-2 border">Rol</th>
              <th class="px-4 py-2 border">Estado</th>
              <th class="px-4 py-2 border">Opciones</th>
            </tr>
          </thead>

          <tbody>
            {#each todos as todo}
              <tr class="hover:bg-gray-50">
                <td class="py-2 border">{todo.usuario}</td>
                <td class="py-2 border">{todo.nombre}</td>
                <td class="py-2 border">{todo.apellido}</td>
                <td class="py-2 border">{todo.documento}</td>
                <td class="py-2 border">{todo.telefono}</td>
                <td class="py-2 border">{todo.nombre_rol}</td>

                <td class="py-2 border">
                  <span class={todo.estado ? "text-green-600" : "text-red-600"}>
                    {todo.estado ? "Activo" : "Desactivado"}
                  </span>
                </td>
                <td class=" py-2 border">
                  <button aria-label="editar"
                    class="btn btn-info"
                    on:click={() => editar(todo.id, todo.nombre)}> <i class="bi bi-pencil-square"></i></button
                  >
                  {#if todo.estado}
                    <!-- Mostrar botón "Desactivar" si el usuario está activo -->
                    <button aria-label="desactivar"
                      class="btn btn-danger"
                      on:click={() =>
                        desactivar(todo.id, todo.nombre, todo.usuario)}
                    >
                    <i class="bi bi-toggle-off"></i>
                    </button>
                  {:else}
                    <!-- Mostrar botón "Activar" si el usuario está desactivado -->
                    <button aria-label="activar"
                      class="btn btn-success"
                      on:click={() => activar(todo.id, todo.nombre)}
                    >
                    <i class="bi bi-toggle-on"></i>
                    </button>
                  {/if}
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
      <button class="btn btn-close col-lg-1"  aria-label="Cerrar edición de usuario" on:click={() => Ocultar()}
      ></button>
    </div>
    <div class="card-body" style="margin-left: 10%;">
      <div class="row">
        <div class="col-lg-2">
          <p class="card-text"><b>Nombre:</b></p>
        </div>

        <div class="col-lg-10">
          <input
            type="text"
            placeholder="Nombres"
            id="nombres"
            maxlength="100"
            style="border: none; width: 55%;"
            
          />
        </div>
      </div>

      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Apellido:</b></p>
        </div>

        <div class="col-lg-10">
          <input
            type="text"
            placeholder="Apellidos"
            id="apellidos"
            style="border: none; width: 55%;"
            
          />
        </div>
      </div>

      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>documento:</b></p>
        </div>
        <div class="col-lg-10">
          <input
            type="text"
            id="documento"
            placeholder="Documento de identidad"
            style="border: none; width: 55%;"
            
          />
        </div>
      </div>

      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Telefono:</b></p>
        </div>
        <div class="col-lg-10">
          <input
            type="text"
            id="telefono"
            placeholder="Telefono"
            maxlength="20"
            style="border: none; width: 55%;"
            
          />
        </div>
      </div>

      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Correo:</b></p>
        </div>
        <div class="col-lg-10">
          <input
            type="text"
            placeholder="Correo electronico"
            id="correo"
            style="border: none; width: 55%;"
            
          />
        </div>
      </div>
      
      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Rol:</b></p>
        </div>
        <div class="col-lg-10">
          <select id="roles" required style="border: none; width: 55%;">
            <option value="" selected>Seleccione</option>
        </select>
        </div>
      </div>

      <div class="row pt-3">
        <div class="col-lg-2">
          <p class="card-text"><b>Estado:</b></p>
        </div>
        <div class="col-lg-10">
          <select id="estado" name="opciones" style="border: none; width: 55%;">
            <option value="1">Activar</option>
            <option value="0">Desactivar</option>
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



