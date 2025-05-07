# AI Chat Assistant

A simple chatbot application built using Google's Gemini Pro model and Streamlit. This project demonstrates the use of Large Language Models (LLMs) in creating an interactive chat interface.

## Features

- Interactive chat interface using Streamlit
- Integration with Google's Gemini Pro model
- Chat history management
- Context-aware responses
- Clean and modern UI
- Error handling and input validation

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd <repository-name>
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# On Windows:
.\venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
   - Copy `.env.example` to `.env`
   - Add your Google API key to the `.env` file

5. Run the application:
```bash
streamlit run src/main.py
```

## Project Structure

```
project/
├── .env                    # API keys and configuration
├── requirements.txt        # Project dependencies
├── README.md              # Project documentation
├── src/
│   ├── main.py            # Main application file
│   ├── gemini_handler.py  # Gemini API integration
│   ├── config.py          # Configuration management
│   └── utils/
│       └── prompt_utils.py # Prompt templates and utilities
└── static/
    └── styles.css         # Custom styling
```

## Implementation Details

- Uses Google's Gemini Pro model for generating responses
- Implements prompt engineering techniques for better context management
- Maintains conversation history for contextual responses
- Provides a clean and intuitive user interface using Streamlit

## Future Improvements

- Add support for different conversation styles
- Implement conversation memory management
- Add support for file uploads and processing
- Enhance error handling and rate limiting
- Add user authentication

## License

MIT License 