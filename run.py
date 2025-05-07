import streamlit.web.bootstrap as bootstrap
from pathlib import Path

def main():
    """Run the Streamlit application."""
    app_path = Path(__file__).parent / "src" / "main.py"
    bootstrap.run(str(app_path), "", [], {})

if __name__ == "__main__":
    main() 