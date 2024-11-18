<script>
   import Footer from "../lib/Footer.svelte";
   import Carrusel from "../lib/Carrusel.svelte";
</script>

<div class="py-3" style="background-color: darkcyan; border-style: solid; border-color: darkcyan;">
   <div class="row g-2">
      <div class="col-xl-1 col-lg-2 col-md-2 col-sm-2 col-2 px-3" style="margin-left: 3%;">
         <image src="/favicon.png"></image>
         <p style="font-style: italic; color:white;">Hostipal</p>
      </div>
      <div
         class=" col-xl-10  col-lg-10 col-md-10 col-sm-10 col-10 text-end py-4 px-4"
         style=""
      >
         <a href="Register" class="btn btn-light text-decoration-none mx-2" style="color: black;"
            >Registrarse</a
         >

         <a href="Login" class=" btn btn-light text-decoration-none mx-3" style="color: black;"
            >Iniciar sesión</a
         >
      </div>
   </div>
</div>

<div class="bg-info"> 
   <div class="row g-1" >
      <div class="container" style="background-image: url('/image7.png');background-size: cover;
       background-position: center;height: 100vh; width: 100vw;">
        <div class="row g-2 pt-2">
         <div class=" col-xl-6 col-lg-8 col-md-8 col-sm-6 col-6 fs-4 text-center px-5" style="margin-left: 2%; margin-top: 5%;">
            <h1 class="display-6">Quienes somos</h1>
            En Hostipal, estamos comprometidos con brindar a nuestros usuarios, una
            experiencia excepcional y ayudarlos con su salud y bienestar. Valoramos
            a nuestros usuarios, y es por eso que proporcionamos a los usuarios, una
            buena gestion y creemos que todos merecen la oportunidad de recibir atencion
            medica.
         </div>
         <div class=" col-xl-4 col-lg-6 col-md-8 col-sm-4 col-6 fs-4 text-center">
         </div>
      </div>
   </div>
   </div>
</div>



<!--<div class="container">
   <div class="row pt-2">
      <div class=" col-xl-4 col-lg-6 col-md-8 col-sm-4 col-6 fs-4 text-center">
         <h1 class="display-6">Quienes somos</h1>
         En Hostipal, estamos comprometidos con brindar a nuestros usuarios, una
         experiencia excepcional y ayudarlos con su salud y bienestar. Valoramos
         a nuestros usuarios, y es por eso que proporcionamos a los usuarios, una
         buena gestion y creemos que todos merecen la oportunidad de recibir atencion
         medica.
        
      </div>

      <div class=" col-xl-4 col-lg-6 col-md-8 col-sm-4 col-6 fs-4 text-center">
         <h1 class="display-6">Que hacemos</h1>
      </div>

      <div class=" col-xl-4 col-lg-6 col-md-8 col-sm-4 col-6 fs-4 text-center">
         <Carrusel></Carrusel>
      </div>
   </div>
</div>
-->

<Footer></Footer>

<!--<Login> </Login>-->
