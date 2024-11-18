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
          window.location.href = "/";
        }
      });
      
    }
        
    
  </script>
  
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand mx-4" href="/medico_vista" id="name"></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="Menu-usuarios" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li class="nav-item mx-4">
              <a class="nav-link" href="">Agenda</a>
            </li>
            <li class="nav-item mx-4">
              <a class="nav-link" href="">Paciente</a>
            </li>
            <li class="nav-item mx-4">
              <a class="nav-link" href="">Certificados</a><!---->
            </li>
            <li class="nav-item mx-4">
              <a class="nav-link" href="">Botci</a>
            </li>
            <!--<li class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                Servicios
              </a>
              <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                <li><a class="dropdown-item" href="">Action</a></li>
                <li><a class="dropdown-item" href="">Another action</a></li>
                <li><a class="dropdown-item" href="">Something else here</a></li>
              </ul>
            </li>-->
          </ul>
  
          <form class="d-flex   nav-item nav-link ms-auto">
            <a class="btn btn-outline-dark" on:click={confirmacion} href="#" >Cerrar sesion</a>
          </form>
        </div>
      </div>
    </nav>