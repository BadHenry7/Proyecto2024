<script>
    import { onMount } from "svelte";
    import Footer from "$lib/Footer.svelte";

    onMount(() => {
        var map = L.map("map").setView([10.960658, -74.801816], 16);

        L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution:
                '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        }).addTo(map);


        L.marker([10.960658, -74.801816])
            .addTo(map)
            .bindPopup("A pretty CSS popup.<br> Easily customizable.")
            .openPopup();

        var marker = L.marker([10.960658, -74.801816]).addTo(map);
        var circle = L.circle([10.960658, -74.801816], {
            color: "red",
            fillColor: "#f03",
            fillOpacity: 0.5,
            radius: 50,
        }).addTo(map);   

        
        var marker2 = L.marker([10.962032, -74.794501]).addTo(map);
        var circle2 = L.circle([10.962032, -74.794501], {
            color: "red",
            fillColor: "#f03",
            fillOpacity: 0.5,
            radius: 50,
        }).addTo(map);   




        var polygon = L.polygon([
            [51.509, -0.08],
            [51.503, -0.06],
            [51.51, -0.047],
        ]).addTo(map);

        function onMapClick(e) {
        alert("You clicked the map at " + e.latlng);
    }

    map.on("click", onMapClick);

    });

    
</script>

<div class="container pt-4">
    <a class="btn btn-outline-info" href="/">volver</a>

    <p>Estas son las ubicaciones de los hospitales</p>

    <div id="map"></div>
</div>



<div style="margin-bottom: 200px;"></div>

<Footer></Footer>

<style>
    #map {
        height: 580px;
    }
</style>
