import numpy as np
import tensorflow as tf
from tensorflow.keras.applications.inception_v3 import preprocess_input
import cv2

IMG_SIZE = (299, 299)

def prepare_image_for_predict(image_bytes):
    """
    Prepara a imagem para enviar ao modelo
    
    - Redimensiona a imagem para o tamanho especificado (299x299).
    - Aplica o processo de CLAHE (Contrast Limited Adaptive Histogram Equalization, ou Equalização Adaptativa de Histograma com Limitação de Contraste),
    um processo de processamento de imagem para melhorar o contraste local de uma imagem.
    - Normaliza a imagem entre 0 a 1.
    - Expande as dimensões para ficar no formato (1, X, Y, Canais).
    """
    # Decodifica JPEG/PNG para array numpy
    img = tf.io.decode_image(image_bytes, channels=3)
    img = tf.image.resize(img, IMG_SIZE)
    img = img.numpy().astype(np.uint8)   # agora vira array uint8 para funcionar no cv2

    # Converte para RGB (garantia)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Converte para grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    # Aplica CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    equalized = clahe.apply(gray)

    # Volta para 3 canais
    equalized_rgb = cv2.merge([equalized, equalized, equalized]).astype(np.float32)

    # Aplica preprocess_input do InceptionV3
    processed = preprocess_input(equalized_rgb)

    # Expande batch dimension
    processed = np.expand_dims(processed, axis=0)

    return processed