# 🤖 AI Chat Assistant

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-2.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

A modern, intelligent chat assistant powered by Google's Gemini 2.0 model, featuring a sleek Streamlit interface and advanced conversation capabilities.

![Chat Assistant Demo](https://raw.githubusercontent.com/Abhirup0/AI-Chat-Assistant/master/static/demo.gif)

## ✨ Features

- 🧠 Powered by Google's Gemini 2.0 model for intelligent responses
- 💬 Natural conversation flow with context awareness
- 🎨 Modern, responsive UI design
- 📝 Markdown support for formatted responses
- 🔄 Chat history management
- 🛡️ Input validation and error handling
- 🎯 Configurable model parameters

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Abhirup0/AI-Chat-Assistant.git
cd AI-Chat-Assistant
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
# Edit .env with your Google Gemini API key
```

4. Run the application:
```bash
python -m streamlit run src/main.py
```

## 🛠️ Configuration

The application can be configured through the `config.py` file:

- `MAX_INPUT_LENGTH`: Maximum length of user input
- `MAX_HISTORY_LENGTH`: Maximum number of conversation turns to maintain
- Other model parameters and settings

## 📁 Project Structure

```
AI-Chat-Assistant/
├── src/
│   ├── main.py           # Main Streamlit application
│   ├── gemini_handler.py # Gemini model integration
│   ├── config.py        # Configuration settings
│   └── utils/           # Utility functions
├── static/              # Static assets and styles
├── requirements.txt     # Project dependencies
└── README.md           # Project documentation
```

## 🎯 Usage

1. Start the application using the command above
2. Access the chat interface at `http://localhost:8501`
3. Type your message in the chat input
4. Receive intelligent responses from the AI assistant

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini API for providing the language model
- Streamlit for the amazing web framework
- All contributors and supporters of this project

## 📧 Contact

Abhirup - [@Abhirup0](https://github.com/Abhirup0)

Project Link: [https://github.com/Abhirup0/AI-Chat-Assistant](https://github.com/Abhirup0/AI-Chat-Assistant) 