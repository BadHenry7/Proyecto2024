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
            sintomas = [...data.sintomas]; // SOLUCIÓN: Forzar actualización en Svelte
        } catch (error) {
            console.error("Error al cargar los síntomas:", error);
        }
    });

    function mostrar() {
        Swal.fire("Tiene  un " + probabilidad+" de probabilidad de tener "+enfermedad);
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
                    title: "Error!",
                    text: "Por favor seleccione mas de 3 sintomas",
                    icon: "info",
                    confirmButtonText: "Cool",
                });
            return
        }
            const res = await fetch("http://127.0.0.1:8000/predict", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ selected_symptoms: seleccionados }),
            });
            const data = await res.json();
            enfermedad = data.enfermedad;
            probabilidad= data.probabilidad;
            mostrar();
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

    <div class="grid">
        <!-- Izquierda: Lista de síntomas -->
        <div class="sintomas-box">
            <input
                type="text"
                placeholder="Buscar síntomas..."
                bind:value={filtro}
                class="search-box"
            />

            <div class="sintomas-list">
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

        <!-- Derecha: Síntomas seleccionados -->
        <div class="seleccionados-box">
            <h3>Síntomas Seleccionados</h3>
            <ul>
                {#each seleccionados as sintoma}
                    <li class="seleccionado-item">
                        {sintoma}
                        <button on:click={() => quitarSintoma(sintoma)}>❌</button>
                    </li>
                {/each}
            </ul>

            <button type="button" class="btn" on:click={predecir} disabled={seleccionados.length ===0}>
                Predecir
            </button>
        </div>
    </div>
</div>

<style>
    

    .grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 20px;
        margin-top: 20px;
    }

    .sintomas-box, .seleccionados-box {
        border: 1px solid #ddd;
        padding: 10px;
        border-radius: 5px;
        background: #f9f9f9;
    }

    .search-box {
        width: 100%;
        padding: 8px;
        margin-bottom: 10px;
        border: 1px solid #ccc;
        border-radius: 5px;
    }

    .sintomas-list {
        max-height: 500px;
        overflow-y: auto;
        padding: 5px;
    }

    .sintoma-item {
        display: flex;
        align-items: center;
        padding: 5px;
        border-bottom: 1px solid #ddd;
    }

    .seleccionados-box h3 {
        margin-bottom: 10px;
    }

    .seleccionado-item {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px;
        border-bottom: 1px solid #ddd;
    }

    .seleccionado-item button {
        background: none;
        border: none;
        cursor: pointer;
        font-size: 14px;
        color: red;
    }

    .btn {
        margin-top: 10px;
        padding: 10px 15px;
        border: none;
        border-radius: 5px;
        background: #007bff;
        color: white;
        cursor: pointer;
        width: 100%;
    }

    .btn:hover {
        background: #0056b3;
    }

    .btn:disabled {
        background: #ccc;
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