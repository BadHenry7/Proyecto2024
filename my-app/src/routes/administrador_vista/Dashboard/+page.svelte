<script>
    // MONTHNAME() PARA DEVOLVER EL NOMBRE DEL MES  y yearname el año
    import Navbaradmin from "../../../lib/Navbaradmin.svelte";
    import { onMount } from "svelte";

    let todos = {};
    let loading = true;
    let error = null;
    let exportesModal;
    let opcion = "";
    let fecha_de = "";
    let fecha_hasta = "";

    onMount(async () => {
        grafica2_citas();
        grafica3_citas_activas();
        grafica4_promedio_citas();

        try {
            console.log;
            const response = await fetch(
                "http://127.0.0.1:8000/estadisticas_citas",
            );
            if (!response.ok) throw new Error("Error al cargar los datos");
            const data = await response.json();
            todos = data.resultado;
            console.log(todos);

            const vCantidad = [];
            const vDoctores = []; //
            for (let i = 0; i < todos.length; i++) {
                vCantidad.push(todos[i].citas);
                vDoctores.push(todos[i].doctor);
            }
            console.log("cantidad de citas", vCantidad);
            console.log("Nombre del doctor", vDoctores);

            var grafica = document.getElementById("grafica1").getContext("2d");
            var myChart = new Chart(grafica, {
                type: "pie",
                data: {
                    labels: vDoctores,
                    datasets: [
                        {
                            label: vDoctores,
                            data: vCantidad, //
                            fill: true,
                            backgroundColor: [
                                "rgba(85, 226, 251, 0.3)", //diamante
                                "rgba(238, 180, 2, 0.3)", //Gold
                                "rgba(145,145,145,0.3)", //medium
                                "rgba(255,255,255,0.4)",
                            ], //Plus
                            borderColor: "rgb(0, 0, 0, 0.3)",
                            pointBackgroundColor: "rgb(255, 99, 132)",
                            pointBorderColor: "#fff",
                            pointHoverBackgroundColor: "#fff",
                            pointHoverBorderColor: "rgb(255, 99, 132)",
                        },
                    ],
                },
                options: {
                    plugins: {
                        legend: {
                            display: true,
                            position: "right",
                        },
                    },
                    title: {
                        display: true,
                        text: "Cantidad de pacientes asignados ",
                        position: "top",
                    },
                },
                //
            });
        } catch (e) {
            error = e.message;
            console.log(error);
        } finally {
            loading = false;
        }
    });

    let myChart2;
    let myChart3;
    let myChart4;

    let mygrafica_activas;
    let mygrafica_noactivas;

    let my_AVG_citas;
 
    async function grafica2_citas() {
        if (myChart2) {
            console.log("revisando el mychart2", myChart2);
            myChart2.destroy();
        }
        if (myChart3) {
            console.log("revisando el mychart3" + myChart3);
            myChart3.destroy();
        }
        if (myChart4) {
            console.log("revisando el mychart4" + myChart4);
            myChart4.destroy();
        }
        opcion = document.getElementById("opcion").value;
        if (opcion == "dia") {
            console.log("opcion seleccionada aca: " + opcion);
            try {
                console.log;
                const response = await fetch(
                    "http://127.0.0.1:8000/estadisticas2_citas",
                );
                if (!response.ok) throw new Error("Error al cargar los datos");
                const data = await response.json();
                todos = data.resultado;
                console.log(todos);

                const vCantidad = [];
                const vFecha = []; //
                for (let i = 0; i < todos.length; i++) {
                    vCantidad.push(todos[i].citas_dia);
                    vFecha.push(todos[i].Fecha);
                }
                console.log("cantidad de citas", vCantidad);
                console.log("Fecha de la cita", vFecha);

                var grafica2 = document
                    .getElementById("grafica2")
                    .getContext("2d");
                myChart2 = new Chart(grafica2, {
                    type: "bar",
                    data: {
                        labels: vFecha,
                        datasets: [
                            {
                                label: "Cantidad de citas",
                                data: vCantidad, //
                                fill: true,
                                backgroundColor: [
                                    "rgba(85, 226, 251, 0.3)", //diamante
                                    "rgba(238, 180, 2, 0.3)", //Gold
                                    "rgba(145,145,145,0.3)", //medium
                                    "rgba(255,145,255,0.4)",
                                ], //Plus
                                borderColor: "rgb(0, 0, 0, 0.3)",
                                borderWidth: 1,
                                pointBackgroundColor: "rgb(255, 99, 132)",
                                pointBorderColor: "#fff",
                                pointHoverBackgroundColor: "#fff",
                                pointHoverBorderColor: "rgb(255, 99, 132)",
                            },
                        ],
                    },
                    options: {
                        interaction: {
                            mode: null, // Desactiva completamente cualquier interacción
                        },
                        plugins: {
                            legend: {
                                display: true,
                                position: "right",
                            },
                        },
                        title: {
                            display: true,
                            text: "Cantidad de citas asignados ",
                            position: "top",
                        },
                    },
                    //
                });
            } catch (e) {
                error = e.message;
                console.log(error);
            } finally {
                loading = false;
            }
        } else if (opcion == "mes") {
            console.log("opcion seleccionada aca: " + opcion);

            try {
                console.log;
                const response = await fetch(
                    "http://127.0.0.1:8000/estadisticas3_citas",
                );
                if (!response.ok) throw new Error("Error al cargar los datos");
                const data = await response.json();
                todos = data.resultado;
                console.log(todos);

                const vCantidad = [];
                const vFecha = []; //
                for (let i = 0; i < todos.length; i++) {
                    vCantidad.push(todos[i].citas_mes);
                    vFecha.push("Mes: " + todos[i].Fecha);
                }
                console.log("cantidad de citas", vCantidad);
                console.log("Fecha de la cita", vFecha);

                var grafica3 = document
                    .getElementById("grafica2")
                    .getContext("2d");
                myChart3 = new Chart(grafica3, {
                    type: "bar",
                    data: {
                        labels: vFecha,
                        datasets: [
                            {
                                label: "Cantidad de citas",
                                data: vCantidad, //
                                fill: true,
                                backgroundColor: [
                                    "rgba(85, 226, 251, 0.3)", //diamante
                                    "rgba(238, 180, 2, 0.3)", //Gold
                                    "rgba(145,145,145,0.3)", //medium
                                    "rgba(255,145,255,0.4)",
                                ], //Plus
                                borderColor: "rgb(0, 0, 0, 0.3)",
                                borderWidth: 1,
                                pointBackgroundColor: "rgb(255, 99, 132)",
                                pointBorderColor: "#fff",
                                pointHoverBackgroundColor: "#fff",
                                pointHoverBorderColor: "rgb(255, 99, 132)",
                            },
                        ],
                    },
                    options: {
                        interaction: {
                            mode: null, // Desactiva completamente cualquier interacción
                        },
                        plugins: {
                            legend: {
                                display: true,
                                position: "right",
                            },
                        },
                        title: {
                            display: true,
                            text: "Cantidad de citas asignadas ",
                            position: "top",
                        },
                    },
                    //
                });
            } catch (e) {
                error = e.message;
                console.log(error);
            } finally {
                loading = false;
            }
        } else {
            console.log("opcion seleccionada aca: " + opcion);

            try {
                console.log;
                const response = await fetch(
                    "http://127.0.0.1:8000/estadisticas4_citas",
                );
                if (!response.ok) throw new Error("Error al cargar los datos");
                const data = await response.json();
                todos = data.resultado;
                console.log(todos);

                const vCantidad = [];
                const vFecha = []; //
                for (let i = 0; i < todos.length; i++) {
                    vCantidad.push(todos[i].citas_year);
                    vFecha.push("año: " + todos[i].Fecha);
                }
                console.log("cantidad de citas", vCantidad);
                console.log("Fecha de la cita", vFecha);

                var grafica4 = document
                    .getElementById("grafica2")
                    .getContext("2d");
                myChart4 = new Chart(grafica4, {
                    type: "bar",
                    data: {
                        labels: vFecha,
                        datasets: [
                            {
                                label: "Cantidad de citas",
                                data: vCantidad, //
                                fill: true,
                                backgroundColor: [
                                    "rgba(85, 226, 251, 0.3)", //diamante
                                    "rgba(238, 180, 2, 0.3)", //Gold
                                    "rgba(145,145,145,0.3)", //medium
                                    "rgba(255,145,255,0.4)",
                                ], //Plus
                                borderColor: "rgb(0, 0, 0, 0.3)",
                                borderWidth: 1,
                                pointBackgroundColor: "rgb(255, 99, 132)",
                                pointBorderColor: "#fff",
                                pointHoverBackgroundColor: "#fff",
                                pointHoverBorderColor: "rgb(255, 99, 132)",
                            },
                        ],
                    },
                    options: {
                        interaction: {
                            mode: null, // Desactiva completamente cualquier interacción
                        },
                        plugins: {
                            legend: {
                                display: true,
                                position: "right",
                            },
                        },
                        title: {
                            display: true,
                            text: "Cantidad de citas asignadas ",
                            position: "top",
                        },
                    },
                    //
                });
            } catch (e) {
                error = e.message;
                console.log(error);
            } finally {
                loading = false;
            }
        }
    }

    async function grafica3_citas_activas() {
        console.log("queeeeeeeeeeeeeeeeeeeeeeeeee");
        if (mygrafica_activas) {
            console.log("revisando el mychart2" + mygrafica_activas);
            mygrafica_activas.destroy();
        }
        if (mygrafica_noactivas) {
            console.log("revisando el mychart3" + mygrafica_noactivas);
            mygrafica_noactivas.destroy();
        }
        let opcion2 = document.getElementById("opcion2").value;
        if (opcion2 == "activo") {
            console.log("opcion seleccionada aca: " + opcion2);
            try {
                console.log;
                const response = await fetch(
                    "http://127.0.0.1:8000/estadisticas_citas_activas",
                );
                if (!response.ok) throw new Error("Error al cargar los datos");
                const data = await response.json();
                todos = data.resultado;
                console.log("esta es activos", todos);

                const vCantidad = [];
                const vFecha = []; //
                for (let i = 0; i < todos.length; i++) {
                    vCantidad.push(todos[i].citas_mes);
                    vFecha.push(todos[i].Fecha);
                }
                console.log("cantidad de citas", vCantidad);
                console.log("Fecha de la cita", vFecha);

                var grafica_activas = document
                    .getElementById("grafica3")
                    .getContext("2d");
                mygrafica_activas = new Chart(grafica_activas, {
                    type: "bar",
                    data: {
                        labels: vFecha,
                        datasets: [
                            {
                                label: "Cantidad de citas",
                                data: vCantidad, //
                                fill: true,
                                backgroundColor: [
                                    "rgba(85, 226, 251, 0.3)", //diamante
                                    "rgba(238, 180, 2, 0.3)", //Gold
                                    "rgba(145,145,145,0.3)", //medium
                                    "rgba(255,145,255,0.4)",
                                ], //Plus
                                borderColor: "rgb(0, 0, 0, 0.3)",
                                borderWidth: 1,
                                pointBackgroundColor: "rgb(255, 99, 132)",
                                pointBorderColor: "#fff",
                                pointHoverBackgroundColor: "#fff",
                                pointHoverBorderColor: "rgb(255, 99, 132)",
                            },
                        ],
                    },
                    options: {
                        interaction: {
                            mode: null, // Desactiva completamente cualquier interacción
                        },
                        plugins: {
                            legend: {
                                display: true,
                                position: "right",
                            },
                        },
                        title: {
                            display: true,
                            text: "Cantidad de citas pendientes por meses ",
                            position: "top",
                        },
                    },
                    //
                });
            } catch (e) {
                error = e.message;
                console.log(error);
            } finally {
                loading = false;
            }
        } else if (opcion2 == "no_activo") {
            console.log("opcion seleccionada aca: " + opcion2);

            try {
                console.log;
                const response = await fetch(
                    "http://127.0.0.1:8000/estadisticas_citas_desactivado",
                );
                if (!response.ok) throw new Error("Error al cargar los datos");
                const data = await response.json();
                todos = data.resultado;
                console.log(todos);

                const vCantidad = [];
                const vFecha = []; //
                for (let i = 0; i < todos.length; i++) {
                    vCantidad.push(todos[i].citas_mes);
                    vFecha.push("Mes: " + todos[i].Fecha);
                }
                console.log("cantidad de citas", vCantidad);
                console.log("Fecha de la cita", vFecha);

                var grafica_noactivas = document
                    .getElementById("grafica3")
                    .getContext("2d");
                mygrafica_noactivas = new Chart(grafica_noactivas, {
                    type: "bar",
                    data: {
                        labels: vFecha,
                        datasets: [
                            {
                                label: "Cantidad de citas",
                                data: vCantidad, //
                                fill: true,
                                backgroundColor: [
                                    "rgba(85, 226, 251, 0.3)", //diamante
                                    "rgba(238, 180, 2, 0.3)", //Gold
                                    "rgba(145,145,145,0.3)", //medium
                                    "rgba(255,145,255,0.4)",
                                ], //Plus
                                borderColor: "rgb(0, 0, 0, 0.3)",
                                borderWidth: 1,
                                pointBackgroundColor: "rgb(255, 99, 132)",
                                pointBorderColor: "#fff",
                                pointHoverBackgroundColor: "#fff",
                                pointHoverBorderColor: "rgb(255, 99, 132)",
                            },
                        ],
                    },
                    options: {
                        interaction: {
                            mode: null, // Desactiva completamente cualquier interacción
                        },
                        plugins: {
                            legend: {
                                display: true,
                                position: "right",
                            },
                        },
                        title: {
                            display: true,
                            text: "Cantidad de citas realizadas por meses",
                            position: "top",
                        },
                    },
                    //
                });
            } catch (e) {
                error = e.message;
                console.log(error);
            } finally {
                loading = false;
            }
        }
    }

    async function grafica4_promedio_citas() {
        if (my_AVG_citas) {
            console.log(my_AVG_citas);
            my_AVG_citas.destroy();
        }
        console.log("PROMEDIO DE CITAS GRAFICAS1");
       

         fecha_de=document.getElementById('desde_citas').value;
         fecha_hasta=document.getElementById('hasta_citas').value;
        console.log("PROMEDIO DE CITAS GRAFICAS2");
        if (fecha_de==""){
            fecha_de = "2024-11-01";
            console.log(fecha_de)
            
        }if (fecha_hasta==""){
            fecha_hasta = "2024-12-30";
            console.log(fecha_hasta)
        }
        console.log(fecha_de)
        console.log(fecha_hasta)
       

        try {
            console.log;
            const response = await fetch(
                "http://127.0.0.1:8000/estadisticas_avg_citas",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        fecha: fecha_de,
                        fecha2: fecha_hasta,
                    }),
                },
            );
            if (!response.ok) throw new Error("Error al cargar los datos");
            const data = await response.json();
            console.log("AVG", data)
            todos = data.resultado;
            console.log("PROMEDIO DE CITAS GRAFICAS",todos);

            const vCantidad = [];
            const vFecha = []; //
            for (let i = 0; i < todos.length; i++) {
                vCantidad.push(todos[i].promedio_citas);
                vFecha.push(todos[i].mes);
            }
            console.log("cantidad de citas", vCantidad);
            console.log("Fecha de la cita", vFecha);

            var AVG_citas = document
                .getElementById("grafica4")
                .getContext("2d");
                my_AVG_citas = new Chart(AVG_citas, {
                type: "bar",
                data: {
                    labels: vFecha,
                    datasets: [
                        {
                            label: "Promedio de citas",
                            data: vCantidad, //
                            fill: true,
                            backgroundColor: [
                                "rgba(85, 226, 251, 0.3)", //diamante
                                "rgba(238, 180, 2, 0.3)", //Gold
                                "rgba(145,145,145,0.3)", //medium
                                "rgba(255,145,255,0.4)",
                            ], //Plus
                            borderColor: "rgb(0, 0, 0, 0.3)",
                            borderWidth: 1,
                            pointBackgroundColor: "rgb(255, 99, 132)",
                            pointBorderColor: "#fff",
                            pointHoverBackgroundColor: "#fff",
                            pointHoverBorderColor: "rgb(255, 99, 132)",
                        },
                    ],
                },
                options: {
                    interaction: {
                        mode: null, // Desactiva completamente cualquier interacción
                    },
                    plugins: {
                        legend: {
                            display: true,
                            position: "right",
                        },
                    },
                    title: {
                        display: true,
                        text: "Promedio de citas ",
                        position: "top",
                    },
                },
                //
            });
        } catch (e) {
            error = e.message;
            console.log(error);
        } finally {
            loading = false;
        }
    }
