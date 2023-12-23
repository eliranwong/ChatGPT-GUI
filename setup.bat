@echo off
python -m venv venv
call .\venv\Scripts\activate
pip install --upgrade PySide6 openai tiktoken gtts pyqtdarktheme duckduckgo-search googlesearch-python
python ChatGPT-GUI.py
pause
