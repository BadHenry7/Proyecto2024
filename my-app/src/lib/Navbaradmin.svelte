<script>

import { onMount } from "svelte";
import {token_obtener} from "$lib"

let modal_perfil;

let todos = {};
let error = null;
var v_id=1
var henry=true


onMount(async() => {

  let cookies = document.cookie
        .split("; ")
        .find(row => row.startsWith("sesionGoogle="));

    if (cookies) {
        let sesionGoogleRaw = cookies.split("=")[1];
        let sesionGoogle = JSON.parse(decodeURIComponent(sesionGoogleRaw));
        console.log("Sesión decodificada:", sesionGoogle);
        let miStorage = window.localStorage;
        let name = sesionGoogle.nombre;
        let id = sesionGoogle.id;
        let correo = sesionGoogle.email;
        let todos2=await token_obtener(correo, "v_password", token_v, "true");
        let encontrado = { name, id, correo, todos2};
        miStorage.setItem("usuario", JSON.stringify(encontrado));
    } 
  
    let miStorage = window.localStorage;
    let usuario = JSON.parse(miStorage.getItem('usuario'));
    let n=usuario.name;
   v_id=usuario.id;

    console.log(n)
    document.getElementById('name').text = n;

    console.log("e")
    console.log("aca onmount", v_id)

    let abrirModal = localStorage.getItem("abrirModal");
    if (abrirModal === "true") {
        localStorage.removeItem("abrirModal"); 
        await showModal();
    }





});

function borrarCookies() {
    document.cookie.split(";").forEach((c) => {
        document.cookie = c
            .replace(/^ +/, "") // Elimina espacios en blanco al inicio
            .replace(/=.*/, "=;expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/"); // Expira la cookie
    });
}

function confirmacion() {
        Swal.fire({
      title: "¿Estas seguro?",
      text: "Se perdera lo que no hayas guardado",
      icon: "warning",
      showCancelButton: true,
      confirmButtonColor: "#3085d6",
      cancelButtonColor: "#d33",
      confirmButtonText: "Si, cerrar!"
    }).then((result) => {
      if (result.isConfirmed) {
        localStorage.clear();
        borrarCookies()

        window.location.href = "/";
      }
    });
    
}
 



async function showModal() {

  const modalElement = document.getElementById("perfil_modal");
        if (modalElement) {
            modal_perfil = new bootstrap.Modal(modalElement);
        }


        if (modal_perfil) {
            modal_perfil.show();
        }
        document.getElementById("nav_correo").value = "s";
        
        
        try {
            console.log("entra al try");
            const response = await fetch("http://127.0.0.1:8000/get_user", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id: v_id,
                }),
            });

            const data = await response.json();
            console.log("entra al try");
            console.log(data);
            todos = data;

            document.getElementById("nav_correo").value = todos.usuario;
            document.getElementById("nav_nombre").value = todos.nombre;
            document.getElementById("nav_apellido").value = todos.apellido;
            document.getElementById("nav_password").value = todos.password;
            document.getElementById("nav_documento").value = todos.documento;
            document.getElementById("nav_telefono").value = todos.telefono;
        } catch (e) {
            error = e.message;
            console.log(e);
        }
}    
      
function redirigir() {
  if (window.location.pathname === "/administrador_vista") {
    showModal()
}else{
  localStorage.setItem("abrirModal", "true"); // Guardar indicador en localStorage
}

}


async function editar() {
        const correov= document.getElementById("nav_correo");
        correov.removeAttribute("readonly");

        const nombrev= document.getElementById("nav_nombre");
        nombrev.removeAttribute("readonly");

        const apellidov= document.getElementById("nav_apellido");
        apellidov.removeAttribute("readonly");

        const passwordv= document.getElementById("nav_password");
        passwordv.removeAttribute("readonly");

        const documentov= document.getElementById("nav_documento");
        documentov.removeAttribute("readonly");

        const telefonov=  document.getElementById("nav_telefono");
        telefonov.removeAttribute("readonly");
        henry=false
        
    }

  async function actualizar() {

  let miStorage = window.localStorage;
  let v_id = JSON.parse(miStorage.getItem("usuario"));
  v_id = v_id.id;
  console.log(v_id);
  console.log("entra aca a actualizar"+v_id)
  try{ let v_correo =document.getElementById("nav_correo").value;
  let v_nombre =document.getElementById("nav_nombre").value;
  let v_apellido  =document.getElementById("nav_apellido").value;
  let  v_password =document.getElementById("nav_password").value;
  let  v_documento =document.getElementById("nav_documento").value;
  let v_telefono  =document.getElementById("nav_telefono").value;
  console.log(v_password)
  const response = await fetch("http://127.0.0.1:8000/update_adm", {
          method: "PUT",
          headers: {
              "Content-Type": "application/json",
          },
          body: JSON.stringify({
              usuario: v_correo,
              nombre: v_nombre,
              apellido: v_apellido,
              password: v_password,
              documento: v_documento,
              telefono: v_telefono,
              id: v_id
          }),
      });
      console.log("actualizado")



      


  henry=true
  sendSMS()

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
    title: "datos actualizado con exito",
  });



  setTimeout(() => {
  location.reload();
    }, 2000);
  }catch(e){
  error=e.message
  console.log(error)
  }

}



