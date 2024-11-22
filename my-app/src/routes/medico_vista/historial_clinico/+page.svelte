<script>
    import Navbarmedico from "$lib/Navbarmedico.svelte";
    import { onMount } from "svelte";

    let loading = true;
    onMount(async () => {
        try {
            const response = await fetch(
                "http://127.0.0.1:8000/get_cita_admin/",
                {
                    method: "GET",
                },
            );
            const data = await response.json();
            citas = data.resultado;
            console.log("citas", citas);
        } catch (e) {
            error = e.message;
            console.log(error);
        } finally {
        }
    });

    let todos = {};
    let todos2 = {};
    let citas = {};
    let error = null;
    let comprobar = false;

    async function buscar() {
        let buscardocument_v =
            document.getElementById("buscardocument_v").value;
        console.log("documento a buscar: ", buscardocument_v);
        const response = await fetch(
            "http://127.0.0.1:8000/get_user_document",
            {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                },
                body: JSON.stringify({
                    documento: buscardocument_v,
                }),
            },
        );
        loading = false;
        const data = await response.json();
        console.log(data);
        todos = data;
        console.log("Nombre del usuario: ", todos.nombre);
        document.getElementById("nombre").textContent = todos.nombre;
        document.getElementById("documento").textContent = todos.documento;
        document.getElementById("telefono").textContent = todos.telefono;
        nombre_v = todos.nombre;
        let v_id = todos.id;
        console.log("id del usuario", v_id);

        setTimeout(() => {
            globalThis.$("#myTable").DataTable(); // Para convertrlo en datatable :D
        }, 0);
        try {
            const response = await fetch(
                "http://127.0.0.1:8000/historia_clinica",
                {
                    method: "POST",
                    headers: {
                        "Content-type": "application/json",
                    },
                    body: JSON.stringify({
                        id_paciente: v_id,
                    }),
                },
            );
            const data = await response.json();
            console.log("Data de cita");
            console.log(data);
            todos2 = data.resultado;
            console.log(todos2);
            comprobar = true;
        } catch (e) {
            error = e.message;
            console.log(error);
        }
    }
    var nombre_v = "";
    async function editar() {
        console.log("Entro a todos");
        document.getElementById("nombre_v").textContent = nombre_v;

        //Mostrar el card que permite añadir otro historial clinico
        const v_editar = document.getElementById("nav-listado");
        v_editar.removeAttribute("class");

        //Ocultar historial clinico
        let ocultar = document.getElementById("Mostrarhistorial");
        ocultar.setAttribute("class", "fade");

        //cambiar de posicion
        const cambiar = ocultar.parentElement;
        cambiar.insertBefore(v_editar, ocultar);

        const v_edit_sintomas = document.getElementById("sintomas");
        v_edit_sintomas.removeAttribute("readonly");
        v_edit_sintomas.focus();

        const v_edit_descripcion_sintomas = document.getElementById(
            "descripcion_sintomas",
        );
        v_edit_descripcion_sintomas.removeAttribute("readonly");

        const v_edit_diagnostico = document.getElementById("diagnostico");
        v_edit_diagnostico.removeAttribute("readonly");

        const v_edit_descripciond = document.getElementById(
            "descripcion_diagnostico",
        );
        v_edit_descripciond.removeAttribute("readonly");

        const v_edit_Observaciontratamiento = document.getElementById(
            "Observaciontratamiento",
        );
        v_edit_Observaciontratamiento.removeAttribute("readonly");
    }

    async function guardar() {
        console.log("entra a actualizar");
        console.log(todos);
        let sintomas_v = document.getElementById("sintomas").value;
        let descripcions_v = document.getElementById( "descripcion_sintomas").value;
        let estado_v = 1;
        let v_id_paciente = todos.id;
        console.log(v_id_paciente);
        try {
            let id_cita_v=document.getElementById('citas').value;
            console.log("id de la cita", id_cita_v)
            const response = await fetch("http://127.0.0.1:8000/create_sintomas", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    nombre: sintomas_v,
                    descripcion: descripcions_v,
                    estado: estado_v,
                    id_cita: id_cita_v,
                }),
            });
        } catch (e) {
            error = e.message;
            console.log(error);
        }

        try {
            let id_cita_v=document.getElementById('citas').value;
            console.log("id de la cita", id_cita_v)

            let diagnostico_v=document.getElementById('diagnostico').value;
            let descripcions_d = document.getElementById( "descripcion_diagnostico").value;
            let Observacion_v = document.getElementById( "Observaciontratamiento").value;
            let v_estado=1
            
            

            const response = await fetch("http://127.0.0.1:8000/create_diagnosticos", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    id_cita: id_cita_v,//mano ya estas ahi?
                    resultado: diagnostico_v,
                    descripcion: descripcions_d,
                    Observacion: Observacion_v,
                    estado: v_estado
                }),
            });

            const Toast = Swal.mixin({
          toast: true,
          position: "bottom-end",
          showConfirmButton: false,
          timer: 3000,
          timerProgressBar: true,
          didOpen: (toast) => {
            toast.onmouseenter = Swal.stopTimer;
            toast.onmouseleave = Swal.resumeTimer;
          },
        });
        Toast.fire({
          icon: "error",
          iconColor: "white",
          color: "white",
          background: "#ff4e4e",
          title: "Historial clinico añadido",
        });


        setTimeout(() => {
        location.reload();
      }, 3000);

        } catch (e) {
            error = e.message;
            console.log(error);
        }
    }
