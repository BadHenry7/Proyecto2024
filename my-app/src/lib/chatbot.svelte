<script>
    let error= null
   

    let mensaje = "";
    let mensajes = [];
    var a ={}
    var b={}
    

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
                    
                    // Agrega la respuesta del bot al chat
                    if (data.length > 0) {
                        mensajes = [...mensajes, { texto: data[0].text, emisor: "bot" }];
                    }
                } catch (e) {
                    console.error("Error:", e);
                }

                mensaje = "";
            }
</script>

<button class="btn btn-primary tonyo_select" type="button" data-bs-toggle="offcanvas" data-bs-target="#offcanvasRight" aria-controls="offcanvasRight">Tonio</button>

<div class="offcanvas offcanvas-end tonyo_body" data-bs-scroll="true" data-bs-backdrop="false" tabindex="-1" id="offcanvasRight" aria-labelledby="offcanvasRightLabel">
    <div class="offcanvas-header ">
        <h5 class="offcanvas-title" id="offcanvasRightLabel">Chatbox, tigre tony</h5>
        <button type="button" class="btn-close" data-bs-dismiss="offcanvas" aria-label="Close"></button>
    </div>
    <div class=" offcanvas-body" style="margin-bottom: 17%;">
        <div class="row">

            {#each mensajes as msg}
                <div class="mt-2 d-flex {msg.emisor === 'user' ? 'justify-content-end' : 'justify-content-start'}">
                    <div class="{msg.emisor === 'user' ? 'mensaje-user' : 'mensaje-bot'}">
                        {msg.texto}
                    </div>
                </div>
            {/each}        
        
        </div>   
    </div>
    <div class="input-group input-area px-2 py-2" style="background-color: aqua; " > 
        <input type="text" bind:value={mensaje} placeholder="Escribe tu mensaje aca" class="form-control" on:keydown={(e) => e.key === 'Enter' && enviar()} />
        
        <button on:click={enviar} class="btn border" aria-label="enviar">
            <i class="bi bi-send"></i>
        </button>
    </div>
</div>


<style>
    .tonyo_select {
        position: fixed;
        width: 80px;
        height: 40px;
        right: 1%;
        top: 40%;
        border-radius: 5px;
        transform: translateY(-50%);
        z-index: 1000;
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
        bottom: 10px;
        width: 90%;
    }
</style>