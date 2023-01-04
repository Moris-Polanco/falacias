import openai
import streamlit as st
import os

# Set up the OpenAI API client
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Configura el modelo GPT-3
model_engine = "text-davinci-003"

st.title("Identificador de falacias")

# Obtener la entrada del usuario
text = st.text_area("Ingresa el texto a analizar:")

# Usa el modelo GPT-3 para analizar el texto en busca de falacias
@st.cache
def detect_fallacies(text):
    completions = openai.Completion.create(
        engine=model_engine,
        prompt=f"Por favor, enumera cualquier falacia presente en el siguiente texto:\n{text}\n",
        max_tokens=1024,
        temperature=0.5,
    )

    # Extraer la primera completación
    fallacy_list = completions.choices[0].text

    return fallacy_list

# Mostrar la lista de falacias
fallacy_list = detect_fallacies(text)
st.write(fallacy_list)
