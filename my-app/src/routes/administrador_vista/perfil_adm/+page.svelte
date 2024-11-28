<script>
    import Navbaradmin from "../../../lib/Navbaradmin.svelte";
    import { onMount } from "svelte";

    let todos = {};
    let error = null;
    var v_id=1
   
    onMount(async () => {
        let miStorage = window.localStorage;
        let v_id = JSON.parse(miStorage.getItem("usuario"));
        v_id = v_id.id;
        console.log(v_id);

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

            document.getElementById("correo").value = todos.usuario;
            document.getElementById("nombre").value = todos.nombre;
            document.getElementById("apellido").value = todos.apellido;
            document.getElementById("password").value = todos.password;
            document.getElementById("documento").value = todos.documento;
            document.getElementById("telefono").value = todos.telefono;
        } catch (e) {
            error = e.message;
            console.log(e);
        }
    });
   
        
    async function editar() {
        const correov= document.getElementById("correo");
        correov.removeAttribute("readonly");

        const nombrev= document.getElementById("nombre");
        nombrev.removeAttribute("readonly");

        const apellidov= document.getElementById("apellido");
        apellidov.removeAttribute("readonly");

        const passwordv= document.getElementById("password");
        passwordv.removeAttribute("readonly");

        const documentov= document.getElementById("documento");
        documentov.removeAttribute("readonly");

        const telefonov=  document.getElementById("telefono");
        telefonov.removeAttribute("readonly");
        henry=false
        
    }


    var henry=true


    async function actualizar() {
        let miStorage = window.localStorage;
        let v_id = JSON.parse(miStorage.getItem("usuario"));
        v_id = v_id.id;
        console.log(v_id);
        console.log("entra aca a actualizar"+v_id)
       try{ let v_correo =document.getElementById("correo").value;
        let v_nombre =document.getElementById("nombre").value;
        let v_apellido  =document.getElementById("apellido").value;
        let  v_password =document.getElementById("password").value;
        let  v_documento =document.getElementById("documento").value;
        let v_telefono  =document.getElementById("telefono").value;
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
          }, 1000);
    }catch(e){
    error=e.message
    console.log(error)
    }
       
    }
</script>

<Navbaradmin></Navbaradmin>

<div
    class="card text-center border-dark mt-4"
    style="width: 50%; margin-left: 20%;"
>
    <div class="card-header">Informacion del administrador</div>

    <div class="card-body">
        <div class="row">
            <div class="col-xl-2">
                <label for="">Correo:</label>
            </div>
            <div class="col-xl-2">
                <input id="correo" type="text" readonly style="border: none;" />
            </div>
        </div>

        <div class="row">
            <div class="col-xl-2 pt-2">
                <label for="">Contraseña:</label>
            </div>
            <div class="col-xl-2 pt-2">
                <input
                    id="password"
                    type="password"
                    readonly
                    style="border: none;"
                   
                />
            </div>
        </div>

        <div class="row">
            <div class="col-xl-2">
                <label for="">Nombre:</label>
            </div>
            <div class="col-xl-2 pt-2">
                <input id="nombre" type="text" readonly style="border: none;" />
            </div>
        </div>

        <div class="row">
            <div class="col-xl-2">
                <label for="">Apellido:</label>
            </div>
            <div class="col-xl-2 pt-2">
                <input
                    id="apellido"
                    type="text"
                    readonly
                    style="border: none;" 
                />
            </div>
        </div>

        <div class="row">
            <div class="col-xl-2">
                <label for="">Documento:</label>
            </div>
            <div class="col-xl-2 pt-2">
                <input
                    id="documento"
                    type="text"
                    readonly
                    style="border: none;"  
                />
            </div>
        </div>

        <div class="row">
            <div class="col-xl-2">
                <label for="">Telefono:</label>
            </div>
            <div class="col-xl-2 pt-2">
                <input
                    id="telefono"
                    type="text"
                    readonly
                    style="border: none;" 
                />
            </div>
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
          <button class="btn btn-outline-info" on:click={() => actualizar()}>
            Actualizar
          </button>
        {/if}

    </div>
</div>
