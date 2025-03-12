<script>

  import { onMount } from "svelte";
  
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
        let encontrado = { name, id, correo};
        miStorage.setItem("usuario", JSON.stringify(encontrado));
    } 
  

    
      let miStorage = window.localStorage;
      let usuario = JSON.parse(miStorage.getItem('usuario'));
    let n=usuario.name;
   v_id=usuario.id;
  
  console.log(n)
      document.getElementById('name').text = n;


      
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


  function redirigir() {
      if (window.location.pathname === "/usuario") {
        showModal()
    }else{
      localStorage.setItem("abrirModal", "true"); // Guardar indicador en localStorage
    }
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
    
      

  
  
</script>

<nav class="navbar navbar-expand-lg navbar-light bg-light">
    <div class="container-fluid">
      <a class="navbar-brand" href="/usuario" id="name" aria-label="Name del medico" on:click={redirigir}></a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="Menu-usuarios" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavDropdown">
        <ul class="navbar-nav">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              Gestion de citas
            </a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
              <li><a class="dropdown-item" href="/usuario/citas_usuario/crear_citas_vista_usuario">Agendar citas</a></li>
              <li><a class="dropdown-item" href="/usuario/citas_usuario/revisar_citas_vista_usuario">Ver citas programadas</a></li>
          
            </ul>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/usuario/Reportes">Reportes</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/certificados">Certificados</a><!---->
          </li>
        <!--  <li class="nav-item">
            <a class="nav-link" href="/usuario/perfil">Perfil</a>
          </li>
        -->
        </ul>

        <form class="d-flex   nav-item nav-link ms-auto">
          <button class="btn btn-outline-dark" on:click={confirmacion}  >Cerrar sesion</button>
        </form>
      </div>
    </div>
  </nav>


  
  <div class="modal fade"  id="perfil_modal" tabindex="-1" aria-labelledby="rModalLabel" aria-hidden="true">
    <div class="modal-dialog modal-lg">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="mleModalLabel">
                    <b>Perfil del paciente</b>
                </h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
              <div class="card text-center border-dark mt-4">
              <div class="card-header">Bienvenido al apartado de Informacion personal</div>


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
          
                  <p>Recuerda que para cambiar tu informacion personal debes enviar un correo al hostipalinc.github@gmail.com</p>
                  
              </div>
          </div>
            </div>
          
        </div>
    </div>
</div>