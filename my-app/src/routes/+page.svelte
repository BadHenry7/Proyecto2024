<script>
    import Footer from "../lib/Footer.svelte";
    import Navbarindex from "$lib/Navbarindex.svelte";
    import { onMount } from "svelte";
    import Carrusel from "$lib/Carrusel.svelte";
    import Slide from "$lib/slide.svelte";
    import SocialMedia from "$lib/social_media.svelte";
    

    
    
function redirigir() {
    const v_url = "/usuario/citas_usuario/crear_citas_vista_usuario"; 
    localStorage.setItem("Redirigir", v_url); 
    window.location.href = "/Login"; 
}

</script>

    <!-- Barra superior -->
  
   <Navbarindex></Navbarindex>
   <SocialMedia></SocialMedia>
   
   <Slide></Slide>
   

  <!-- Boton de reserva -->
  <div class="reserva">
    <div class="texto-reserva">
      <h3><b>Reserve su cita aquí</b></h3>
      <p><b>No pierdas más el tiempo, no dejes <br>pasar más el tiempo 
         la solución esta <br> aquí no esperes más.</b></p>
    </div>
    <button href="" class="btn btn-success" on:click={redirigir}> Reservar </button>

        
  </div>

  <!-- cartas ... -->
        <h1 style="text-align: center; margin-top: 5vh;
           font-family: poppins; color: #022a63;">
           Beneficios con nosotros
        </h1>

  <div class="cartas">

        <div class="card">
            <img src="/gestion.png" alt="">
            <h3 class="fs-5 mt-3">Gestión de citas médicas</h3>
            <p>Agenda y administra tus citas médicas de forma rápida y sencilla.</p>
        </div>

        <div class="card">
            <img src="/carta.png" alt="">
            <h3 class="fs-5 mt-3">Confirmación automática de tu cita</h3>
                <p>Recibe un correo con los detalles de tu cita médica inmediatamente después de agendarla.</p>
        </div>

        <div class="card">
            <img src="/detectar.png" alt="">
            <h3 class="fs-5 mt-3">Detección de enfermedades</h3>
            <p>Utilizamos redes neuronales para detectar enfermedades básicas y brindarte orientación.</p>
        </div>

        <div class="card">
            <img src="/tiempo.png" alt="">
            <h3 class="fs-5 mt-3" >Citas médicas sin largas esperas</h3>
            <p>Olvídate de las filas y agenda tu consulta en el horario que más te convenga.</p>
        </div>

  </div>
      <!-- Cartas de Logos -->
    <h1 style="text-align: center; margin-top: 5vh;
     font-family: poppins; color: #022a63;">
     Servicios e información
    </h1>

    <div class="logos">

        <div class="card-logo" id="icono-1">
        <img src="/tonyopng.png" alt="">
            <p>Chatbot</p>
        </div>

        <div class="card-logo" id="icono-2">
            <a href="/ubicaciones" class="btn"><img src="/ubicacion.png" alt="">
            <p>Ubicación</p>
            </a>    
        </div>

        <div class="card-logo" id="icono-3">
        <a href="/acerca_de" class="btn"><img src="/nosotros.png" alt=""></a>
            <p>Nosotros</p>
        </div>

        <div class="card-logo" id="icono-4">
        <a href="/salud"><img src="/salud.png" alt="/salud"></a>
            <p>Salud & Bienestar</p>
        </div>

  </div>


 
    <Footer></Footer>






<style>*{
font-family: Arial, Helvetica, sans-serif;
}

.cartas {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 50px;
      margin-top: 10vh;
      margin-bottom: 1vh;
      background-color: #9fc6ca09;
} 

.card {
      width: 310px;
      height: 310px;
      background-color: #fff;
      box-shadow: 0 10px 12px rgba(0,0,0,0.1);
      transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
      align-items: center;
      justify-content: center;
      text-align: center;
      padding:30px;
    }    

.card img{
  height: 100px;
  width: 100px;
}

.card:hover {
      transform: translateY(-10px); 
      box-shadow: 0 10px 15px rgba(0,0,0,0.2);
      background-color: #e0f7fa;
    }

@keyframes flotar {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
  100% { transform: translateY(0px); }
}

.card h3 {
      margin-bottom: 10px;
      color: #333;
      padding: 05px;
    }    

.card p {
      color: #666;
      padding: 0 10px;
      font-family: Comic sans-serif;
    }    

.reserva{
      justify-content: center;
      display: flex;
      gap: 50px;
      padding: 20vh;
      background-image: url(../../../../fondo2.png);
      background-attachment: fixed; 
      background-size: 50vh;
      position: relative;
      z-index: 1;
      clip-path: ellipse(100% 100% at 50% 1%);
    }

.reserva button{
  border-radius: 30%;
  width: 90px;
  height: 90px;
  animation: flotar 3s ease-in-out infinite;
  transition: transform 0.3s, box-shadow 0.3s;
}    

