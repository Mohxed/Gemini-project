import google.generativeai as genai
import os 
from core.config import settings


genai.configure(api_key=settings.GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-1.5-pro') # Selected a free model

def gemini_response(text):
    response = model.generate_content(text)
    return response.text