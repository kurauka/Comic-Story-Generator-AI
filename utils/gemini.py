import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

def generate_comic_story(prompt: str) -> str:
    # Enhanced prompt with clear multi-page instructions
    enhanced_prompt = f"""
    Create a fun comic book story for kids based on this prompt: '{prompt}'
    
    Format the story as a comic book with multiple distinct pages.
    For each page:
    - Start with "Page X:" where X is the page number
    - Include characters, narration, and dialogue
    - Make each page a complete scene with a beginning and end
    - Include character dialogue in the format: Character: "Dialogue"
    
    Keep the overall tone kid-friendly and appropriate.
    """
    
    response = model.generate_content(enhanced_prompt)
    return response.text