<script>

import { onMount } from "svelte";


onMount(() => {//no va a funcionar  no no no no no no dale a seguirme
    let miStorage = window.localStorage;
    let name = JSON.parse(miStorage.getItem('usuario'));
    let n=name.name

console.log(n)
    document.getElementById('name').text = n;
    });

    
</script>


<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="/administrador_vista" id="name"></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="Menu-usuarios" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item dropdown">
            <!--Aca empieza otro-->
            <a class="nav-link dropdown-toggle" href="" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Usuarios
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <li><a class="dropdown-item" href="/administrador_vista/Usuario/Crear_usuario">Registrar usuario</a></li>
              <li><a class="dropdown-item" href="/administrador_vista/Usuario/Buscar_usuario">Buscar usuario</a></li>
              <li><a class="dropdown-item" href="">Desactivar usuario</a></li>
            </ul>
            <!--Aca empieza otro-->
          </li>
           <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Citas medicas
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <li><a class="dropdown-item" href="/administrador_vista/Citas_medicas/crear_citas">Asignar cita </a></li>
              <li><a class="dropdown-item" href="/administrador_vista/Citas_medicas/buscar_citas">Buscar cita</a></li>
              <li><a class="dropdown-item" href="/administrador_vista/Citas_medicas/actualizar_citas">Modificar cita</a></li>
              <li><a class="dropdown-item" href="/administrador_vista/Citas_medicas/cancelar_citas">Cancelar cita</a></li>
            </ul>
<!--Aca empieza otro-->
            <li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Medicos
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <li><a class="dropdown-item" href="/administrador_vista/Crear_usuario">Registrar medico</a></li>
                <li><a class="dropdown-item" href="/administrador_vista/Buscar_usuario">Buscar medico</a></li>
                <li><a class="dropdown-item" href="">Actualizar medico</a></li>
                <li><a class="dropdown-item" href="">Desactivar medico</a></li>
              </ul>

          </li>
          <!--Aca empieza otro-->
          <li class="nav-item">
            <a class="nav-link" href="/administrador_vista/Reportes">Reportes</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/administrador_vista/Dashboard">Dashboard</a><!---->
          </li>
          <li class="nav-item">
            <a class="nav-link" href="">Perfil</a>
          </li>

          <li class="nav-item">
            <a class="nav-link disabled" href="">Botci :D</a>
          </li>

        </ul>

        

        
        <form class="d-flex   nav-item nav-link ms-auto">
          <a class="btn  nav-item" href="/">Cerrar sesion</a>
        </form>
       
      </div>
    </div>
  </nav>