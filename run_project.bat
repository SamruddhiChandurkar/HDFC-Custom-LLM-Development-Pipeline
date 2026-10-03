@echo off
cd /d "%~dp0"

start "HDFC Backend" cmd /k "call .venv\Scripts\activate.bat && python -m uvicorn src.api:app --reload"

timeout /t 3 /nobreak >nul

start "HDFC Streamlit" cmd /k "call .venv\Scripts\activate.bat && streamlit run app.py"

exits