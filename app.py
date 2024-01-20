import streamlit as st 
#from googletrans import Translator
from language import *
from openai import OpenAI
from dotenv import load_dotenv
from decouple import config
import openai
import os
load_dotenv()

openai.api_key=os.getenv("OPENAI_API_KEY")

# Define a function to handle the translation process
def translate_text(text, target_language):
    # Define the prompt for the ChatGPT model
    prompt = f"Please translate '{text}' to {target_language}, without including any additional information or explanation. eg user: ¡Vale! your response: okay!, user: agba la gba ni mi your response: I am an old man"

    
    # Generate the translated text using ChatGPT
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that translates text."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Extract the translated text from the response
    translated_text = response.choices[0].message.content.strip()
    
    return translated_text
# Define the main function that sets up the Streamlit UI and handles the translation process
def main():
    # Set up the Streamlit UI
    st.sidebar.header('MyAI ACLT')
    st.sidebar.write('Please enter text to translate and select the target language:')
    
    # Create a text input for the user to enter the text to be translated
    text_input = st.text_input('Enter text')
    
    # Create a selectbox for the user to select the target language
    target_language = st.selectbox('Select language', ['Arabic', 'English', 'Spanish', 'French', 'German'])
    
    # Create a button that the user can click to initiate the translation process
    translate_button = st.button('Translate')
    
    # Create a placeholder where the translated text will be displayed
    translated_text = st.empty()
    
    # Handle the translation process when the user clicks the translate button
    if translate_button:
        translated_text.text('Translating...')
        translated_text.markdown(f'<span style="font-size:40px">{translate_text(text_input, target_language)}</span>', unsafe_allow_html=True)

        translated_text.text(translate_text(text_input, target_language))
    # Call the main function
if __name__ == '__main__':
    main()
