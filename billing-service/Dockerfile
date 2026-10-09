FROM python:3.12-slim
RUN useradd --create-home billing
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
USER billing
HEALTHCHECK CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"
CMD ["flask", "run", "--host=0.0.0.0"]
