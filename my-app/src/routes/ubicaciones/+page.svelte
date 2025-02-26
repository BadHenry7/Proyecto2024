<script>
    import { onMount } from "svelte";
    import Footer from "$lib/Footer.svelte";
    import Navbarindex from "$lib/Navbarindex.svelte";

    onMount(() => {
        var map = L.map("map").setView([10.960658, -74.801816], 16);

        L.tileLayer("https://tile.openstreetmap.org/{z}/{x}/{y}.png", {
            attribution:
                '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
        }).addTo(map);


     

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

        L.marker([10.960658, -74.801816])
            .addTo(map)
            .bindPopup("Hospital Nazareth")
            .openPopup();


        L.marker([10.962032, -74.794501])
        .addTo(map)
        .bindPopup("Paso la 21")
        


        // function onMapClick(e) {
        // alert("Ubicacion " + e.latlng);
        //  }

    map.on("click", onMapClick);

    });

    
</script>
<Navbarindex></Navbarindex>





<div class="container pt-4">
    <div class=" text-start fs-3  text-dark text-center"><b>¡Ubicaciones!</b></div>
    <hr>
   

    <!--<p class="fs-4">Estas son las ubicaciones de los hospitales</p>-->
    

    <div id="map"></div>
</div>



<div style="margin-bottom: 30px;"></div>

<Footer></Footer>

<style>
    #map {
        height: 580px;
    }
</style>
