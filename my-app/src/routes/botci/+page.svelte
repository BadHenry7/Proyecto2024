<script>
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

  // Enviar los síntomas seleccionados al backend
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
      } catch (error) {
          console.error("Error al predecir la enfermedad:", error);
      }
  }
</script>

<h1>Predicción de Enfermedades</h1>
<p>Selecciona los síntomas que presentas:</p>

<!-- Formulario para seleccionar síntomas -->
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
      <button type="button" on:click={predecir}>Predecir</button>
  {/if}
</form>

<!-- Mostrar la enfermedad predicha -->
{#if enfermedad}
  <h2>Resultado:</h2>
  <p>La enfermedad predicha es: {enfermedad}</p>
{/if}

<style>
  h1 {
      color: #2c3e50;
  }
  form {
      margin: 1rem 0;
  }
  button {
      background-color: #3498db;
      color: white;
      border: none;
      padding: 0.5rem 1rem;
      cursor: pointer;
  }
  button:hover {
      background-color: #2980b9;
  }
</style>
