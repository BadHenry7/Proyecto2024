<script>
  import { onMount } from "svelte";
  import Navbaradmin from "$lib/Navbaradmin.svelte";
    
  let loading = true;
  let error = null;
  let todos={}
  let t_roles={}
  var todos_modulos={}
  let seleccionados = [];
 
  let todos_info={}
  let todos_mxp={}
  let rol_v=0


  onMount(async () => {
    try {
      const response = await fetch("http://127.0.0.1:8000/get_modulos");
      const response_roles = await fetch("http://127.0.0.1:8000/get_roles");

      if (!response.ok) throw new Error("Error al cargar los datos");
     const data = await response.json();
     const data_roles = await response_roles.json()

     todos_modulos=data.resultado
     t_roles=data_roles.resultado


      console.log("revisando el modulo", todos_modulos)
      console.log("revisando el t_roles", t_roles)
      console.log("revisando el t_roles", t_roles.length)

      setTimeout(() => {
        globalThis.$("#myTable").DataTable({
          stripeClasses: ["bg-white", "bg-light"], 
          language: {
            url: "//cdn.datatables.net/plug-ins/1.13.4/i18n/es-ES.json",}
        }); // Para convertrlo en datatable :D
      }, 0);

    } catch (e) {
      alert("s")
      error = e.message;
      
    } finally {
      loading = false;
    }
  });


  async function create_rol() {
    console.log("Seleccionado", seleccionados)
    let v_nombre=document.getElementById('name_m').value;//name modulo
    let v_descripcion=document.getElementById('descripcion').value;
   
    console.log("Nombre del rol:", v_nombre)
    console.log("Descripcion", v_descripcion)

    try {
      console.log("sssssss");

      const response = await fetch("http://127.0.0.1:8000/create_rol",{

        method: "POST",
        headers: {
          "Content-Type": "application/json", },
        body: JSON.stringify({
          nombre:v_nombre,
          descripcion: v_descripcion,
          estado:1,
        }),
                        
      });
 
     const data = await response.json();
     todos= data
     let v_id=todos[0];


      create_mxperfil(v_id)

    } catch (e) {
      error = e.message;
      console.log(error)

      
    } finally {
      loading = false;
    }


    

  }

  async function modulos_asignados(v_id_rol) {
    let miStorage = window.localStorage;
      let usuario = JSON.parse(miStorage.getItem('usuario'));
      let v_id_u=usuario.id



    console.log("Entramos al try de modulos asignados")
    try {
      const response = await fetch("http://127.0.0.1:8000/get_modulos_asignado",{
      method: "POST",
      headers: {
        "Content-Type": "application/json", },
        body: JSON.stringify({
        id:v_id_rol,
      }), 
    });
    const data = await response.json();
    todos=data.resultado
   
    todos_info=data.resultado[0]


    console.log("variables ", todos_info )
    document.getElementById("nambre").value = todos_info.nombre;
    document.getElementById("descrition").value = todos_info.descripcion;
    document.getElementById("etado").value = todos_info.estado_rol;
    


    //arriba guardo la informacion que tiene el rol a editar, abajo, buscara que modulos
    //asignado tiene esa id_rol:
    console.log("-----------")
    console.log("-----------",v_id_rol)
    console.log("-----------",v_id_u)



    const result = await fetch("http://127.0.0.1:8000/get_mxp_id",{
      method: "POST",
      headers: {
        "Content-Type": "application/json", },
        body: JSON.stringify({
        id_rol:v_id_rol,
      }), 
    });
    const data_mxp = await result.json();
    todos_mxp=data_mxp.resultado
    console.log("revisando esta consulta mxp",todos_mxp)
    seleccionados=[]
    for (let i = 0; i < todos_mxp.length; i++) {
    
        if (todos_mxp[i].estado==1){
          seleccionados.push(todos_mxp[i].id_modulo)

        }


    }
    console.log(seleccionados)

    } catch (e) {
      
      error = e.message;
      console.log(error)
    } finally {
      loading = false;
      

    }
    
    
    

  }


