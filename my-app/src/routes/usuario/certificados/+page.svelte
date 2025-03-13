<script>
    import Navbarusuario from "$lib/Navbarusuario.svelte";
    import { onMount } from "svelte";

    function generarPDF() {
        const { jsPDF } = window.jspdf; 
        const doc = new jsPDF();
        // Título
        doc.setFont("helvetica", "bold");
        doc.setFontSize(18);
        doc.text("CERTIFICADO DE INCAPACIDAD MÉDICA", 20, 20);

        // Línea divisoria
        doc.setLineWidth(0.5);
        doc.line(20, 25, 190, 25);

        // Contenido
        doc.setFont("times", "normal");
        doc.setFontSize(12);
        doc.text("Estimado/a paciente,", 20, 40);
        doc.text(
            "Por medio del presente, le informamos que debido a su condición médica, se le ha otorgado una incapacidad médica de", 
            20, 50, { maxWidth: 170 }
        );
        doc.setFont("times", "bold");
        doc.text("7 días (1 semana)", 20, 60);
        doc.setFont("times", "normal");
        doc.text(
            "Durante este período, se recomienda reposo absoluto y el seguimiento de las indicaciones médicas brindadas.",
            20, 70, { maxWidth: 170 }
        );

        doc.text(
            "En caso de requerir una extensión de la incapacidad o presentar síntomas adicionales, le recomendamos acudir nuevamente a consulta médica.",
            20, 85, { maxWidth: 170 }
        );

        // Espacio para la firma
        doc.text("Atentamente,", 20, 120);
        doc.text("__________________________", 20, 135);
        doc.text("Dr. Adm", 20, 145);
        doc.text("Médico General", 20, 155);

        // Guardar PDF
        doc.save("Incapacidad_Medica.pdf");
    }
</script>
<style>
    .container {
        display: flex;
        justify-content: space-between;
        align-items: flex-start;
        padding: 40px;
        gap: 20px;
    }

    .left, .right {
        width: 25%;
        background: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }

    .center {
        width: 50%;
        background: #fff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
    }

    .full-width-card {
        margin-top: 20px;
        width: 100%;
        background: #f1f1f1;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        text-align: center;
    }

    h1 {
        color: #333;
        font-size: 24px;
        margin-bottom: 15px;
    }

    h2 {
        color: #007BFF;
        font-size: 20px;
        margin-bottom: 10px;
    }

    p {
        color: #555;
        font-size: 16px;
        line-height: 1.5;
    }

    .button {
        background: #007BFF;
        color: white;
        padding: 12px 24px;
        font-size: 18px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        margin-top: 20px;
        transition: background 0.3s ease;
    }

    .button:hover {
        background: #0056b3;
    }

    /* Diseño responsivo */
    @media (max-width: 768px) {
        .container {
            flex-direction: column;
            align-items: center;
        }

        .left, .right, .center {
            width: 100%;
            margin-bottom: 20px;
        }
    }
</style>

<Navbarusuario />

<!-- Tarjeta de recomendaciones médicas ocupando toda la pantalla -->
<div class="container">
    <div class="full-width-card bg-light">
        <h2>🔹 Recomendaciones Médicas Generales 🔹</h2>
        <p>Para garantizar una pronta recuperación, es importante seguir estas recomendaciones adicionales:</p>
        <ul>
            <p>Evitar el contacto con personas enfermas para prevenir comppcaciones.</p>
            <p>Descansar lo suficiente y no interrumpir el tratamiento antes de tiempo.</p>
            <p>Mantener una apmentación balanceada con frutas y verduras para reforzar el sistema inmunológico.</p>
            <p>Evitar el consumo de alcohol y tabaco durante el periodo de recuperación.</p>
            <p>Si persisten los síntomas, acudir de inmediato a una consulta médica.</p>
        </ul>
    </div></div>
<div class="container">
    <!-- Columna izquierda -->
    <div class="left">
        <h2>⚠️ Recuerda que si empeoras...</h2>
        <p>Debes acudir inmediatamente a consulta médica si presentas fiebre alta, dificultad para respirar o cualquier otro síntoma grave.</p>
        <p>Tu salud es importante, asi que no la descuides!</p>
    </div>

    <!-- Columna central -->
    <div class="center">
        <h1>Certificado de Incapacidad Médica</h1>
        <p>Estimado paciente, se le ha otorgado una incapacidad médica de <b>7 días</b>.</p>
        <p>Durante este tiempo, es recomendable seguir las indicaciones médicas y descansar adecuadamente.</p>
        <p>Si los síntomas persisten, acuda nuevamente al médico.</p>
        
        <button class="button" on:click={generarPDF}>Descargar Incapacidad</button>
    </div>

    <!-- Columna derecha -->
    <div class="right">
        <h2>📌 Indicaciones Médicas</h2>
        <ul>
            <li>Reposo absoluto durante la primera fase</li>
            <li>Tomar medicamentos según prescripción</li>
            <li>Hidratación constante</li>
            <li>Evitar esfuerzo físico</li>
            <li>Acudir a revisión si los síntomas empeoran</li>
        </ul>
    </div>
</div>
