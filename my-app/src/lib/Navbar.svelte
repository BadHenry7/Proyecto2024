<script>

    import { onMount } from "svelte";
    
    let todos={}
    let loading=true
    let error=null
    onMount(() => {//no va a funcionar  no no no no no no dale a seguirme
        let miStorage = window.localStorage;
        let name = JSON.parse(miStorage.getItem('usuario'));
        let n=name.name
    
    console.log(n)
    mostrar_modulos()

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
    


      async function mostrar_modulos() {
        let miStorage = window.localStorage;
        let usuario = JSON.parse(miStorage.getItem('usuario'));
        let v_id_rol=usuario.rol_v
        console.log("idddd", v_id_rol)
        try {
          const response = await fetch("http://127.0.0.1:8000/get_modulos_asignado",{
      method: "POST",
      headers: {
        "Content-Type": "application/json", },
        body: JSON.stringify({
        id:v_id_rol,
      }), 
    });


      if (!response.ok) throw new Error("Error al cargar los datos");
     const data = await response.json();

      todos=data.resultado
      console.log("-----",todos)
      console.log("-----",todos.nombre)

      

    } catch (e) {
      alert("s")
      error = e.message;
      
    } finally {
      loading = false;
    }
        
      }
      var v_henry=""
    </script>
    
    
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
        <div class="container-fluid">
          <a class="navbar-brand" href="/vista_main" id="name">.</a>
          <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="Menu-usuarios" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
          </button>
          <div class="collapse navbar-collapse" id="navbarNavDropdown">
            <ul class="navbar-nav">



                {#each todos as todo, i}


                {#if todo.nombre_modulo!="Administrador" &&  (i === 0 ||  todo.nombre_modulo !== todos[i - 1].nombre_modulo)}
                {console.log("revisando:",todo.nombre_modulo)}
                <li class="nav-item dropdown">
                    <!--Aca empieza otro-->
                    <a class="nav-link dropdown-toggle" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                      {todo.nombre_modulo}
                    </a>
                    <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
                   


                        {#each todos as subtodo}
                      {console.log("toma el valor de:",subtodo.nombre_modulo)}
                      {console.log("toma el 2valor de:",todo.nombre_modulo)}


                  {#if subtodo.nombre_modulo===todo.nombre_modulo}

                      {console.log("revisando123:",subtodo.submodulo)}
                      {console.log("revisando555:",subtodo.url)}
                      

                      <li><a class="dropdown-item" href="{subtodo.url}">{subtodo.submodulo}</a></li>

                      {/if}
                        {/each}

                    </ul>
    
                    </li>
                
                
                
                {:else if todo.nombre_modulo==="Administrador" }
                <li class="nav-item">
                  {console.log("revisando1231321232323:")}
                    <a class="nav-link" href="{todo.url}">{todo.submodulo}</a>
                  </li>
                {/if}
                

               
                {/each}

  
    
            </ul>
    
            
    
            
            <form class="d-flex   nav-item nav-link ms-auto">
              <button class="btn btn-outline-dark  nav-item" on:click={confirmacion} href="#" aria-label="Cerrar edición de usuario">Cerrar sesion</button>
            </form>
           
          </div>
        </div>
      </nav>