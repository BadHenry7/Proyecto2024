from fastapi import FastAPI
from fastapi import APIRouter, HTTPException
import pandas as pd
import numpy as np
from pydantic import BaseModel
from tensorflow.keras.models import load_model


router = APIRouter()
# Cargar el dataset y el modelo
data = pd.read_csv("../red/dataset2.csv", sep=";")

model = load_model("../red/botci.h5")

# Obtener lista de síntomas y enfermedades
symptoms = data.drop(columns=["diseases"]).columns.tolist()
diseases = data["diseases"].unique().tolist()



# Modelo para recibir los síntomas seleccionados
class PredictionRequest(BaseModel):
    selected_symptoms: list[str]

@router.get("/sintomas")
async def get_symptoms():
   

    return {"sintomas": symptoms}

@router.post("/predict")
async def predict_disease(request: PredictionRequest):
    # Crear un vector de entrada con los síntomas seleccionados
    selected = request.selected_symptoms
    input_vector = [1 if symptom in selected else 0 for symptom in symptoms]
    input_vector = np.array(input_vector).reshape(1, -1)

    # Hacer la predicción
    result = model.predict(input_vector)
    predicted_class = np.argmax(result)
    predicted_disease = diseases[predicted_class]

    return {"enfermedad": predicted_disease}
