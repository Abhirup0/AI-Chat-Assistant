import os
import sys
import streamlit.cli as stcli

if __name__ == "__main__":
    sys.path.insert(0, os.path.abspath("."))
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, "src", "main.py")
    sys.argv = ["streamlit", "run", filename]
    stcli.main() 