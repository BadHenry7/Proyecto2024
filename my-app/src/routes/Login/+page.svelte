<script>
    import { onMount } from "svelte";

    let todos = {};
    let loading = true;
    let error = null;
    let v_usuario = "";
    let v_password = "";

    onMount(async () => {
        try {
            const response = await fetch("");

            if (!response.ok) throw new Error("Error al cargar los datos");
            todos = await response.json();
        } catch (e) {
            error = e.message;
        } finally {
            loading = false;
        }
    });

    async function Login() {
        try {
            const response = await fetch("http://127.0.0.1:8000/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    usuario: v_usuario,
                    password: v_password,
                }),
            });

            const data = await response.json();
            console.log(data);

            if (response.ok) {
                alert("Inicio de sesión exitoso");
                // Redireccionar o actualizar el estado
            } else {
                alert("Error de autenticación");
            }
        } catch (e) {
            error = e.message;
            alert("Error en la solicitud: " + error);
        }
    }
</script>
<div class="col-sm-2 col-md-3 col-xl-3 col-lg-3  col-2">
    <a href="/" class="btn btn-outline-dark mt-1 mx-2">Volver</a>
</div>
<div class="container bg-info">
   


    <div class="row g-2">
        <div class="col-auto" style="margin-right: ;">
            <input type="text" placeholder="Correo" bind:value={v_usuario} />
        </div>
        <div class="col-auto">
            <input
                type="password"
                placeholder="Contraseña"
                bind:value={v_password}
            />
        </div>
        <button on:click={Login}>Ingresar</button>
    </div>
</div>