//guardar la tabla del modulo por perfil
  async function create_mxperfil(v_id_rol) {
    try {

      console.log("id del rol que fue creado:",v_id_rol)
      console.log("modulos seleccionados",seleccionados)

      const response = await fetch("http://127.0.0.1:8000/create_moduloxperfil",{

        method: "POST",
        headers: {
          "Content-Type": "application/json", },
        body: JSON.stringify({
          id_rol:v_id_rol,
          id_modulo: seleccionados,
          estado:1, 
        }), 
      });

      
     const data = await response.json();
      todos=data.resultado
     

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
        background: "green",
        title: "rol creado con exito",
      });

      setTimeout(() => {
        location.reload();
      }, 3000);



    } catch (e) {
      alert("s")
      error = e.message;
      
    } finally {
      loading = false;
    }
  }
  //let cont=0


  async function update_rol(v_id_rol) {
    try{

      let put_nombre=document.getElementById('nambre').value;
      let put_descripcion=document.getElementById('descrition').value;
      let v_estado=document.getElementById('etado').value;
      console.log(v_id_rol)
      console.log(seleccionados)

      
      const response = await fetch ('http://127.0.0.1:8000/update_modulo_seleccionado',{

      method: 'PUT',
      headers:{ "Content-Type": "application/json",},
      body: JSON.stringify({
          id: v_id_rol,
          nombre:put_nombre,
          descripcion: put_descripcion,
          estado:v_estado,
          modulo_seleccionado: seleccionados,
         
        }),

      })

      
 
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
        title: "rol actualizado con exito",
      });

      setTimeout(() => {
        location.reload();
      }, 3000);

    }catch(e){
      error=e.message
      console.log(error)
    }


  }
let loading_estado=true

  async function cam_estado() {
                
                  let v_etado= document.getElementById('etado').value;
                  console.log("es v_etado", v_etado)

                  if (v_etado!=0){

                    loading_estado=true
                  }else{
                    loading_estado=false
                  }

                }

                //no tocar, ya vuelvo afk
  
</script>

<Navbaradmin></Navbaradmin>


<!--Creacion de roles-->


<div class="card-body container"> 
  <div class="container text-center"><b class="fs-4">¡Creacion de roles!</b></div>

  <div class="row">
    <div class="col-xl-6">
      <label for="" >Nombre del rol</label>
      <input type="text" id="name_m" class="form-control" />
    </div>
    <div class="col-xl-6">
      <label for="" >Descripcion</label>
      <input type="text" id="descripcion" class="form-control" />
    </div>
  </div>

  <div class="row mt-1">
    <div class="col-xl-12">
      <button class="btn"  data-bs-toggle="modal" data-bs-target="#RModal2">
      <i class="fas fa-plus-square fa-2x " style="color: green;"></i><span class="mx-2 fs-5">Añadir modulo</span>
      </button>
      
    </div>
  </div>
</div>