</script>

<Navbarmedico></Navbarmedico>

<div class="container" id="Mostrarhistorial">
    <div>
        <label for="">Cedula:</label>
        <input type="text" class="mt-3" id="buscardocument_v" />
        <button class="btn btn-outline-info" on:click={buscar}>Buscar</button>
    </div>
    <div class="card border-dark shadow mt-5">
        <div class="card-header">
            <!--Header-->
            <div class="fs-2 text-center">
                Historial clinico de <span class="" id="nombre"></span>
            </div>
        </div>
        <!--Fin del Header-->

        <div class="card-body">
            <!--Body-->

            <div>
                <label for=""
                    ><b>Documento:</b> <span id="documento"> </span></label
                >
                <br />
                <label for=""
                    ><b>Telefono:</b> <span id="telefono"></span></label
                >
            </div>

            <div class="pt-4">
                <h3 style="color: steelblue;">Antecedentes medicos:</h3>

                <!--Aca estaria la tabla de antecedentes medicos-->
            </div>

            {#if loading}
                <!---->
                <div class="row g-2 justify-content-center">
                    <p
                        class="text-center col-lg-2 col-md-2 col-sm-2 col-12 col-xl-2"
                    >
                        Digita la cedula y dar clic en el boton de buscar...
                    </p>
                    <div
                        class="spinner-border col-lg-4 col-md-4 col-sm-4 col-12 col-xl-4"
                        role="status"
                    >
                        <span class="visually-hidden">Loading...</span>
                    </div>
                </div>
            {:else if error}
                <p class="text-red-500">Error: {error}</p>
            {:else}
                <div class="overflow-x-auto">
                    <table
                        class="min-w-full bg-white border border-gray-300"
                        id="myTable"
                    >
                        <thead>
                            <tr>
                                <th class="px-4 py-2 border"
                                    >Fecha del diagnosticos​</th
                                >
                                <th class="px-4 py-2 border">Sintomas</th>
                                <th class="px-4 py-2 border"
                                    >Descripcion del sintomas</th
                                >

                                <th class="px-4 py-2 border">Diagnostico</th>
                                <th class="px-4 py-2 border"
                                    >Descripcion del diagnostico</th
                                >
                                <th class="px-4 py-2 border"
                                    >Observacion/tratamiento</th
                                >
                            </tr>
                        </thead>

                        <tbody>
                            {#each todos2 as todo}
                                <tr class="hover:bg-gray-50">
                                    <td class="px-4 py-2 border"
                                        >{todo.fecha_diagnostico}</td
                                    >
                                    <td class="px-4 py-2 border"
                                        >{todo.sintomas}</td
                                    >
                                    <td class="px-4 py-2 border"
                                        >{todo.descripcion_sintomas}</td
                                    >

                                    <td class="px-4 py-2 border"
                                        >{todo.diagnostico}</td
                                    >
                                    <td class="px-4 py-2 border"
                                        >{todo.descripcion}</td
                                    >
                                    <td class="px-4 py-2 border"
                                        >{todo.Observaciontratamiento}</td
                                    >
                                </tr>
                            {/each}
                        </tbody>
                    </table>
                </div>
            {/if}
        </div>
        <!--Fin del body-->
        {#if comprobar}
            <div class="card-footer">
                <!--Aca comienza en footer-->
                <div class="text-center">
                    <button class="btn btn-outline-info" on:click={editar}
                        >Añadir historial medico</button
                    >
                </div>
            </div>
        {/if}
        <!--Aca termina el footer-->
    </div>
</div>

<div class=" fade" id="nav-listado">
    <div class="container pt-5">
        <div class="card">
            <div class="card-header text-center">
                <b>Historial clinico de <span class="" id="nombre_v"></span></b>
            </div>

            <div class="card-body" style="margin-left: 10%;">
                <div class="row">
                    <div class="col-lg-2">
                        <p class="card-text"><b>Sintomas:</b></p>
                    </div>

                    <div class="col-lg-10">
                        <input
                            type="text"
                            placeholder="sintomas del paciente"
                            id="sintomas"
                            
                            style="border: none; width: 55%;"
                            readonly
                        />
                    </div>
                </div>

                <div class="row pt-3">
                    <div class="col-lg-2">
                        <p class="card-text">
                            <b>Descripcion del/los sintoma/s</b>
                        </p>
                    </div>

                    <div class="col-lg-10">
                        <input
                            type="text"
                            placeholder="descripcion del sintoma del paciente"
                            id="descripcion_sintomas"
                            style="border: none; width: 55%;"
                            readonly
                        />
                    </div>
                </div>

                <div class="row pt-3">
                    <div class="col-lg-2">
                        <p class="card-text"><b>Diagnostico:</b></p>
                    </div>
                    <div class="col-lg-10">
                        <input
                            type="text"
                            id="diagnostico"
                            placeholder="diagnostico del usuario"
                            style="border: none; width: 55%;"
                            readonly
                        />
                    </div>
                </div>

                <div class="row pt-3">
                    <div class="col-lg-2">
                        <p class="card-text">
                            <b>Descripcion del diagnostico:</b>
                        </p>
                    </div>
                    <div class="col-lg-10">
                        <input
                            type="text"
                            id="descripcion_diagnostico"
                            placeholder="descripcion del diagnostico"
                           
                            style="border: none; width: 55%;"
                            readonly
                        />
                    </div>
                </div>

                <div class="row pt-3">
                    <div class="col-lg-2">
                        <p class="card-text">
                            <b>Observacion o tratamiento:</b>
                        </p>
                    </div>
                    <div class="col-lg-10">
                        <input
                            type="text"
                            placeholder="Observacion de tratamiento"
                            id="Observaciontratamiento"
                            style="border: none; width: 55%;"
                            readonly
                        />
                    </div>
                </div>

                <div class="row pt-3">
                    <div class="col-lg-2">
                        <p class="card-text">
                            <b>Seleccione la cita </b>
                        </p>
                    </div>
                    <div class="col-lg-10">
                        <select
                            id="citas"
                            class="form-select"
                            aria-label="Selecciona una cita"
                        >
                            <option value="">Selecciona una cita</option>
                            {#each citas as cita}
                                <option value={cita.id}>
                                    Fecha: {cita.fecha} - Hora: {cita.hora}
                                </option>
                            {/each}
                        </select>
                    </div>
                </div>

                <div class="row" style="margin-top: 4%;">
                    <div class="col-lg-9">
                        ¡Al terminar, darle click en guardara para guardar los
                        cambios!
                    </div>
                </div>
            </div>

            <div class="card-footer">
                <div class="text-center">
                    <button class="btn btn-outline-info" on:click={guardar}
                        >Guardar</button
                    >
                </div>
            </div>
        </div>
    </div>
</div>
