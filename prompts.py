#Prompt texto-texto
import openai

# Configura la clave API
openai.api_key = "AQUI IRIA TU API KEY"

# Realiza la llamada para generar el chat
cliente = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "¿Podrias crearme una rutina para una persona de 32 años, 72 kg, sexo masculino, que cubra todos los musculos para entrenar 6 dias a la semana",
        }
    ],
)

# Imprime la respuesta
print(cliente.choices[0].message["content"])


#Prompt texto-imagen

import openai
import requests
from io import BytesIO
from PIL import Image

#Configurando la API KEY
openai.api_key = "AQUI VA TU API KEY"

prompt_usuario = input("Mostrame la tecnica correcta del ejercicio dorsales abiertos con barra para espalda")

#Generar la imagen
response = openai.Image.create(
    model="dall-e-3",
    prompt = prompt_usuario,
    size = "1024x1024"
)

#Obteniendo el link de la imagen generada
url_image = response['data'][0]['url']
print(url_image)

#guardar imagen
imagen = Image.open(BytesIO(requests.get(url_image).content))
imagen.save('imagen.png')
