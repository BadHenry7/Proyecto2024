<script>
    let error= null
   

    let mensaje = "";
    let mensajes = [];
    var a ={}
    var b={}
    let loading=false
   
    async function enviar() {
                if (!mensaje.trim()) return;  
                mensajes = [...mensajes, { texto: mensaje, emisor: "user" }];
                
                try {
                    const response = await fetch("http://localhost:5005/webhooks/rest/webhook", {
                        method: "POST",
                        headers: {
                            "Content-Type": "application/json",
                        },
                        body: JSON.stringify({
                            sender: "2",
                            message: mensaje,
                        }),
                    });
                    const data = await response.json();
                    console.log("data toma",data)
                    loading=true
                                 
            
                    // Agrega la respuesta del bot al chat
                for (let i = 0; i < data.length; i++) {
                    setTimeout(() => {
                        loading = true;
                        // Muestra el loading antes de enviar el mensaje
                        console.log("Mostrando loading...");
                        
                        setTimeout(() => {
                            // Envía el mensaje después de un pequeño retraso
                            mensajes = [...mensajes, { texto: data[i].text, emisor: "bot",  image: data[i].image? data[i].image:null  }];
                            loading = false;
                            console.log("Mensaje enviado:", data[i].text);
                        }, 1000); // Esto simula que mientras loading es true, después de 1 segundo llega el mensaje

                    }, i * 3000); // Cada mensaje se envía con 3s de diferencia
                }


                } catch (e) {
                    console.error("Error:", e);
                }

                mensaje = "";
            }
</script>

<div class="" style="position: fixed;">
    <button class="btn btn-primary tonyo_select" ype="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">
    
        <i class="bi bi-chat-dots"></i>
        <span class="tonyo-text">Tonyo, asistente virtual</span>
    </button>

    <div class="offcanvas offcanvas-end tonyo_body" data-bs-scroll="true" data-bs-backdrop="false" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
        <div class="offcanvas-header bg-primary"  style="border-top-left-radius: 12px;   border-top-right-radius: 12px;"  >
            <img src="/tonyo2.png"  class="img-fluid" style="height: 55px;" alt="">
            <h2 class="offcanvas-title" id="offcanvasRightLabel " style="color: white;">hostipal</h2>
            <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
        </div>
        <div class=" offcanvas-body" style="margin-bottom: 17%;">
            <div class="row">

            

                {#each mensajes as msg}
                    <div class="mt-2 d-flex {msg.emisor === 'user' ? 'justify-content-end' : 'justify-content-start'}">
                        <div class="{msg.emisor === 'user' ? 'mensaje-user' : 'mensaje-bot'}">
                            {#if msg.texto}
                            {msg.texto}
                            {:else}
                            <img src={msg.image} 
                                class="img-fluid"  alt="">
                            
                            {/if}


                        </div>
                    </div>
                {/each}        
                {#if loading}
                <div class="typing-dots">
                    <span></span><span></span><span></span>
                </div>
                {/if}
            </div>   
        </div>
        
        <div class="offcanvas-footer text-black">
            <div class="input-group input-area px-2 py-2" > 
                <input type="text" bind:value={mensaje} placeholder="Escribe tu mensaje aca" class="form-control" on:keydown={(e) => e.key === 'Enter' && enviar()} />
                
                <button on:click={enviar} class=" border" aria-label="enviar" style="background-color: white;">
                    <i class="bi bi-send input-group-text" style="background-color: white; border: none;"></i>
                </button>
            </div>
        </div>
    </div>
 
</div>

<style>

.offcanvas-footer{
    padding: 2rem 2rem;
    border-top: 1px solid #2bff00;
    background-color: #007bff;
    
    border-bottom-left-radius: 12px;
    border-bottom-right-radius: 12px;
    
}

.offcanvas-footer input, button{
    border-radius: 100px;

}


    .tonyo_select {
        position: fixed;
        right: 1%;
        top: 40%;
        width: 70px;
        height: 50px;
        background-color: #007bff;
        border-radius: 50%;
        display: flex;
        justify-content: center;/* Alinea el contenido (texto o ícono) horizontalmente en el centro. */
        align-items: center;/*Alinea el contenido verticalmente en el centro.*/
        color: white;
        border: none;
        cursor: pointer;
        z-index: 1000;
        transition: width 0.5s ease;
    }

    .tonyo_select:hover {
        width: 150px;
        height: 70px;
        border-radius: 25px;
        justify-content: space-around;
        background-color: cornflowerblue;
    }

    .tonyo-text {
        display: none;
        color: white;
        font-size: 14px;
    }

    .tonyo_select:hover .tonyo-text {
        display: block;
    }

    
    .tonyo_body{
       margin-top: 100px;
       margin-bottom: 110px;
       margin-right: 10px;
       border-radius: 25px;
       
    }

    .input-area {
        position: absolute;
        padding-top: 5px;
        bottom: 4px;
        right: 22px;
        width: 90%;
       


    }

    



    .typing-dots {
        display: flex;
        justify-content: center;
        align-items: center;
        background: #f1f1f1;
        border-radius: 15px;
        width: 60px;
        height: 30px;
        box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.2);
    }
    
    .typing-dots span {
        width: 8px;
        height: 8px;
        margin: 0 3px;
        background-color: #3498db;
        border-radius: 50%;
        animation: typingAnimation 1.5s infinite;
    }
    
    .typing-dots span:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    .typing-dots span:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    @keyframes typingAnimation {
        0% { opacity: 0.3; transform: translateY(0px); }
        50% { opacity: 1; transform: translateY(-5px); }
        100% { opacity: 0.3; transform: translateY(0px); }
    }
</style>


    

