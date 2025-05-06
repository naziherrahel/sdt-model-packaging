# Live Detection with Streamlit, Pydantic, pytest, CI/CD, and Docker 🚀

## Run Locally

```bash
pip install -r requirements.txt
cp .env.example .env
streamlit run streamlit_app.py
```

## Run Tests

```bash
pytest
```

## Docker

```bash
docker build -t yolov8-streamlit .
docker run -p 8501:8501 yolov8-streamlit
```
