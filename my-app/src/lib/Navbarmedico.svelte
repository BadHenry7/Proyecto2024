<script>

    import { onMount } from "svelte";
    
    
    onMount(() => {

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
        let encontrado = { name, id, correo};
        miStorage.setItem("usuario", JSON.stringify(encontrado));
    } 
  


        let miStorage = window.localStorage;
        let name = JSON.parse(miStorage.getItem('usuario'));
        let n=name.name
    
    console.log(n)
        document.getElementById('name').text = n;
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
        
    
  </script>
  
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
      <div class="container-fluid">
        <a class="navbar-brand mx-4" href="/medico_vista" id="name" aria-label="Name del medico"></a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="Menu-usuarios" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNavDropdown">
          <ul class="navbar-nav">
            <li class="nav-item mx-4">
              <a class="nav-link" href="/medico_vista/citas_medico">Agenda</a>
            </li>
            <li class="nav-item mx-4">
              <a class="nav-link" href="/medico_vista/historial_clinico">Paciente</a>
            </li>
            <li class="nav-item mx-4">
              <a class="nav-link" href="/medico_vista/reporte_medico">Reportes</a><!---->
            </li>
            <li class="nav-item mx-4">
              <a class="nav-link " href="/botci">Botci</a>
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
            <button class="btn btn-outline-dark" on:click={confirmacion} href="#" >Cerrar sesion</button>
          </form>
        </div>
      </div>
    </nav>