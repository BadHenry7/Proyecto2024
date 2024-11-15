<script>
    import Navbarusuario from "$lib/Navbarusuario.svelte";
    import { onMount } from "svelte";
    let todos = {};
    let error = null;

    onMount(async () => {
        let miStorage = window.localStorage;
        let v_id = JSON.parse(miStorage.getItem("usuario"));
        v_id = v_id.id;
        console.log(v_id);
       
        try {
            const response = await fetch("http://127.0.0.1:8000/get_user", {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                },
                body: JSON.stringify({
                    id: v_id,
                }),
            });
            const data=await response.json();
            console.log(data)
            todos=data
            console.log(todos.usuario)

        document.getElementById("correo").value=todos.usuario;
       document.getElementById("nombre").value=todos.nombre;
        document.getElementById("apellido").value=todos.apellido;
       document.getElementById("documento").value=todos.documento;
        document.getElementById("telefono").value=todos.telefono;
        console.log("sss")

            
        } catch (e) {
            error = e.message;
            console.log(error);
        }
    });
</script>

<Navbarusuario></Navbarusuario>

<div
    class="card text-center border-dark shadow mt-4"
    style="width: 60%; margin-left: 20%;"
>
    <div class="card-header">Informacion personal</div>
    <div class="card-body">
        <h5 class="card-title">
            Bienvenido al apartado de Informacion personal
        </h5>

        <div class="row">
            <div class="col-xl-5">
                <label for=""><b>Correo:</b></label>
                <input type="text" id="correo" readonly style="border: none;" />
            </div>
        </div>

        <div class="row">
            <div class="col-xl-5 pt-2">
                <label for=""><b>Nombre:</b></label>
                <input type="text" id="nombre" readonly style="border: none;" />
            </div>
        </div>

        <div class="row">
            <div class="col-xl-5 pt-2">
                <label for=""><b>Apellido:</b></label>
                <input
                    type="text"
                    id="apellido"
                    readonly
                    style="border: none;"
                />
            </div>
        </div>

        <div class="row">
            <div class="col-xl-5 pt-2">
                <label for=""><b>Documento:</b></label>
                <input
                    type="text"
                    id="documento"
                    readonly
                    style="border: none;"
                />
            </div>
        </div>

        <div class="row">
            <div class="col-xl-5 pt-2">
                <label for=""><b>Telefono:</b></label>
                <input
                    type="text"
                    id="telefono"
                    readonly
                    style="border: none;"
                />
            </div>
        </div>
    </div>

    <div class="card-footer">
        Recuerda que para cambiar tu informacion personal debes enviar un correo
        al hostipalinc.github@gmail.com
    </div>
</div>
