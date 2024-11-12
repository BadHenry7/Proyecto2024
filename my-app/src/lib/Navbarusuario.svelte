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
      <a class="navbar-brand" href="/usuario" id="name"></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="Menu-usuarios" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Gestion de citas
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <li><a class="dropdown-item" href="/usuario/citas_usuario/crear_citas_vista_usuario">Agendar citas</a></li>
              <li><a class="dropdown-item" href="/usuario/citas_usuario/revisar_citas_vista_usuario">Ver citas programadas</a></li>
              <li><a class="dropdown-item" href="">Cancelar citas</a></li>
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/usuario/Reportes">Reportes</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="">Certificados</a><!---->
          </li>
          <li class="nav-item">
            <a class="nav-link" href="">Perfil</a>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Servicios
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <li><a class="dropdown-item" href="">Action</a></li>
              <li><a class="dropdown-item" href="">Another action</a></li>
              <li><a class="dropdown-item" href="">Something else here</a></li>
            </ul>
          </li>
        </ul>

        <form class="d-flex   nav-item nav-link ms-auto">
          <a class="btn  nav-item" href="/">Cerrar sesion</a>
        </form>
      </div>
    </div>
  </nav>