import os
from dotenv import load_dotenv

# loading environment variables from .env file

load_dotenv()

GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
GCS_BUCKET_NAME = os.getenv("GCS_BUCKET_NAME")
BIGQUERY_DATASET = os.getenv("BIGQUERY_DATASET")
BIGQUERY_TABLE = os.getenv("BIGQUERY_TABLE")
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

API_URL = "https://api.sampleapis.com/playstation/games"
FILE_NAME = "playstation_games.jsonl"
SCHEMA_FILE = "schemas/playstation_games_schema.json"