<!--Asignacion de modulo de roles-->
<div class="modal fade" id="RModal2" tabindex="-1" aria-labelledby="rModalLabel" aria-hidden="true">
  <div class="modal-dialog">
      <div class="modal-content">
          <div class="modal-header">
              <button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
              ></button>
          </div>
          <div class="modal-body">
              <h3>Seleccione los modulos que tendran el rol</h3>

              
            {#if loading}
              <p class="text-center">Cargando...</p>
            {:else if error != null}
              <p class="text-red-500">Error: {error}</p>
            {:else if todos_modulos.length > 0}
              {#each todos_modulos as todo}
                <label>
                  <input type="checkbox" value={todo.id} bind:group={seleccionados}>
                  {todo.submodelos}
                </label>
                <br>
              {/each}
            {:else}
              <p class="text-center">No hay datos</p>
            {/if}
              
          </div>

          <div class="card-footer">
            <button class="btn btn-info" on:click={create_rol}>Agregar</button>
          </div>
      </div>
  </div>
</div>



<!--Mostrar los roles
<div class="container">
  <div class="card-header text-center "  >Roles creados</div>
  <div class="row">
    {#each t_roles as rol, i}
      <div class="col-sm-6">
        <div class="card">
          <div class="card-body">
            <h5 class="card-title">{rol.nombre}</h5>
            <p class="card-text">{rol.descripcion}</p>
            <p class="card-text"><b>Estado:</b><span class={rol.estado? "text-success":"text-danger"}> {rol.estado ? "Activo" : "Desactivo"}</span></p>
            
            {#if rol.id!=1 && rol.id!=2 && rol.id!=3}
            <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#RModaledit" on:click={()=>modulos_asignados(rol.id)}>Editar</button>
            {:else}
            <p>Rol exclusivo, no es posible editar</p>

            {/if}


          </div>
        </div>
      </div>
  
      {#if (i + 1) % 2 === 0 }//1%2=1   2%2=0   3%2=1   4%2=0
      <div class="pt-2"> 
      </div> 
        {/if}
    {/each}
  </div>
</div>

-->

<div id="Mostrarroles">
  <div class="container">
    
    
    
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
              <th class="py-2 border">Nombre</th>
              <th class="py-2 border">descripcion</th>
              <th class="py-2 border">Estado</th>
              <th class="py-2 border">Opcion</th>
            </tr>
          </thead>

          <tbody>
            {#each t_roles as rol}
              <tr class="hover:bg-gray-50">
                <td class="py-2 border">{rol.nombre}</td>
                <td class="py-2 border">{rol.descripcion}</td>

                <td class="py-2 border">
                  <span class={rol.estado ? "text-green-600" : "text-red-600"}>
                    {rol.estado ? "Activo" : "Desactivado"}
                  </span>
                </td>
                <td class=" py-2 border text-center">
                {#if rol.id!=1 && rol.id!=2 && rol.id!=3}
                  <button aria-label="editar" class="btn btn-info" data-bs-toggle="modal" data-bs-target="#RModaledit" on:click={()=>modulos_asignados(rol.id)}>
                     <i class="bi bi-pencil-square"></i> Editar</button
                  >
                {:else}
                <button aria-label="editar" class="btn btn-info" data-bs-toggle="modal" data-bs-target="#RModalver" on:click={()=>rol_v=rol.id}>
                  <i class="bi bi-eye"></i> Ver</button>

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


<!--Editar roles-->
<div class="modal fade" id="RModaledit" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog ">
      <div class="modal-content">
          <div class="modal-header">
              <button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
              ></button>
          </div>
          <div class="modal-body">
            <div class="col-lx-4">
              <label for="">Nombre:</label>
              <input type="text" id="nambre"  class="form-control">
            </div>

            <div class="col-lx-4">
              <label for="">Descripcion:</label>
              <input type="text" id="descrition"   class="form-control">
            </div>

            <div class="col-lx-4 mt-1">
              
              <label for="">Estado:</label><!--Cam es cambiar-->
              <select id="etado" name="opciones" on:change={cam_estado}  style="border: none; width: 55%;" class="form-control">
                <option value="1">Activar</option>
                <option value="0">Desactivar</option>
              </select>
            </div>
            {#if loading_estado!=0}
            <div>
                    <label for="">Modulos:
                    </label>
                    <br>
                    {#each todos_modulos as todo}
                  
                    <label>
                      <input type="checkbox" value={todo.id} checked bind:group={seleccionados}><!--Galesxedkdeas-->
                      {todo.submodelos}
                    </label>
                    <br>
                    

                  {/each}
            </div>
            {/if}
          </div>
       
          <div class="card-footer">
            <button class="btn btn-info" on:click={()=>update_rol(todos_info.id_rol)}>Actualizar</button>
          </div>
      </div>
  </div>
</div>

<!--Mostrar roles exclusivo-->
<div class="modal fade" id="RModalver" data-bs-backdrop="static" data-bs-keyboard="false" tabindex="-1" aria-labelledby="staticBackdropLabel" aria-hidden="true">
  <div class="modal-dialog ">
      <div class="modal-content">
          <div class="modal-header">
              <button
                  type="button"
                  class="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
              ></button>
          </div>
          <div class="modal-body">
            {#if rol_v == 1}
        <p>Rol exclusivo del superadministrador</p>
        <p>Acceso total al sistema.</p>
        <ul>
          <li>Gestion de usuario</li>
          <li>Gestion de medico</li>
          <li>Gestion de roles</li>
          <li>Gestion de citas</li>
          <li>Realizar Reportes</li>
          <li>ver tablero</li>
        </ul>
            {:else if rol_v==2}
            <p>Rol exclusivo del paciente</p>
            <p>Podra realizar: </p>

            <ul>
              <li>Citas medicas</li>
              <li>Reportes</li>
              <li>Certificados</li>
              <li>Ver su perfil</li>
            </ul>
            {:else if rol_v==3}
            <p>Rol exclusivo del doctor</p>
            <p>Podra realizar: </p>

            <ul>
              <li>Ver citas</li>
              <li>Historial clinico</li>
              <li>Reportes</li>
              <li>Usar la red neuronal como apoyo para la deteccion de enfermedades basicas</li>
            </ul>
            {/if}
          </div>
       
      </div>
  </div>
</div>



<!--#f0ecec-->

