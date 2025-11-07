from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
import numpy as np
import os

router = APIRouter(tags=["Predicts"])

class RequestData(BaseModel):
    pass # TODO

@router.post("/predict")
async def predict(data: RequestData):
    # Adquire o caminho do modelo
    main_path = os.path.dirname(__file__)
    model_path = os.path.join(main_path, '..', 'chexpert_classifier.joblib')
    
    # TODO: Alterar para o tipo de resposta esperado
    return {
        "predictValue": predict.tolist(), # Converte para lista para evitar erros de serialização
    }