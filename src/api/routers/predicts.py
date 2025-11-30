from fastapi import APIRouter, File, HTTPException, UploadFile
from tensorflow.keras.models import load_model
from utils import prepare_image_for_predict
from custom_layers.layers import ChannelAttention, SpatialAttention
import os

ALLOWED_EXTENSIONS = ['.png', '.jpg', '.jpeg']
LABEL_COLS = ["no_finding","enlarged_cardiomediastinum","cardiomegaly","lung_opacity","lung_lesion","edema","consolidation","pneumonia","atelectasis","pneumothorax","pleural_effusion","pleural_other","fracture","support_devices"]

main_path = os.path.dirname(__file__)
cnn_model_path = os.path.join(main_path, '..', 'chexpert_cnn_classifier.keras')
cnn_model = load_model(cnn_model_path, 
                       custom_objects={
                           "ChannelAttention": ChannelAttention,
                           "SpatialAttention": SpatialAttention
                       })

router = APIRouter(tags=["Predicts"])

@router.post("/predict")
async def predict(file: UploadFile = File(...)):
    """
    ### Classificação de doenças cardíacas

    Realiza classificação de doenças cardíacas em Raio X do tórax com perspectiva frontal do tipo PA.
    
    PA — Posteroanterior: O feixe entra pelas costas e sai pelo peito.

    **Arquivos válidos:**
    - png
    - jpg
    - jpeg
    """
    filename = file.filename

    file_extension = os.path.splitext(filename)[1].lower()
    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail=f'Extensão de arquivo inválida: {file_extension}. Permitidos: {ALLOWED_EXTENSIONS}')
    
    img = await file.read()  # lê o conteúdo do arquivo
    img = prepare_image_for_predict(img)
    
    pred = cnn_model.predict(img)[0]
    print(pred)
    
    return { label: round(float(pred[idx]) * 100, 2)
            for idx, label in enumerate(LABEL_COLS) }