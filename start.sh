#!/bin/sh
python -m uvicorn src.api:app --host 0.0.0.0 --port 8000 &
exec streamlit run app.py --server.address 0.0.0.0 --server.port 8501
