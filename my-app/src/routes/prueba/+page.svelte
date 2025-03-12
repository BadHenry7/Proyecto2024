<script>
      import { onMount } from "svelte"; 
      
  let calendarElement;

onMount(() => {
  if (calendarElement) {
    new coreui.Calendar(calendarElement, {
      locale: "es-ES",
      calendars: 1,
      range: true
    });
  }
});
</script>


<link
rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
/>
<link
rel="stylesheet"
href="https://cdn.jsdelivr.net/npm/@coreui/coreui-pro@5.10.0/dist/css/coreui.min.css">

<div class="container-fluid mt-3">
    <div class="row gap-3">
        <!-- Sección de Citas Agendadas (Izquierda) -->
        <div class="col-md-7">
            <div id="Mostrarusuario">
                <div class="container p-3">
                    <h2 class="mb-3">Citas agendadas</h2>
                    {#if loading}
                        <p class="text-center">Cargando datos...</p>
                    {:else if error}
                        <p class="text-danger">Error: {error}</p>
                    {:else}
                        <div class="overflow-x-auto">
                            <table class="table table-bordered table-sm">
                                <thead class="table-dark">
                                    <tr>
                                        <th>Paciente</th>
                                        <th>Doctor</th>
                                        <th>Fecha</th>
                                        <th>Hora</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    {#each todos as todo}
                                        <tr>
                                            <td>{todo.paciente}</td>
                                            <td>{todo.medico}</td>
                                            <td>{todo.fecha}</td>
                                            <td>{todo.hora}</td>
                                        </tr>
                                    {/each}
                                </tbody>
                            </table>
                        </div>
                    {/if}
                </div>
            </div>
        </div>

        <!-- Sección de Reportes (Derecha) -->
        <div class="col-md-5 d-flex justify-content-start">
            <div class="card shadow-lg p-3" style="width: 100%; max-width: 400px; background: #f0f4f8; border-radius: 10px;">
                <h3 class="text-center mb-3 text-danger">Reportes</h3>

                <!-- Selector de Reporte -->
                <select class="form-select mb-2" id="opcion" required>
                    <option value="1">Citas registradas</option>
                    <option value="2">Diagnósticos de usuarios</option>
                    <option value="3">Usuarios que han tenido citas</option>
                </select>
                
                <!-- Calendario -->
                <div class="d-flex justify-content-center">
                    <div bind:this={calendarElement} class="border rounded p-2 bg-white calendar-container"></div>
                </div>    

                <!-- Botones --> 
                <div class="d-flex justify-content-end mt-2">
                    <button class="btn btn-success me-1">Generar</button>
                    <button class="btn btn-secondary">Enviar correo</button>
                </div>
            </div>
        </div>
    </div>
</div>


      