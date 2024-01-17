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
    prompt = f"Translate the text : '{text}' to {target_language} only. The result should be a straight translation with no explanation, and precise for example always use this format  'Comment vous appelez-vous' your response 'What is your name?'. Another example  'Comment ça va'  your response: 'How are you?',  another example 'كيف حالك؟' should be 'How are you?, etc' "

    
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
    st.sidebar.header('MyAI ACTL')
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
        translated_text.text(translate_text(text_input, target_language))
    # Call the main function
if __name__ == '__main__':
    main()
