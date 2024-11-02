<script>
    import { onMount } from "svelte";

    let todos = {};
    let loading = true;
    let error = null;
    let v_usuario = "";
    let v_password = "";
    let loginModal;

    /*
    onMount(async () => {
        try {
            const response = await fetch("http://127.0.0.1:8000/login");
            if (!response.ok) throw new Error("Error al cargar los datos");
            todos = await response.json();
        } catch (e) {
            error = e.message;
            alert ("sss")
        } finally {
            loading = false;
        }
    });*/

    onMount(() => {
        const modalElement = document.getElementById("loginex");
        if (modalElement) {
            loginModal = new bootstrap.Modal(modalElement);
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
                //

                let name = data.resultado[0].nombre;
                let id = data.resultado[0].id;

                let encontrado = { name,id };

                let miStorage = window.localStorage;
                miStorage.setItem("usuario", JSON.stringify(encontrado));
                alert("Inicio de sesión exitoso. Bienvenido " + name);
                //document.getElementById("loginex").style.display = "flex";
                showModal();
            } else {
                alert("Error de autenticación");
            }
        } catch (e) {
            error = e.message;
            alert("Error en la solicitud: " + error);
        }
    }

    function showModal() {
        if (loginModal) {
            loginModal.show();
        }
    }

    function Ocultar() {
        loginModal.hide();
    }
</script>

<div class="col-sm-2 col-md-3 col-xl-3 col-lg-3 col-2" style="margin-top: 2%;">
    <a href="/" class="btn btn-outline-dark mt-1 mx-2">Volver</a>
</div>
<div class="container" style="margin-top: 10%;">
<div style="text-align: center; margin-top: 20px; " class="fs-3">
    <b>Inicio de sesión</b>
</div>
    <div class="row justify-content-center g-2">
        <div class="col-md-4 mb-3">
            <input
                type="text"
                class="form-control"
                placeholder="Correo"
                bind:value={v_usuario}
            />
        </div>

        <div class="col-md-4 mb-3">
            <input
                class="form-control"
                type="password"
                placeholder="Contraseña"
                bind:value={v_password}
            />
        </div>
    </div>

    <div class="text-center">
        <button
            type="button"
            class="btn btn-primary mt-3"
            on:click={Login}>Ingresar
        </button>
    </div>
</div>

<style>
    .container {
        max-width: 600px; /* Limita el ancho del contenedor */
        margin: auto; /* Centra el contenedor horizontalmente */
        padding: 20px; /* Agrega padding interno */
        border-radius: 10px; /* Bordes redondeados */
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Sombra para profundidad */
        background-color: #f9f9f9; /* Color de fondo claro */
    }

    .form-control {
        border-radius: 5px; /* Bordes redondeados para los inputs */
        border: 1px solid #ced4da; /* Borde gris claro */
    }

    .form-control:focus {
        border-color: #80bdff; /* Color del borde al enfocar */
        box-shadow: 0 0 0 0.2rem rgba(0, 123, 255, 0.25); /* Sombra al enfocar */
    }

    .btn-primary {
        background-color: #007bff; /* Color de fondo del botón */
        border: none; /* Sin borde */
        padding: 10px 20px; /* Padding interno */
    }

    .btn-primary:hover {
        background-color: #0056b3; /* Color de fondo al pasar el mouse */
    }

    @media (max-width: 768px) {
        .col-md-4 {
            width: 100%; /* Hace que los inputs ocupen el 100% en pantallas pequeñas */
        }
    }
</style>


<div
    class="modal fade"
    id="loginex"
    tabindex="-1"
    aria-labelledby="rModalLabel"
    aria-hidden="true"
>
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <button
                    type="button"
                    class="btn-close"
                    data-bs-dismiss="modal"
                    aria-label="Close"
                ></button>
            </div>
            <div class="modal-body row">
                <h2>Selecciona tu rol</h2>
                <a
                    on:click={Ocultar}
                    href="administrador_vista"
                    class="col-md-4 text-decoration-none btn btn-outline-dark"
                    style="margin-left: 4%; margin-top:2%">Administrador</a
                >
                <div class="col-md-3" style="color: white;">relleno :D</div>
                <a
                    on:click={Ocultar}
                    href="usuario"
                    class="col-md-4 text-decoration-none btn btn-outline-dark"
                    style="margin-top:2%">Usuario</a
                >
            </div>
        </div>
    </div>
</div>


<!--  <div class="modal show">
        <div class="modal-content">
            <h2>Selecciona tu rol</h2>
            <button on:click={() => redirect('admin')}>Administrador</button>
            <button on:click={() => redirect('user')}>Usuario</button>
        </div>
    </div>
-->
