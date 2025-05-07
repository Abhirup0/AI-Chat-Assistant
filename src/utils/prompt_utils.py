from typing import List, Dict

def create_system_prompt() -> str:
    """Creates the system prompt that defines the AI assistant's behavior."""
    return """You are a helpful and knowledgeable AI assistant. You provide clear, accurate, and concise responses.
    You always maintain a professional tone while being friendly and engaging.
    If you're unsure about something, you'll acknowledge that uncertainty.
    You'll never make up information or provide false details."""

def format_chat_history(messages: List[Dict[str, str]]) -> str:
    """Formats the chat history into a string for context."""
    formatted_history = ""
    for message in messages:
        role = message["role"].capitalize()
        content = message["content"]
        formatted_history += f"{role}: {content}\n"
    return formatted_history

def create_prompt_with_context(user_input: str, chat_history: List[Dict[str, str]]) -> str:
    """Creates a prompt that includes chat history context."""
    system_prompt = create_system_prompt()
    history = format_chat_history(chat_history)
    
    full_prompt = f"""{system_prompt}

Previous conversation:
{history}

User: {user_input}
Assistant:"""
    
    return full_prompt 