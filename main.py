import streamlit as st 
from googletrans import Translator
from languages import languages


st.title("MyAI ACLT")
source_text = st.text_area("Enter message to translate:")
target_language = st.selectbox("Select target language:", languages)
translate = st.button('Translate')
if translate:
    translator = Translator()
    out = translator.translate(source_text,dest=target_language)
    st.write(out.text)
    
                               