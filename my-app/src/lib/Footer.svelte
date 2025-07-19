<footer class="footer">
  <div class="footer-top">
    <div class="contact-info"  style="margin-left: 300px;">
      <p><i class="fas fa-map-marker-alt"></i> <strong>Dirección</strong><br>
        Calle 45e # 20-114 Casa<br> Barranquilla / Colombia
      </p>
      <p><i class="fas fa-phone-alt"></i> <strong>Teléfonos</strong><br>605-3463168, 605-3173981</p>
      <p><i class="fas fa-comment-dots"></i> <strong>Quejas y Reclamos</strong><br>
        quejasyreclamoshostipal.com.co</p>
    </div>

    <div class="footer-links">
        <ul>
           <div><i class="fab fa-whatsapp" style="color: #4a90e2;"></i> WhatsApp: <br>302 2843231</div><br>
            <div><i class="fas fa-envelope" style="color:#4a90e2;"></i> Correo Electronico: <br>hostipalinc.github@gmail.com</div>
            
                
         

          <div class="py-4">
                    <p>
                        <strong>HOSTIPAL®</strong> <br> Todos los derechos reservados
                        2025
                    </p>
                </div>
        </ul>
        <ul>
            <li><a href="#">Oficina Virtual</a></li>
            <li><a href="#">Línea de Atención</a></li>
            <li><a href="#">Sedes</a></li>
             <li><a href="#">Privacidad de datos</a></li>
          <li><a href="#">Términos y condiciones</a></li>
        </ul>
    </div>
  </div>
        <div class="img" style="margin-left: 250px;">  
        <img src="/image_otro_logo.png" alt="" style="height: 100px; width: 300px;">
        </div>

  <div class="footer-bottom">
    <div class="social">
      <a href="#"><i class="fab fa-facebook-f"></i></a>
      <a href="#"><i class="fab fa-instagram"></i></a>
      <a href="#"><i class="fab fa-whatsapp"></i></a>
    </div>
    <p>2025 © Hostipal. Todos los derechos reservados</p>
  </div>
</footer>

<style>
.footer {
  font-family: 'Segoe UI', sans-serif;
  background-color: #fff;
  color: #00214d;
  padding: 40px 0px 0;
  border-top: 1px solid #ccc;
  background-image: url(../../../../fondootro.png);
  background-size: 50vh;
  background-attachment: fixed;
}

.footer-top {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  gap: 40px;
}

.contact-info {
  flex: 1;
  min-width: 250px;
  font-size: 15px;
}

.contact-info p {
  margin-bottom: 20px;
  line-height: 1.4;
}

.contact-info i {
  color: #4a90e2;
  font-size: 16px;
}

.footer-links {
  display: flex;
  flex: 3;
  justify-content: space-between;
  flex-wrap: wrap;
    padding: 0px 200px 0;
}

.footer-links ul {
  list-style: none;
  padding: 0;
  margin: 0;
  min-width: 180px;
}

.footer-links ul li {
  margin-bottom: 10px;
}

.footer-links ul li a {
  text-decoration: none;
  color: #00214d;
  font-size: 15px;
  position: relative;
}

.footer-links ul li a::before {
  content: '›';
  margin-right: 8px;
  color: #4a90e2;
}

.footer-links ul li a:hover {
  color: #4a90e2;
}

.footer-bottom {
  background-color: #80b4e3;
  color: white;
  margin-top: 40px;
  padding: 15px 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  border-radius: 10px 10px 0 0;
}

.footer-bottom .social a {
  color: white;
  margin-right: 20px;
  font-size: 18px;
  transition: transform 0.3s;
}

.footer-bottom .social a:hover {
  transform: scale(1.2);
  color: #00214d;
}

.footer-bottom p {
  margin: 0;
  font-size: 14px;
}

@keyframes flotar {
  0% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
  100% { transform: translateY(0px); }
}


img{
    animation: flotar 3s ease-in-out infinite;
    transition: transform 0.3s, box-shadow 0.3s;
}
</style>