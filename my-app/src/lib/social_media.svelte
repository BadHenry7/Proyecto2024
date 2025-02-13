<div class="social-icons">
    <a href="https://www.facebook.com" class="facebook" target="_blank" aria-label="Icono de facebook"> 
        <i class="fab fa-facebook-f" id="facebook" style="font-size: 3em; color: white;"></i>
    </a>


    <a href="https://www.instagram.com" class="instagram" target="_blank" aria-label="Icono de instagram">
        <i
            class="fab fa-instagram"
            id="instagram"
            style="font-size: 3em; color:white;"
        ></i>
    </a>

    <a href="https://wa.me/qr/E6SCTXPOXHDBD1" class="whatsapp" target="_blank" aria-label="Icono de whats">
        <i
            class="fab fa-whatsapp"
            id="whatsapp"
            style="font-size: 3em; color: #white;"
        ></i>
    </a>
</div>

<style>
    .social-icons {
        position: fixed;
        right: -2%;
        top: 50%;
        transform: translateY(-50%);
        z-index: 1000;
    }

    .social-icons a {
        display: block;
        margin-bottom: 15px;
        padding: 15px;
        border: 3px solid black;
        border-radius: 50%;
        color: white;
        text-align: center;
        font-size: 12px;
        transition: all 0.5s ease; /* Añadir transición para suavizar el movimiento */
        position: relative;
    }

    .social-icons a.facebook {
        background-color: #127bbe;
    }
    .social-icons a.instagram {
        background: linear-gradient(rgb(250, 7, 230), rgb(249, 253, 12));
    }

    .social-icons a.whatsapp {
        background-color: #15dd0f;
    }
    
    .social-icons a:hover {
       transform: translateX(-22%); 
    }

    .social-icons a:hover {
        background: #000000;
    }

</style>