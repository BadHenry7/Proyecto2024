<script > 
    import Navbaradmin from "../../../lib/Navbaradmin.svelte";
    import { onMount } from "svelte";
    
   

    let todos = {};
    let loading = true;
    let error = null;
    let exportesModal;
    let opcion;
    let fecha_de = "";
    let fecha_hasta = "";

    onMount(async() => {
        try {
            console.log
            const response = await fetch(
                "http://127.0.0.1:8000/estadisticas_citas",);
            if (!response.ok) throw new Error("Error al cargar los datos");
            const data = await response.json();
            todos = data.resultado;
            console.log(todos);
            
            const vCantidad = [];
            const vDoctores = [];//
            for (let i = 0; i < todos.length; i++) {
            vCantidad.push(todos[i].citas);
            vDoctores.push(todos[i].doctor);
        }
        console.log("cantidad de citas", vCantidad)
        console.log("Nombre del doctor", vDoctores)
        
        var grafica4 = document.getElementById("grafica1").getContext("2d");
        var myChart = new Chart(grafica4, {
            type: "pie",
            data: {
                labels: vDoctores,
                datasets: [{
                    label: vDoctores,
                    data: vCantidad, // 
                    fill: true,
                    backgroundColor: ['rgba(85, 226, 251, 0.3)',//diamante
                        'rgba(238, 180, 2, 0.3)',//Gold
                        'rgba(145,145,145,0.3)',//medium
                        'rgba(255,255,255,0.4)'],//Plus
                    borderColor: 'rgb(0, 0, 0, 0.3)',
                    pointBackgroundColor: 'rgb(255, 99, 132)',
                    pointBorderColor: '#fff',
                    pointHoverBackgroundColor: '#fff',
                    pointHoverBorderColor: 'rgb(255, 99, 132)'
                }]
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
            console.log(error)
           
        } finally {
            loading = false;
        }
    
    });

    
</script>

<Navbaradmin></Navbaradmin>


<div style="background-image: url('/image9.png'); background-size: cover; background-position: center;height: 100vh; width: 100vw;">
<div class="container" >
    <div class="row">

      <div class="col-lg-6" id="g1">
        <canvas id="grafica1" style="width: 310px; height: 220px;" class="ps-5 pe-5 pt-3" data-bs-toggle="modal"
          data-bs-target="#RModal2" ></canvas>
      </div>

      <div class="col-lg-6 fs-1" id="g2">
        <br>
        <br>
        <br>
        
        <p>En esta vista veremos diferentes estadísticas, la estadística a continuación es un ejemplo de una las estadísticas que el administrador podrá consultar</p>
      </div>

      <div class="col-lg-6" id="g3">
        <canvas id="grafica3" style="width: 300px; height: 220px;" class="ps-5 pe-5 pt-3" data-bs-toggle="modal"
          data-bs-target="#RModal4"></canvas>
      </div>

      <div class="col-lg-6" id="g4">
        <canvas id="grafica4" style="width: 300px; height: 220px;" class="ps-5 pe-5 pt-3" data-bs-toggle="modal"
          data-bs-target="#RModal5"></canvas>
      </div>

    </div>
  </div>
  

</div>





<style>
   

   
</style>