.texto-reserva p{
  color: #000000;
  font-family: Comic sans-serif;

}

.texto-reserva h3{
  color: rgb(164, 16, 16);
}

.logos{
  justify-content: center;
  display: flex;
  gap: 100px;
  background-image: url(../../../../fondo2.png);
  background-size: 50vh;
  background-attachment: fixed;
  padding: 8vh;
  z-index: 1;
}

.card-logo{
  padding: 5vh;
  justify-content: center;
  justify-items: center;
  border-radius: 60% 40% 40% 60% / 50% 60% 40% 50%; /* Forma orgánica */
  box-shadow: 0 10px 15px rgba(159, 94, 94, 0.504); /* Sombra */
}

.card-logo img{
  width: 70px;
  height: auto;
  justify-content: center;
  justify-items: center;
  animation: flotar 2s ease-in-out infinite;
  transition: transform 0.3s, box-shadow 0.3s;
}

#icono-1{
  background-color: rgb(188, 241, 241);
}

#icono-2{
  background-color: rgb(241, 191, 188);
}

#icono-3{
  background-color: rgb(241, 188, 240);
}

#icono-4{
  background-color: rgb(241, 221, 188);
}

.card-logo img:hover{

  transform: translateY(-5px);

}</style>


















<!--darkcyan
<div class="py-1" style="background-color:  white;  border-bottom: 1px solid black; border-color: blue; ">
   <div class="container">
      <div class="row g-2">
         <div class="col-xl-1 col-lg-2 col-md-2 col-sm-2 col-2 px-3 mb-2 mt-3" style="margin-left: 3%;">
            <image src="/logo_hostipal.png" style="width: 78px; height: 78px;"></image>
            
         </div>
         <div
            class=" col-xl-10  col-lg-10 col-md-10 col-sm-10 col-10 text-end py-4 px-4"
            style=""
         >
            <a href="Register" class="btn btn-light text-decoration-none mx-2" style="color: black;"
               >Registrarse</a
            >

            <a href="Login" class=" btn btn-light text-decoration-none mx-3" style="color: black;"
               >Iniciar sesión</a>
         </div>
      </div>
   </div>
</div>

<div class="card text-center text-white mb-5" style="background: #70c8af;">Hostipal</div>

<Carrusel></Carrusel>
<SocialMedia></SocialMedia>



<div class="container mt-5">
   <div class="row mt-3">
      <div class="col-sm-4">
         <div class="card pt-3">
            <img src="/image4.png" class="card-img-top" alt="...">
            <div class="card-body">
               <h5 class="card-title">Gestión de Citas Eficiente</h5>
               <p class="card-text">Reserva y gestiona tus citas médicas de manera fácil y rápida. Nuestro sistema optimiza la disponibilidad de los especialistas, reduciendo tiempos de espera y asegurando una mejor atención para cada paciente.</p>
               <p>Agenda tu cita sin preocupaciones y una interfaz intuitiva.</p>
      
            </div>
         </div>
      </div>
      <div class="col-sm-4">
      <div class="card py-4">
         <img src="/image5.png" class="card-img-top" alt="...">

         <div class="card-body">
            <h5 class="card-title">Seguridad y Privacidad</h5>
            <p class="card-text">La información de salud es delicada, por eso implementamos protocolos de seguridad avanzados para proteger los datos de nuestros usuarios. Con encriptación de extremo a extremo, garantizamos la confidencialidad y seguridad de cada diagnóstico y cita.
               Déjame saber si quieres ajustes o un enfoque diferente. </p>
         </div>
      </div>
      </div>


      <div class="col-sm-4">
         <div class="card pt-4 pb-5">
            <img src="/image6.png" class="card-img-top" alt="...">
   
            <div class="card-body">
               <h5 class="card-title">Diagnóstico Inteligente</h5>
               <p class="card-text">Nuestra plataforma utiliza inteligencia artificial avanzada para detectar patrones en los síntomas y ofrecer una evaluación preliminar en segundos. Gracias a nuestra red neuronal, obtenemos análisis precisos que ayudan a los médicos a tomar decisiones informadas rápidamente.</p>
              
            </div>
         </div>
         </div>

   </div>
</div>
<style>
  .background {
    position: fixed; /* Fija el fondo en la pantalla */
    top: 0;
    left: 0;
    width: 100vw; /* Ancho total de la ventana */
    height: 100vh; /* Altura total de la ventana */
    background-image: url('/image.png');/* image7.png */
    background-size: cover; /* Cubre todo el espacio */
    background-position: center; /* Centra la imagen */
    background-repeat: no-repeat; /* Evita que se repita */
    z-index: -1; /* Coloca el fondo detrás del contenido */
  }
</style>

<div class="background"></div>

 Contenido del componente aquí


<br><br><br><br><b></b>



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
      </div
   </div>
   </div>
</div>




<Footer></Footer>


-->