from setuptools import setup, find_packages

setup(
    name="ai-chat-assistant",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "streamlit>=1.28.0",
        "google-generativeai>=0.3.0",
    ],
) 