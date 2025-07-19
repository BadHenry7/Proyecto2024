<script>
    import Footer from "$lib/Footer.svelte";
import Navbarindex from "$lib/Navbarindex.svelte";
    import { onMount } from "svelte";

//  onMount(() => {
//     window.addEventListener('scroll', function () {

//     let animacion = document.getElementById('FondoSalud');
//     console.log(animacion)
//           if (!animacion) return;

//     let posicionObj1 = animacion.getBoundingClientRect().top;
//     console.log(posicionObj1)
//     let TamañoPantalla= window.innerHeight;
//     console.log("tamañopantalla", TamañoPantalla)

//     if (!animacion.classList.contains('animar') && posicionObj1 < TamañoPantalla) {
//         //animacion.style.animation='mover 1s ease-out'
//           animacion.classList.add('animar');
//         console.log("entra weon")
//     }
// })

//   });

</script>
<Navbarindex></Navbarindex>


<div class="container text-center mt-5">

    <b class=" fs-4">Tenemos asombrosos servicios que ofrecemos aca en Hostipal</b>
    <p>Contamos con herramientas para mejorar la gestion medica</p>
        
    <!--Cards-->
    <div class="row row-cols-1 row-cols-md-3 g-4  ">
        <div class="col ">
            <div class="card h-100 cartas">
            <img src="/MedicionAltura.png" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Medición de altura</h5>
                <p class="card-text"> Usamos tecnología con cámara y visión por computadora para estimar la altura del paciente de forma automática y sin contacto.</p>
            </div>
         
            </div>
        </div>
        <div class="col">
            <div class="card h-100 cartas ">
            <img src="/MedicionPresion.png" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Medición de la presión</h5>
                <p class="card-text">Monitoreamos la presión arterial, facilitando una atención médica preventiva y eficaz.</p>
            </div>
           
            </div>
        </div>
        <div class="col">
            <div class="card h-100 cartas">
            <img src="/MedicionPeso.png" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">Medición del peso</h5>
                <p class="card-text">  Registramos el peso del paciente de forma precisa para apoyar el seguimiento, control y la evaluación del estado general de salud.</p>
            </div>
         
            </div>
        </div>
    </div>
    <!--Fin de las cards-->
    
</div>
 

  <section style="view-timeline-name: --scroll; view-timeline-axis: block;">
<div class="" style="margin-top: 122px; "></div>
<div class="py-5" style="background-color: #e0e0e0;">
  <div class="container">
        <div class="row">
        <div class="col-xl-6">
            <img src="FondoSaludyBienestar.png" id="FondoSalud" alt="" class="img-fluid animar ">
        </div>
        <div class="col-xl-6"><!--d-flex align-items-center-->
                <h1 class="text-black text-center">Hacemos lo mejor para ti</h1>
                <h5 class="text-muted text-center ">
                    Tu bienestar es nuestra prioridad.  
                    Cada decisión, cada acción y cada servicio que ofrecemos  
                    está pensado para cuidar de ti y de los que más amas.  
                    Nos esforzamos día a día para brindarte atención médica  
                    de calidad, con empatía, respeto y compromiso.
                </h5>
                
                <div class="mx-3">
                    <div class="mt-5">
                        <i class="bi bi-rulers text-primary me-2"></i>
                        <b>Medición automática de altura</b><br>
                        <span class="text-muted small ms-4">Estimación sin contacto mediante visión por computadora.</span>
                    </div>
                    <div class="mb-3 mt-4 ">
                        <i class="bi bi-heart-pulse text-danger me-2"></i>
                        <b>Control de presión arterial</b><br>
                        <span class="text-muted small ms-4">Monitoreo preventivo para una atención eficaz.</span>
                    </div>
                    <div class="mb-3 mt-4">
                        <i class="fas fa-weight text-success me-2"></i>
                        <b>Registro preciso de peso</b><br>
                        <span class="text-muted small ms-4">Seguimiento confiable del estado general del paciente.</span>
                    </div>
                    <div class="mb-3 mt-4">
                        <i class="bi bi-calendar-check text-info me-2"></i>
                        <b>Gestión de citas médicas</b><br>
                        <span class="text-muted small ms-4">Agenda, consulta y organiza tu atención desde cualquier lugar.</span>
                    </div>
                    </div>
        </div>
        
        </div>
        <!--Finn del row-->

  </div>
