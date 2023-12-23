@echo off
python -m venv venv
call .\venv\Scripts\activate
pip install --upgrade PySide6 openai==0.28.1 tiktoken gtts pyqtdarktheme duckduckgo-search googlesearch-python
python ChatGPT-GUI.py
pause
