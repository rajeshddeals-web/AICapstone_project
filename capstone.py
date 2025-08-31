import streamlit as st
import google.generativeai as genai
from gtts import gtts
import os
import pandas as pd
import PyPDF2
import tempfile

# Set your Google Generative AI API key
genai.configure(api_key="AIzaSyBLbhhwiQCuNCiabOZyM6lCW9t9I0v_Sfo")
model = genai.Model("gemini-1.5-flash")


# Function to generate text using Google Generative AI with exception handling
def translate_text_genai(text, target_language):
    try:
        prompt = f"Translate the following text to {target_language}:\n\n{text}"
        response = model.generate_text(prompt=prompt)
        return response.text
    except Exception as e:
        print(f"An error occurred while generating text: {e}")
        return None