</script>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="/administrador_vista" id="name" on:click={redirigir}>.</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#Menu-usuarios" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="Menu-usuarios">
        <ul class="navbar-nav">
          <li class="nav-item dropdown">
            <!--Aca empieza otro-->
            <a class="nav-link dropdown-toggle" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Usuarios
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <li><a class="dropdown-item" href="/administrador_vista/Usuario/Crear_usuario">Registrar usuario</a></li>
              <li><a class="dropdown-item" href="/administrador_vista/Usuario/Buscar_usuario">Buscar usuario</a></li>
            </ul>
            <!--Aca empieza otro-->
          </li>
           <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Citas medicas
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <li><a class="dropdown-item" href="/administrador_vista/Citas_medicas/crear_citas">Asignar citas</a></li>
              <li><a class="dropdown-item" href="/administrador_vista/Citas_medicas/buscar_citas">Gestionar citas</a></li>
            </ul>
<!--Aca empieza otro-->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle"  id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Medicos
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <li><a class="dropdown-item" href="/administrador_vista/Doctor_adm/regis_medicos">Registrar medico</a></li>
                <li><a class="dropdown-item" href="/administrador_vista/Doctor_adm/buscar_medicos">Buscar medico</a></li>
              <!--  <li><a class="dropdown-item" >Actualizar medico</a></li>
                <li><a class="dropdown-item" >Desactivar medico</a></li>
              </ul>-->

          </li>
          <!--Aca empieza otro-->
          <li class="nav-item">
            <a class="nav-link" href="/administrador_vista/Reportes">Reportes</a>
          </li>

          
          <li class="nav-item">
            <a class="nav-link" href="/administrador_vista/Dashboard">Dashboard</a><!---->
          </li>
          <!--
          <li class="nav-item">
            <a class="nav-link" href="/administrador_vista/perfil_adm">Perfil</a>
          </li>
          -->
          <li class="nav-item">
            <a class="nav-link" href="/administrador_vista/create_rol">Roles</a>
          </li>

          <li class="nav-item">
            <a class="nav-link" href="/botci">Botci :D</a>
          </li>

        </ul>

        

        
        <form class="d-flex   nav-item nav-link ms-auto">
          <button class="btn btn-outline-dark  nav-item" on:click={confirmacion} href="#" aria-label="Cerrar edición de usuario">Cerrar sesion</button>
        </form>
       
      </div>
    </div>
  </nav>

  <div class="modal fade"  id="perfil_modal" tabindex="-1" aria-labelledby="rModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="mleModalLabel">
                    <b>Perfil del administrador</b>
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <div class="card text-center border-dark mt-4">
              <div class="card-header">Informacion del administrador</div>


              <div class="row">
                <div class="col-md-6">
                  <!--Correo/usuario-->
                  <div class="mb-3 mt-2 mx-2">
                    <div class="input-group">
                        <span class="input-group-text"><i class="bi bi-person-circle"></i></span>
                        <input type="text" class="form-control" id="nav_correo" required autocomplete="off" readonly>
                    </div>
                 </div>

                  <!--password-->
                 <div class="mb-3 mt-2 mx-2" role="presentation">
                  <div class="input-group" >
                      <span class="input-group-text"><i class="bi bi-lock"></i></span>
                      <input type="password" class="form-control" name="password" id="nav_password" required autocomplete="off" readonly>
                  </div> 
                 </div>
                 <!--nombre-->
                 <div class="mb-3 mt-2 mx-2">
                  <div class="input-group">
                      <span class="input-group-text"><i class="bi bi-person"></i></span>
                      <input type="text" class="form-control" id="nav_nombre" required autocomplete="off" readonly>
                  </div> 
                 </div>
                 <!--apellido-->
                 <div class="mb-3 mt-2 mx-2">
                  <div class="input-group">
                      <span class="input-group-text"><i class="bi bi-person"></i></span>
                      <input type="text" class="form-control" id="nav_apellido" required autocomplete="off" readonly>
                  </div> 
                 </div>
                  <!--Documento-->
                  <div class="mb-3 mt-2 mx-2">
                    <div class="input-group">
                        <span class="input-group-text"><i class="bi bi-card-list"></i></span>
                        <input type="text" class="form-control" id="nav_documento" required autocomplete="off" readonly>
                    </div> 
                   </div>
                   <!--Telefono-->
                  <div class="mb-3 mt-2 mx-2">
                    <div class="input-group">
                        <span class="input-group-text"><i class="bi bi-telephone"></i></span>
                        <input type="text" class="form-control" id="nav_telefono" required autocomplete="off" readonly>
                    </div> 
                   </div>
                 
               </div>


                <div class="col-md-6">
                  <img src="/image.png" alt="Hospital" class="img-fluid w-100 h-100" style="object-fit: cover;">
                  
                </div>
             </div>

          
              <div class="card-footer">
          
                  {#if henry}
                    <!-- Mostrar botón "Desactivar" si el usuario está activo -->
                    <button class="btn btn-success" on:click={() =>editar()}>
                      Editar
                    </button>
                  {:else}
                    <!-- Mostrar botón "Activar" si el usuario está desactivado -->
                    <button class="btn btn-outline-info" id="sendMessage" on:click={() => actualizar()}>
                      Actualizar
                    </button>
                  {/if}
                  
              </div>
          </div>
            </div>
          
        </div>
    </div>
</div>


