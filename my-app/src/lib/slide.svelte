<script>
  import { fade, fly } from 'svelte/transition';
  import { cubicOut } from 'svelte/easing';
  
  // Datos de ejemplo para el carrusel
  let slides = [
    {
      image: '/GestionMedica.jpg',
      caption: 'Accede a todos tus antecedentes médicos en un solo lugar de manera segura..'
    },
    {
      image: '/Citas.png',
      caption: 'Obtén una evaluación de nuestros especialistas para mayor tranquilidad.'
    },
    {
      image: '/Cerebro.jpg',
      caption: 'Nuestra IA mejora constantemente para brindarte diagnósticos cada vez más precisos..'
    }
  ];
  
  // Índice del slide actual
  let currentIndex = 0;
  
  // Función para ir al siguiente slide
  function nextSlide() {
    currentIndex = (currentIndex + 1) % slides.length;
  }
  
  // Función para ir al slide anterior
  function prevSlide() {
    currentIndex = (currentIndex - 1 + slides.length) % slides.length;
  }
  
  // Función para obtener el índice del siguiente slide
  function getNextIndex(index) {
    return (index + 1) % slides.length;
  }
  
  // Función para obtener el índice del slide anterior
  function getPrevIndex(index) {
    return (index - 1 + slides.length) % slides.length;
  }
  
  // Configurar un intervalo para cambiar automáticamente los slides
  let interval;
  
  function startAutoplay() {
    interval = setInterval(nextSlide, 5000); // Cambiar cada 5 segundos
  }
  
  function stopAutoplay() {
    clearInterval(interval);
  }
  
  // Iniciar el autoplay cuando se monta el componente
  import { onMount, onDestroy } from 'svelte';
  
  onMount(() => {
    startAutoplay();
  });
  
  onDestroy(() => {
    stopAutoplay();
  });
</script>

<div class="carousel-container"  role="presentation"
     on:mouseenter={stopAutoplay} 
     on:mouseleave={startAutoplay} style="background-image: url(../../../../fondo2.png);   background-size: 50vh;" >
  
  <div class="carousel">
    <div class="slides-wrapper">
      <!-- Slide anterior (previsualización) -->
      <div class="slide-card prev-card" on:click={prevSlide}  role="presentation">
        <div class="card-inner">
          <img src={slides[getPrevIndex(currentIndex)].image || "/placeholder.svg"} alt="Slide anterior" />
          <div class="preview-caption">
            {slides[getPrevIndex(currentIndex)].caption}
          </div>
        </div>
      </div>
      
      <!-- Slide actual (principal) -->
      {#key currentIndex}
        <div class="slide-card main-card" transition:fade={{ duration: 300 }}>
          <div class="card-inner">
            <img src={slides[currentIndex].image || "/placeholder.svg"} alt="Slide actual" />
            <div class="caption" transition:fly={{ y: 20, duration: 300, easing: cubicOut }}>
              {slides[currentIndex].caption}
            </div>
          </div>
        </div>
      {/key}
      
      <!-- Siguiente slide (previsualización) -->
      <div class="slide-card next-card" on:click={nextSlide}  role="presentation">
        <div class="card-inner">
          <img src={slides[getNextIndex(currentIndex)].image || "/placeholder.svg"} alt="Siguiente slide" />
          <div class="preview-caption">
            {slides[getNextIndex(currentIndex)].caption}
          </div>
        </div>
      </div>
    </div>
    
    <button class="nav-button prev" on:click={prevSlide} >
      &lt;
    </button>
    <button class="nav-button next" on:click={nextSlide}>
      &gt;
    </button>
  </div>
  
  <div class="indicators">
    {#each slides as _, i}
      <button aria-label="indicators"
        class="indicator {i === currentIndex ? 'active' : ''}" 
        on:click={() => currentIndex = i}
      ></button>
    {/each}
  </div>
</div>

<style>
  .carousel-container {
    max-width: 10000px;
    margin: 0 auto;
    padding: 20px 0;
    position: relative;
  }
  
  .carousel {
    position: relative;
    overflow: hidden;
  }
  
  .slides-wrapper {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    padding: 20px 60px;
  }
  
  .slide-card {
    border-radius: 12px;
    overflow: hidden;
    transition: all 0.3s ease;
    cursor: pointer;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }
  
  .card-inner {
    position: relative;
    overflow: hidden;
  }
  
  .main-card {
    width: 60%;
    z-index: 3;
    transform: scale(1);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.15);
  }
  
  .prev-card, .next-card {
    width: 30%;
    z-index: 2;
    transform: scale(0.85);
    opacity: 0.7;
    filter: brightness(0.8);
  }
  
  .prev-card:hover, .next-card:hover {
    opacity: 0.9;
    transform: scale(0.9);
  }
  
  img {
    width: 100%;
    height: auto;
    display: block;
  }
  
  .caption {
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 12px;
    text-align: center;
    font-size: 1rem;
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
  }
  
  .preview-caption {
    background-color: rgba(0, 0, 0, 0.7);
    color: white;
    padding: 8px;
    text-align: center;
    font-size: 0.8rem;
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  .nav-button {
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    background-color: rgba(255, 255, 255, 0.7);
    border: none;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    font-size: 1.5rem;
    display: none;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background-color 0.3s;
    z-index: 4;
  }
  
  .nav-button:hover {
    background-color: rgba(255, 255, 255, 0.9);
  }
  
  .prev {
    left: 10px;
  }
  
  .next {
    right: 10px;
  }
  
  .indicators {
    display: flex;
    justify-content: center;
    margin-top: 15px;
    gap: 10px;
  }
  
  .indicator {
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background-color: #ccc;
    border: none;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  
  .indicator.active {
    background-color: #05b9fb;
  }
  
  @media (max-width: 768px) {
    .slides-wrapper {
      padding: 10px 40px;
      gap: 10px;
    }
    
    .main-card {
      width: 70%;
    }
    
    .prev-card, .next-card {
      width: 25%;
    }
    
    .caption {
      padding: 8px;
      font-size: 0.9rem;
    }
    
    .preview-caption {
      padding: 6px;
      font-size: 0.7rem;
    }
  }
  
  @media (max-width: 480px) {
    .prev-card, .next-card {
      display: none;
    }
    
    .main-card {
      width: 90%;
    }
  }
</style>