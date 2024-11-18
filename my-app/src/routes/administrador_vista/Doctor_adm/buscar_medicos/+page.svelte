<script>
    import Navbaradmi from "$lib/Navbaradmin.svelte";
    import { onMount } from "Svelte";

    let todos = {};
    let loading = true;
    let error = null;
</script>

<Navbaradmi></Navbaradmi>

<div id="Mostrardoctores">
    <div class="container py-4">
        <h2 class="">Lista de doctores</h2>
        {#if loading}
        <h2>Cargando datos...</h2>
        {:else if error}
        <p>Error{error}</p>
        {:else}
        

        {/if}

    </div>
</div>

<!--Hola-->
