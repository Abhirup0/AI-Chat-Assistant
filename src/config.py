import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Configuration class for the application."""
    
    # API Configuration
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
    DEBUG = os.getenv("DEBUG", "False").lower() == "true"
    
    # Application Settings
    MAX_INPUT_LENGTH = 1000
    MAX_HISTORY_LENGTH = 10  # Maximum number of messages to keep in history
    
    # Model Configuration
    MODEL_NAME = "gemini-pro"
    TEMPERATURE = 0.7  # Controls response randomness (0.0 to 1.0)
    TOP_P = 0.8  # Controls response diversity
    
    # Safety Settings
    SAFETY_CATEGORIES = [
        "HARM_CATEGORY_HARASSMENT",
        "HARM_CATEGORY_HATE_SPEECH",
        "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "HARM_CATEGORY_DANGEROUS_CONTENT"
    ]
    SAFETY_THRESHOLD = "BLOCK_MEDIUM_AND_ABOVE"
    
    @classmethod
    def validate_config(cls) -> bool:
        """Validate that all required configuration is present."""
        if not cls.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY environment variable is not set")
        return True 