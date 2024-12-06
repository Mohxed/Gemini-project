import google.generativeai as genai
import os
import re
from app.core.config import settings

# Configure the Gemini API with the provided settings
genai.configure(api_key=settings.GEMINI_API_KEY)

# Initialize the generative model
model = genai.GenerativeModel(model_name=settings.GEMINI_MODEL)  # Selected a free model

# Function to clean markdown from text
def remove_markdown(text):
    markdown_pattern = r'(\*\*|__|\*|_|`|~{2,}|#|>)'
    return re.sub(markdown_pattern, '', text)

def gemini_response(text, token_limit=1000, page_size=500):

    # Remove markdown from the input text
    clean_text = remove_markdown(text)

    # Enforce token limit on input
    if len(clean_text) > token_limit:
        clean_text = clean_text[:token_limit]

    # Generate response
    response = model.generate_content(clean_text)

    # Paginate the output
    output_text = response.text
    paginated_output = [
        output_text[i:i + page_size] for i in range(0, len(output_text), page_size)
    ]

    return paginated_output
