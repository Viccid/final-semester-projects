import json
import requests
import os
from google.cloud import storage, bigquery
from google.cloud.exceptions import NotFound
from config import (
    GCP_PROJECT_ID,
    GCS_BUCKET_NAME,
    BIGQUERY_DATASET,
    BIGQUERY_TABLE,
    API_URL,
    FILE_NAME,
    SCHEMA_FILE,
)

# This ensure the GOOGLE_APPLICATION_CREDENTIALS environment variable is set

if not os.getenv("GOOGLE_APPLICATION_CREDENTIALS"):
    raise EnvironmentError(
        "GOOGLE_APPLICATION_CREDENTIALS environment variable is not set."
    )


# Fetch data from API
def fetch_data():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()


# Write data to JSONLines format
def write_jsonlines(data):
    with open(FILE_NAME, "w") as f:
        for item in data:
            json.dump(item, f)
            f.write("\n")


# Upload file to GCS
def upload_to_gcs(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client(project=GCP_PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)


# Create GCS bucket if not exists
def create_bucket_if_not_exists(bucket_name):
    storage_client = storage.Client(project=GCP_PROJECT_ID)
    try:
        storage_client.get_bucket(bucket_name)
    except NotFound:
        bucket = storage_client.bucket(bucket_name)
        bucket.location = "US"
        storage_client.create_bucket(bucket)


# Create BigQuery dataset if not exists
def create_dataset_if_not_exists(dataset_name):
    bigquery_client = bigquery.Client(project=GCP_PROJECT_ID)
    dataset_ref = bigquery_client.dataset(dataset_name)
    try:
        bigquery_client.get_dataset(dataset_ref)
    except NotFound:
        dataset = bigquery.Dataset(dataset_ref)
        dataset.location = "US"
        bigquery_client.create_dataset(dataset)


# Load data into BigQuery
def load_data_into_bigquery(dataset_name, table_name, source_uri, schema_file):
    bigquery_client = bigquery.Client(project=GCP_PROJECT_ID)
    dataset_ref = bigquery_client.dataset(dataset_name)
    table_ref = dataset_ref.table(table_name)

    # Load schema
    with open(schema_file, "r") as f:
        schema = json.load(f)

    # Define job configuration
    job_config = bigquery.LoadJobConfig(
        schema=schema,
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
    )

    load_job = bigquery_client.load_table_from_uri(
        source_uri, table_ref, job_config=job_config
    )

    # Wait for the job to complete

    load_job.result()

    print(f"Loaded {load_job.output_rows} rows into {dataset_name}:{table_name}")

    # alternatively
    # print(f"successfully wrote{dataset_name} to {table_name}")


def main():
    # Fetch data
    data = fetch_data()

    # Write data to JSONLines
    write_jsonlines(data)

    # Create GCS bucket if not exists
    create_bucket_if_not_exists(GCS_BUCKET_NAME)

    # Upload file to GCS
    upload_to_gcs(GCS_BUCKET_NAME, FILE_NAME, FILE_NAME)

    # Create BigQuery dataset if not exists
    create_dataset_if_not_exists(BIGQUERY_DATASET)

    # Load data into BigQuery
    source_uri = f"gs://{GCS_BUCKET_NAME}/{FILE_NAME}"
    load_data_into_bigquery(BIGQUERY_DATASET, BIGQUERY_TABLE, source_uri, SCHEMA_FILE)

    print("All tables and data loaded successfully.")


if __name__ == "__main__":
    main()