</script>

<Navbaradmin></Navbaradmin>
<div class="container">
<iframe title="PowerbiRedNeuronal" width="1000" height="500" src="https://app.powerbi.com/view?r=eyJrIjoiN2ZhNzVjYzMtZjhmZS00YzU0LTkzOTgtZTIxMjhhZDk4Y2NhIiwidCI6IjFlOWFhYmU4LTY3ZjgtNGYxYy1hMzI5LWE3NTRlOTI0OTlhZSIsImMiOjR9" frameborder="0" allowFullScreen="true"></iframe>
</div>
<!--<div style="">
    <div class="container">
        <div class="row">
            <div class="col-lg-6" id="g1">
                <canvas
                    id="grafica1"
                    style="width: 310px; height: 220px;"
                    class="ps-5 pe-5 pt-3"
                    data-bs-toggle="modal"
                    data-bs-target="#RModal2"
                ></canvas>
            </div>

            <div class="col-lg-6" id="g2">
                <div style="text-align: center; ">
                    <label for="">Seleccionar criterio:</label>
                    <select
                        id="opcion"
                        style="margin-top: 10px;"
                        on:change={grafica2_citas}
                    >
                        <option value="dia">Por Día</option>
                        <option value="mes">Por Mes</option>
                        <option value="año">Por Año</option>
                    </select>
                </div>

                <canvas
                    id="grafica2"
                    style="width: 310px; height: 220px;"
                    class="ps-5 pe-5 pt-3"
                    data-bs-toggle="modal"
                    data-bs-target="#RModal2"
                >
                </canvas>
            </div>

            <div class="col-lg-6 pt-4" id="g3">
                <div style="text-align: center; ">
                    <label for="">Seleccionar criterio:</label>
                    <select
                        id="opcion2"
                        style="margin-top: 10px;"
                        on:change={grafica3_citas_activas}
                    >
                        <option value="activo">Activas</option>
                        <option value="no_activo">No activas</option>
                    </select>
                </div>
                <canvas
                    id="grafica3"
                    style="width: 300px; height: 220px;"
                    class="ps-5 pe-5 pt-3"
                    data-bs-toggle="modal"
                    data-bs-target="#RModal4"
                ></canvas>
            </div>

            <div class="col-lg-6 pt-4" id="g4">
                <div style="text-align: center; ">
                    <label for="">Seleccionar rango de fecha:</label>

                    Desde:
                    <input
                        type="date"
                        name="citas"
                        id="desde_citas"
                        on:change={grafica4_promedio_citas}
                    />

                    Hasta:
                    <input
                        type="date"
                        name="citas"
                        id="hasta_citas"
                        on:change={grafica4_promedio_citas}
                    />
                </div>

                <canvas
                    id="grafica4"
                    style="width: 300px; height: 220px;"
                    class="ps-5 pe-5 pt-3"
                    data-bs-toggle="modal"
                    data-bs-target="#RModal5"
                ></canvas>
            </div>
        </div>
    </div>
</div>
-->

