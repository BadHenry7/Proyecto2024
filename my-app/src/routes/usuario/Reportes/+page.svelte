<script>
    import Navbarusuario from "../../../lib/Navbarusuario.svelte";

</script>

<Navbarusuario></Navbarusuario>

<div class="container">
    <div>
        <div class="text-center">
            <div class="pt-2 mt-1" >
                <p class="fs-3">Reportes</p>
                <p>Seleccione el reporte que desea generar:</p>
                <form class="mb-5">
                    <select class="mt-1" required>
                        <option value="1">Ultima cita medica</option>
                        <option value="2">Citas agendadas</option>
                    </select>
                </form>
                <button class="btn btn-success mt-1">Generar</button>
            </div>
        </div>
    </div>
</div>