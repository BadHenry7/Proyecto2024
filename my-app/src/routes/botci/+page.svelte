<script>
    import Navbarmedico from "$lib/Navbarmedico.svelte";
    import { onMount } from "svelte";

    let sintomas = []; // Lista de síntomas obtenida del backend
    let seleccionados = []; // Lista de síntomas seleccionados
    let enfermedad = null; // Resultado de la predicción
    let filtro = ""; // Para la búsqueda en tiempo real
    let probabilidad=null;
    // Cargar los síntomas al montar el componente
    onMount(async () => {
        try {
            const res = await fetch("http://127.0.0.1:8000/sintomas");
            const data = await res.json();
            sintomas = [...data.sintomas]; 
        } catch (error) {
            console.error("Error al cargar los síntomas:", error);
        }
    });

    function mostrar(data) {
        // Swal.fire("Tiene  un " + probabilidad+" de probabilidad de tener "+enfermedad);
        let mensaje = "Resultados de predicción:\n";

    if (data.length >= 1) {
        mensaje += data[0].enfermedad + ": " + data[0].probabilidad + "\n";
    }
    if (data.length >= 2) {
        mensaje += data[1].enfermedad + ": " + data[1].probabilidad + "\n";
    }
    if (data.length >= 3) {
        mensaje += data[2].enfermedad + ": " + data[2].probabilidad + "\n";
    }

    Swal.fire(mensaje);
    }
    

    function manejarCambioCheckbox(e, sintoma) {
    if (e.target.checked) {
        if (!seleccionados.includes(sintoma)) {
            seleccionados = [...seleccionados, sintoma];
        }
       
    } else {
        quitarSintoma(sintoma);
    }
}

    async function predecir() {
        try {
            if (seleccionados.length<=3){
                Swal.fire({
                    title: "Síntomas insuficientes",
                    text: "Seleccione al menos 4 síntomas para predecir.",
                    icon: "warning",
                    showConfirmButton: false,
                    timer: 3500
                });
            return
        }
            const res = await fetch("http://127.0.0.1:8000/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ selected_symptoms: seleccionados }),
            });
            const data = await res.json();
            // enfermedad = data.enfermedad;
            // probabilidad= data.probabilidad;
            mostrar(data);
        } catch (error) {
            console.error("Error al predecir la enfermedad:", error);
        }
    }

    function quitarSintoma(sintoma) {
        seleccionados = seleccionados.filter((s) => s !== sintoma);
    }

    // Filtrar síntomas en tiempo real
    $: sintomasFiltrados = sintomas.filter((sintoma) =>
        sintoma.toLowerCase().includes(filtro.toLowerCase())
    );
</script>

<Navbarmedico />

<div class="container">
    <h1 class="text-center">Predicción de Enfermedades</h1>

    <div class="main-grid">
        <!-- Lista de síntomas -->
        <div class="sintomas-box">
            <input
                type="text"
                placeholder="Buscar síntomas..."
                bind:value={filtro}
                class="search-box"
            />

            <div class="sintomas-grid">
                {#if sintomasFiltrados.length > 0}
                    {#each sintomasFiltrados as sintoma}
                        <label class="sintoma-item">
                            <input
                                type="checkbox"
                                value={sintoma}
                                checked={seleccionados.includes(sintoma)}
                                on:change={(e) => manejarCambioCheckbox(e, sintoma)}
                            />
                            {sintoma}
                        </label>
                    {/each}
                {:else}
                    <p>No se encontraron síntomas</p>
                {/if}
            </div>
        </div>

        <!-- Síntomas seleccionados -->
        <div class="seleccionados-box">
            <h3>Síntomas Seleccionados</h3>
            <ul>
                {#each seleccionados as sintoma}
                    <div class="seleccionado-item">
                        {sintoma}
                        <button on:click={() => quitarSintoma(sintoma)}>❌</button>
                    </div>
                {/each}
            </ul>

            <button type="button" class="btn" on:click={predecir} disabled={seleccionados.length === 0}>
                Predecir
            </button>
        </div>
    </div>
</div>

<style>
.container {
    max-width: 1400px;
    margin: auto;
    padding: 30px;
}

.text-center {
    text-align: center;
    font-size: 2rem;
    margin-bottom: 20px;
}

.main-grid {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 30px;
}

.sintomas-box {
    border: 1px solid #e0e0e0;
    padding: 20px;
    border-radius: 8px;
    background: #fff;
}

.search-box {
    width: 100%;
    padding: 10px;
    margin-bottom: 15px;
    border: 1px solid #ccc;
    border-radius: 6px;
}

.sintomas-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    max-height: 500px;
    overflow-y: auto;
}

.sintoma-item {
    display: flex;
    align-items: center;
    gap: 8px;
    background: #f7f7f7;
    padding: 8px;
    border-radius: 6px;
    font-size: 0.95rem;
}

.seleccionados-box {
    border: 1px solid #e0e0e0;
    padding: 20px;
    border-radius: 8px;
    background: #fafafa;
}

.seleccionados-box h3 {
    margin-bottom: 15px;
    font-size: 1.2rem;
}

.seleccionado-item {
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: #e3f2fd;
    padding: 8px;
    margin-bottom: 8px;
    border-radius: 6px;
    margin-right: 29px;
}

.seleccionado-item button {
    background: none;
    border: none;
    color: #d32f2f;
    font-size: 1rem;
    cursor: pointer;
}

.btn {
    margin-top: 15px;
    padding: 12px 20px;
    width: 100%;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    font-weight: bold;
}

.btn:hover {
    background-color: #0056b3;
}

.btn:disabled {
    background-color: #ccc;
    cursor: not-allowed;
}
</style>




<!-- <script>

    import Navbarmedico from "$lib/Navbarmedico.svelte";



  import { onMount } from "svelte";

  let sintomas = []; // Lista de síntomas obtenida del backend
  let seleccionados = []; // Lista de síntomas seleccionados
  let enfermedad = null; // Resultado de la predicción

  // Cargar los síntomas al montar el componente
  onMount(async () => {
      try {
          const res = await fetch("http://127.0.0.1:8000/sintomas");
          const data = await res.json();
          sintomas = data.sintomas;
      } catch (error) {
          console.error("Error al cargar los síntomas:", error);
      }
  });

    function mostrar(){
        Swal.fire("Su enfermedad es "+enfermedad);
    }

  async function predecir() {
      try {
          console.log(seleccionados)
          const res = await fetch("http://127.0.0.1:8000/predict", {
              method: "POST",
              headers: { "Content-Type": "application/json" },
              body: JSON.stringify({ selected_symptoms: seleccionados }),
          });
          const data = await res.json();
          enfermedad = data.enfermedad;
          mostrar()
      } catch (error) {
          console.error("Error al predecir la enfermedad:", error);
      }
  }
</script>
<Navbarmedico></Navbarmedico>

<div class="container">
    <h1>Predicción de Enfermedades</h1>
    <p>Selecciona los síntomas que presentas:</p>

    <form>
    {#if sintomas.length > 0}
        {#each sintomas as sintoma}
            <div>
                <label>
                    <input type="checkbox" value={sintoma} bind:group={seleccionados} />
                    {sintoma}
                </label>
            </div>
        {/each}
        <button type="button" class="btn btn-primary"  style="margin-top: 2%;" on:click={predecir}>Predecir</button>
    {/if}
    </form>


</div> -->