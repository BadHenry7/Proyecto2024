<script>
    import Footer from "../lib/Footer.svelte";
    import Navbarindex from "$lib/Navbarindex.svelte";
    import { onMount } from "svelte";
    import Carrusel from "$lib/Carrusel.svelte";
    
    
function redirigir() {
    const v_url = "/usuario/citas_usuario/crear_citas_vista_usuario"; 
    localStorage.setItem("Redirigir", v_url); 
    window.location.href = "/Login"; 
}
</script>

<div class="bg-light">
    <!-- Barra superior -->
  
   <Navbarindex></Navbarindex>

    <!-- Hero Section
    <section class="position-relative">
        <img src="https://storage.googleapis.com/a1aa/image/-EpcjZIo-GJIVeM6HQyxj-5b0RwGBV3QBWsU2OnRX8Q.jpg" 
             class="w-100" 
             style="height: 200px; object-fit: cover;" 
             alt="Background Image">
        <div class="position-absolute top-0 start-0 w-100 h-100 d-flex align-items-center justify-content-center" 
             style="background: rgba(0, 0, 0, 0.5);">
            <div class="text-center text-white">
                <h1 class="fs-3 fw-bold">Clínica Médica</h1>
                <p class="fs-5">Examen y diagnóstico</p>
            </div>
        </div>
    </section>
     -->

<Carrusel></Carrusel>


    <!-- Sección de informacion -->
    <section class="container py-5">
        <div class="row g-4" >
            <div class="col-md-4"><!--bg-success 
                bg-success 
                bg-success "-->
                <div class="card text-white text-center p-4 bg-success" style="background: #B3DFFC;">
                    <h2 class="fs-4 fw-bold">Historial clinico digital para los pacientes</h2>
                    <p>Accede a todos tus antecedentes médicos en un solo lugar de manera segura..</p>
                    <button class="btn btn-light text-success">Leer más</button>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card text-white text-center p-4 bg-success" style="background: #B3DFFC;">
                    <h2 class="fs-4 fw-bold">Atención medica a los pacientes del centro medico</h2>
                    <p>Obtén una evaluación de nuestros especialistas para mayor tranquilidad.</p>
                    <button class="btn btn-light text-success">Leer más</button>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card text-white text-center p-4 bg-success" style="background: #B3DFFC;">
                    <h2 class="fs-4 fw-bold">Red neuronal como apoyo al medico</h2>
                    <p>Nuestra IA mejora constantemente para brindarte diagnósticos cada vez más precisos..</p>
                    <button class="btn btn-light text-success">Leer más</button>
                </div>
            </div>
        </div>
    </section>

    <!-- Sección de Citas -->
    <section class="text-white py-5 text-center" style="background-color: cornflowerblue;">
        <h2 class="fs-3 fw-bold">Agenda tu cita en línea</h2>
        <button class="btn btn-light text-primary mt-3" on:click={redirigir}>Reservar cita</button>
    </section>

    <!-- Sección de Facilitando tu atencion medica -->
    <section class="container text-center py-5">
        <h2 class="fs-3 text-success fw-bold">Facilitando tu atención médica</h2>
        <div class="row mt-4">
            <div class="col-md-4">
                <i class="fas fa-heartbeat text-success display-4"></i>
                <h3 class="fs-4 mt-3">Gestión de citas médicas</h3>
                <p>Agenda y administra tus citas médicas de forma rápida y sencilla.</p>
                
            </div>
            <div class="col-md-4">
                <i class="fas fa-envelope text-success display-4"></i>
                <h3 class="fs-4 mt-3">Confirmación automática de tu cita</h3>
                <p>Recibe un correo con los detalles de tu cita médica inmediatamente después de agendarla..</p>
                
            </div>
            <div class="col-md-4">
                <i class="fas fa-brain   text-success display-4"></i>
                <h3 class="fs-4 mt-3">Detección de enfermedades</h3>
                <p>Utilizamos redes neuronales para detectar enfermedades básicas y brindarte orientación.</p>
                
            </div>
        </div>
    </section>

 
    <section class="bg-light py-5 text-center">
        <i class="fas fa-clock text-success display-4"></i>
        <h3 class="fs-4 mt-3">Citas médicas sin largas esperas</h3>
        <p>Olvídate de las filas y agenda tu consulta en el horario que más te convenga.</p>
        
    </section>

    <!-- Footer -->
    <Footer></Footer>
</div>
























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