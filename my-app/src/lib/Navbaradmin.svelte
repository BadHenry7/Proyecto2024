<script>

import { onMount } from "svelte";


onMount(() => {//no va a funcionar  no no no no no no dale a seguirme
    let miStorage = window.localStorage;
    let name = JSON.parse(miStorage.getItem('usuario'));
    let n=name.name

console.log(n)
    document.getElementById('name').text = n;
    });

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
        window.location.href = "/";
      }
    });
    
  }

    
</script>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="/administrador_vista" id="name">.</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="Menu-usuarios" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
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
          <li class="nav-item">
            <a class="nav-link" href="/administrador_vista/perfil_adm">Perfil</a>
          </li>

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