</div>

</section >
<div class="">
<p class="text-center fs-3 mt-5"><b>Conoce nuestro trabajo</b></p>
<p class="text-center text-muted">  Descubre cómo usamos tecnología para ayudarte a cuidar tu salud de forma más simple y efectiva.</p>
</div>

<section >
    <div class="container">
     <div class="row mt-2" style="view-timeline-name: --altura; view-timeline-axis: block;">
            <div
                class="col-lg-6 col-md-8 col-sm-4 col-6 col-xl-6 py-2 fs-4 mt-5 text-center scale-in-center"
            >
                <b class="letra_cambiar_color">Medición  de altura</b> <br>
             Medimos tu altura con solo ponerte frente a una cámara.  
            Sin contacto físico, sin esperas ni procedimientos incómodos.  
            Utilizamos tecnología de visión por computadora para obtener resultados precisos en segundos.  
            Esto nos permite agilizar la atención médica y ofrecerte una experiencia más moderna y segura.
            </div>
            <div class="col-lg-6 col-md-4 col-sm-8 col-6 col-xl-6">
                <img src="/AlturaMedicion.png" class="img-fluid scale-in-center " style="width: 550px; height: 400px;" alt="" />
            </div>
        </div>

        <div class="row mt-2 scale-in-hor-left" style="view-timeline-name: --pulso; view-timeline-axis: block;">
            <div class="col-lg-6 col-md-8 col-sm-4 col-6 col-xl-6 py-5 mt-2 img-fluid">
                <img src="/PulsoMedicion.png" class="img-fluid "  style="width: 550px; height: 400px;" alt="" />
            </div>
            <div class="col-lg-6 col-md-4 col-sm-8 col-6 col-xl-6 py-5  fs-4 text-center "style="margin-top: 72px"  >
             
                <b >Medición de la presión y el pulso</b> <br>

                    Usamos un tensiometro y un pulsioxímetro  para medir tu presión sin complicaciones.  
                    El sistema guarda los datos automáticamente, ayudando a los médicos a tomar decisiones más rápidas y precisas.
            </div>
        </div>

        <div class="row mt-2 scale-in-hor-right" style="view-timeline-name: --peso; view-timeline-axis: block;">
            <div class="col-lg-6 col-md-8 col-sm-4 col-6 col-xl-6 py-2  fs-4 text-center" style="margin-top: 72px;">
                <b>Medición del peso</b> <br>

              Registramos el peso del paciente utilizando una báscula digital conectada.  
    Los datos se envían automáticamente a la base de datos, asegurando precisión en los registros y agilizando la atención médica.
            </div>
            <div class="col-lg-6 col-md-4 col-sm-8 col-6 col-xl-6 mt-3" >
                <img src="/PesoMedicion.png" class="img-fluid" alt=""  style="width: 550px; height: 450px;"/>
            </div>
        </div>
    </div>
</section>



<style>
section{
    animation-timeline: --scroll;
}

    .cartas:hover{  
      transform: translateY(-10px); 
      box-shadow: 0 10px 15px rgba(0,0,0,0.2);
      background-color: #e0f7fa;
      
    }

    .cartas img{
            margin-top: 12px;
            width: 200px;
            height: 200px;
            display: block;
            margin-left: auto;
            margin-right: auto;

    }


    .animar {
    animation: mover 10s ease-out forwards;
      animation-timeline: --scroll;
    animation-range: entry  0% entry  100%;

}
    @keyframes mover{
        0%{
            transform: translateX(100%);
        }
           100% {
        transform: translateX(0);
        opacity: 1;
    }
    }

