FROM python:3.11

WORKDIR /app

RUN pip install uv

COPY pyproject.toml ./
RUN uv pip install --system .

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]