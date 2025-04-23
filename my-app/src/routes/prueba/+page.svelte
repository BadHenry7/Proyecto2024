<script>
  import { goto } from '$app/navigation';
  import { loginUser } from '../../stores/userStore'; // Importar la función del store

  let email = '';
  let password = '';
  let errorMessage = '';

  const login = async (event) => {
    event.preventDefault();

    try {
      const response = await fetch('http://localhost:8000/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
      });

      if (response.ok) {
        const data = await response.json();
        console.log("Datos recibidos del servidor:", data);

        // Verifica si la respuesta contiene los campos necesarios
        if (data.success && data.access_token) {
          // Guardar en el store y en localStorage
          loginUser({ email }, data.access_token); // 👈 ya no usamos name
          localStorage.setItem('authToken', data.access_token);

          const token = localStorage.getItem('authToken');
          if (!token) {
            errorMessage = 'Error al guardar el token en localStorage.';
            console.error(errorMessage);
            return;
          }

          console.log("Token guardado en localStorage:", token);

          // Redirigir al chatbot o la página indicada
          goto(data.redirect || '/chatbot');
        } else {
          errorMessage = data.message || "Error desconocido al iniciar sesión.";
        }
      } else {
        try {
          const error = await response.json();
          errorMessage = error.detail || 'Error al iniciar sesión';
        } catch {
          errorMessage = 'Error desconocido del servidor.';
        }
      }
    } catch (err) {
      errorMessage = 'Error al conectar con el servidor';
      console.error(err);
    }
  };
</script>


<section class="vh-100 d-flex align-items-center justify-content-center background-image">
  <div class="container">
    <div class="row d-flex justify-content-center align-items-center">
      <div class="col-md-6">
        <div class="card p-5 shadow-lg login-card text-center">
          <div class="card-body">
            <h2 class="fw-bold mb-4">BIENVENIDA COMUNIDAD DE BARRANQUILLA</h2>

            <div class="avatar">
              <img src="https://th.bing.com/th/id/R.9af632ca01d69ee5ece0cd1b9f1891fd?rik=nq4Az%2f542EN5xw&riu=http%3a%2f%2fportal.avipam.com.br%2fimagens%2fusers%2fAdobeStock_262765707.png&ehk=RJ56EwkHHgSgjM4yj8O2qz%2b2Ja4o6M3Wri8zsNDRCbs%3d&risl=&pid=ImgRaw&r=0" alt="User Avatar" class="avatar-img" />
            </div>

            <!-- Formulario principal -->
            <form on:submit={login}>
              <div class="mb-3">
                <input type="email" class="form-control form-control-lg" placeholder="Email" bind:value={email} required />
              </div>
              <div class="mb-3">
                <input type="password" class="form-control form-control-lg" placeholder="Password" bind:value={password} required />
              </div>

              <div class="g-recaptcha mb-3" data-sitekey="6LfRNgorAAAAAB7aqrTLg0otnOs6zYiT_qM2FPU1"></div>

              {#if errorMessage}
                <div class="error-message">{errorMessage}</div>
              {/if}

              <button type="submit" class="btn btn-primary w-100 mb-3">Login</button>
            </form>

            <!-- Botón para Google Login (redirección simple) -->
            <form method="post" action="?/OAuth2S">
              <button type="submit" class="btn btn-outline-light w-100 d-flex align-items-center justify-content-center google-btn">
                <img src="https://th.bing.com/th/id/OIP._YRByM7l5SCayIje5TRfuwHaHj?w=247&h=252&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2" alt="Google Logo" class="google-logo me-2" />
                Sign in with Google
              </button>
            </form>

            <p class="mt-3">
              <a href="#" class="text-primary">Forgot password?</a>
            </p>
            <p>
              Don't have an account? <a href="/signup" class="text-primary fw-bold">Sign Up</a>
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<style>
  .background-image {
    background: url('https://passporterapp.com/es/blog/wp-content/uploads/2022/07/que-hacer-en-Barranquilla.jpg') no-repeat center center/cover;
    height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .login-card {
    background: rgba(255, 255, 255, 0.923);
    border-radius: 20px;
    padding: 40px;
    animation: fadeIn 1s ease-in-out;
  }
  .avatar {
    margin-bottom: 20px;
  }
  .avatar-img {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    border: 3px solid #007bff;
  }
  .btn-outline-light {
    background: rgba(255, 255, 255, 0.2);
    color: rgb(94, 186, 94);
    border: none;
    font-weight: bold;
    transition: 0.3s;
  }
  .btn-outline-light:hover {
    background: rgb(74, 228, 102);
    color: black;
  }
  .google-btn {
    background: #fff;
    color: black;
    font-weight: bold;
  }
  .google-btn:hover {
    background: #55d04f;
  }
  .google-logo {
    width: 20px;
    height: 20px;
  }
  .error-message {
    color: red;
    font-size: 0.9em;
    margin-top: 10px;
  }
  @keyframes fadeIn {
    from { opacity: 0; transform: translateY(-10px); }
    to { opacity: 1; transform: translateY(0); }
  }
</style>