.letra_cambiar_color{
animation-name: color_letra;
  animation-duration: 4s;
     animation-timeline: --altura;
    animation-range: entry 0% entry  100%;
}

    
@keyframes slide-up {
  0% {
    transform: translateY(80px);
    opacity: 0;
  }
  100% {
    transform: translateY(0);
    opacity: 1;
  }
}


@keyframes color_letra {
  from {color: white}
  to {color: black}
}
    

.scale-in-center {
    animation: scale-in-center 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
    animation-timeline: --altura;
  animation-range: entry 0% entry 100%;
}

.scale-in-hor-left {
	animation: scale-in-hor-left 0.5s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
      animation-timeline: --pulso;
  animation-range: entry 0% entry 100%;
}

.scale-in-hor-right {
	animation: scale-in-hor-right 1s cubic-bezier(0.250, 0.460, 0.450, 0.940) both;
    animation-timeline: --peso;
    animation-range: entry  0% entry  100%;  
}




@keyframes scale-in-center {
  0% {
    transform: scale(0);
    opacity: 1;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}

@keyframes scale-in-hor-left {
  0% {
    transform: scaleX(0);
    transform-origin: 0% 0%;
    opacity: 1;
  }
  100% {
    transform: scaleX(1);
    transform-origin: 0% 0%;
    opacity: 1;
  }
}


@keyframes scale-in-hor-right {
  0% {
    transform: scaleX(0);
    transform-origin: 100% 100%;
    opacity: 1;
  }
  100% {
    transform: scaleX(1);
    transform-origin: 100% 100%;
    opacity: 1;
  }
}

</style>





<!-- <body class="bg-dark    ">
    <div class="container  text-dark  text-center">
        <div class=" text-start fs-3  text-dark text-center"><b>¡Salud y bienestar!</b></div>
        <hr>
        <div class="row">
            <div class="col-lg-6 col-6 col-md-6 col-sm-6 col-xl-6">
                <p>¡Bienvenido a nuestro sistema de asistencia médica con inteligencia artificial!</p>
                <p>Hemos desarrollado una red neuronal diseñada para apoyar a los médicos</p>
                <p>en la detección temprana de enfermedades básicas. Nuestro objetivo es mejorar la</p>
                <p>precisión y eficiencia en los diagnósticos, proporcionando una herramienta</p>
                <p>inteligente que complemente la experiencia médica y ayude a ofrecer una mejor</p>
                <p>atención a los pacientes.</p>
            </div>
            
            <div class="col-lg-6 col-6 col-md-6 col-sm-6 col-xl-6">
                <p>Nuestro equipo de expertos en inteligencia artificial y salud ha trabajado en</p>
                <p>el desarrollo de este sistema para facilitar la evaluación de síntomas y brindar</p>
                <p>apoyo en la toma de decisiones médicas. Si necesitas más información o tienes</p>
                <p>dudas, puedes contactarnos a través de:</p>
                <ul class="text-start text-dark">
                    <li>WhatsApp</li>
                    <li>Correo Electrónico</li>
                    <li>Teléfono</li>
                </ul>
            </div>
            
        </div>

        <div class="row">

            <div class="mt-5">
                <p>Nuestra tecnología utiliza algoritmos avanzados de aprendizaje automático para analizar</p>
                <p>síntomas y patrones de enfermedades comunes. A través de este enfoque innovador,</p>
                <p>buscamos reducir el margen de error en los diagnósticos y agilizar el proceso de atención.</p>
                <p>Si bien la inteligencia artificial no reemplaza la experiencia del médico, sí proporciona</p>
                <p>una segunda opinión confiable y basada en datos, ayudando a mejorar la calidad del servicio médico.</p>
                
            </div>

        </div>
    </div>
</body> -->

<br>
<br>
<Footer></Footer>