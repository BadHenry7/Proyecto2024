<script>

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

    <!--{#if enfermedad}
    <h2>Resultado:</h2>
    <p>La enfermedad predicha es: {enfermedad}</p>
    {/if}-->
</div>