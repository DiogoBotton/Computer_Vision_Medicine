# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Opencv dependency libgl1
#RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 unzip
RUN apt-get update && apt-get install -y \
    wget curl unzip gnupg build-essential \
    libgl1 libglib2.0-0 libnss3 libfontconfig1 libxss1 libgtk-3-0 libx11-xcb1 \
    && apt-get clean

# Set the working directory in the container
WORKDIR /api

# Copy the current directory contents into the container at /app
COPY ./api /api

# Instala gdown para baixar o modelo do google drive
RUN pip install gdown

# Baixa o modelo treinado
RUN gdown --id 1aCs5MOa-nvQzawj2n2A9OMcrltXmTVyg -O chexpert_cnn_classifier.keras

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]