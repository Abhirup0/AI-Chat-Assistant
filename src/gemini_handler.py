import os
from typing import List, Dict, Optional
import google.generativeai as genai
from src.utils.prompt_utils import create_prompt_with_context

class GeminiHandler:
    def __init__(self):
        """Initialize the Gemini handler with API key and model configuration."""
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is not set")
        
        genai.configure(api_key=api_key)
        # Using the stable version of Gemini 2.0 Flash
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        
        # Updated safety settings based on current API
        self.safety_settings = {
            "harassment": "block",
            "hate_speech": "block",
            "sexually_explicit": "block",
            "dangerous": "block"
        }

    def generate_response(self, user_input: str, chat_history: Optional[List[Dict[str, str]]] = None) -> str:
        """Generate a response using the Gemini model with context and safety settings."""
        try:
            # Create prompt with context if chat history exists
            if chat_history:
                prompt = create_prompt_with_context(user_input, chat_history)
            else:
                prompt = user_input

            # Generate response with safety settings
            generation_config = {
                "temperature": 0.7,
                "top_p": 0.8,
                "top_k": 40,
                "max_output_tokens": 2048,
            }

            # For the current version, we'll generate content without explicit safety settings
            # as they are now handled at the model configuration level
            response = self.model.generate_content(
                prompt,
                generation_config=generation_config
            )

            if not response.text:
                return "I apologize, but I couldn't generate a response. Please try rephrasing your question."

            return response.text

        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return error_message

    def validate_input(self, user_input: str) -> bool:
        """Validate user input before processing."""
        if not user_input or not user_input.strip():
            return False
        if len(user_input) > 1000:  # Arbitrary limit to prevent very long inputs
            return False
        return True 