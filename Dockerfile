FROM python:3.10-slim
WORKDIR /app
COPY src/ ./src/
COPY data/ ./data/
RUN pip install nltk
RUN python -m nltk.downloader punkt stopwords wordnet
ENTRYPOINT ["python", "src/main.py"]
