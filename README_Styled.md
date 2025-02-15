# 🏋️‍♂️ Generación de Rutinas con IA

Bienvenido a **Generación de Rutinas con IA**, un proyecto diseñado para ayudar a los usuarios a obtener rutinas de entrenamiento personalizadas utilizando inteligencia artificial. Esta herramienta digitaliza la experiencia en el gimnasio, evitando la acumulación de personas en busca de información y brindando accesibilidad a los principiantes.

---

## 🚀 Funcionalidades

✅ **Generación de rutinas personalizadas** según datos del usuario.  
✅ **Visualización de ejercicios con imágenes generadas por IA**.  
✅ **Interfaz sencilla y automatizada** para mejorar la experiencia del usuario.  
✅ **Costos accesibles** gracias a la optimización del uso de tokens en OpenAI.  

---

## 🛠 Tecnologías Utilizadas

- [Python](https://www.python.org/) para la implementación del código.
- [OpenAI GPT-4o](https://openai.com/) para la generación de rutinas.
- [DALL·E 3](https://openai.com/dall-e/) para la creación de imágenes ilustrativas.
- [Pillow](https://python-pillow.org/) para el procesamiento de imágenes.

---

## 🎯 Problema a Abordar

Muchos usuarios enfrentan dificultades para iniciar su entrenamiento debido a la falta de conocimiento, distancia al gimnasio o timidez. Este proyecto soluciona ese problema generando rutinas personalizadas a través de IA, basadas en datos personales como edad, peso, altura y nivel de experiencia.

---

## 💡 Solución Propuesta

Utilizaremos la API de OpenAI para generar respuestas automáticas a prompts de los usuarios. Se solicitarán datos básicos como peso, altura, edad, tiempo de entrenamiento y disponibilidad horaria. Además, se emplearán modelos de generación de imágenes para mostrar la ejecución correcta de los ejercicios.

### 📌 Ejemplo de Prompt Texto-Texto

```python
import openai

# Configura la clave API
openai.api_key = "AQUI VA TU API KEY"

# Generar una rutina de entrenamiento personalizada
cliente = openai.ChatCompletion.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": "¿Podrías crearme una rutina para una persona de 32 años, 72 kg, sexo masculino, que cubra todos los músculos para entrenar 6 días a la semana?",
        }
    ],
)

# Imprimir la respuesta
print(cliente.choices[0].message["content"])
```

### 🎨 Ejemplo de Prompt Texto-Imagen

```python
import openai
import requests
from io import BytesIO
from PIL import Image

# Configura la clave API
openai.api_key = "AQUI VA TU API KEY"

prompt_usuario = "Mostrame la técnica correcta del ejercicio dorsales abiertos con barra para espalda"

# Generar la imagen con IA
response = openai.Image.create(
    model="dall-e-3",
    prompt=prompt_usuario,
    size="1024x1024"
)

# Obtener el link de la imagen generada
url_image = response['data'][0]['url']
print(url_image)

# Guardar la imagen
imagen = Image.open(BytesIO(requests.get(url_image).content))
imagen.save('imagen.png')
```

---

## 📊 Ejemplo de Rutina Generada

### 🔴 Día 1: Pecho y Tríceps
- 🏋️‍♂️ Press de banca plano con barra – 4x6-8
- 💪 Press inclinado con mancuernas – 4x8-10
- 🔥 Fondos en paralelas – 3x8-12
- 🏋️‍♂️ Extensiones de tríceps en polea – 4x10-12

### 🟠 Día 2: Espalda y Bíceps
- 🔥 Dominadas – 4x6-8
- 💪 Remo con barra – 4x8-10
- 🏋️‍♂️ Curl de bíceps con barra – 4x10

### 🟡 Día 3: Piernas y Pantorrillas
- 🏋️‍♂️ Sentadilla con barra – 4x6-8
- 💪 Prensa de piernas – 4x10
- 🔥 Elevación de talones de pie – 4x15-20

### 🟢 Día 4: Hombros y Abdominales
- 🏋️‍♂️ Press militar con barra – 4x6-8
- 💪 Elevaciones laterales – 4x10-12
- 🔥 Plancha abdominal – 3x45-60 seg

### 🔵 Día 5: Pecho y Tríceps (Variaciones)
- 🏋️‍♂️ Press inclinado con barra – 4x6-8
- 💪 Press de banca con mancuernas – 4x8-10

### 🟣 Día 6: Espalda, Bíceps y Piernas Ligeras
- 🏋️‍♂️ Peso muerto – 4x6-8
- 💪 Curl de bíceps concentrado – 3x10-12
- 🔥 Sentadilla frontal – 3x10

---

## 📌 Objetivo del Proyecto

El objetivo de este proyecto es facilitar el acceso a rutinas personalizadas a través de la IA y proporcionar apoyo a los entrenadores en gimnasios mediante la digitalización de la experiencia.

## 📖 Metodología

Se utilizarán técnicas de generación de contenido con IA basadas en el concepto de **"patrón persona"**, lo que permite adaptar las rutinas según los ajustes necesarios. Además, se trabajará en conjunto con los entrenadores del gimnasio para asegurar que las rutinas sean efectivas.

---

## 💰 Costos Aproximados

El costo de uso de la API de OpenAI es relativamente bajo. Puedes consultar los precios en los siguientes enlaces:  
🔗 [Token Calculator](https://platform.openai.com/tokenizer)  
🔗 [Precios de OpenAI](https://openai.com/api/pricing/)  

Ejemplo: Una rutina generada consume menos de 1K de tokens, lo que equivale a **$0.00250 USD**.

---

## 📢 Contacto

Si tienes preguntas o sugerencias, no dudes en contactarme:  
📧 **Email**: [tuemail@example.com](mailto:tuemail@example.com)  
🌍 **GitHub**: [TuPerfil](https://github.com/TuPerfil)  

**¡Entrena inteligente con IA! 🚀**

© 2025 Jonathan Carles
