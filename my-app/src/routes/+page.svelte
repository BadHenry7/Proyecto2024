<script>
   import Footer from "../lib/Footer.svelte";
   import Carrusel from "../lib/Carrusel.svelte";
</script>

<div class="container">
   <div class="row">
      <div
         class=" col-xl-12 col-lg-12 col-md-12 col-sm-12 col-12 text-end mt-2 px-4"
         style="margin-left: 10%;"
      >
         <a href="Register" class="text-decoration-none btn btn-outline-dark"
            >Registrarse</a
         >

         <a href="Login" class="text-decoration-none btn btn-outline-dark"
            >Iniciar sesión</a
         >
      </div>
   </div>
</div>

<div class="container">
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


<Footer></Footer>

<!--<Login> </Login>-->
