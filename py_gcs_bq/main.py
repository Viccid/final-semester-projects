from google.cloud import bigquery
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# creating bigquery client


def create_bigquery_client(project_id):
    return bigquery.Client(project=project_id)


#  create a dataset in bigquery


def create_dataset(client, dataset_id):
    dataset_ref = client.dataset(dataset_id)
    dataset = client.create_dataset(dataset_ref)
    return dataset


# this creates a table in bigquery
def create_table(client, dataset_id, table_id, schema):
    table_ref = client.dataset(dataset_id).table(table_id)
    table = bigquery.Table(table_ref, schema=schema)

    # this help in catching errors
    try:
        client.get_table(table_ref)
        print(f"Table {table_id} already exists.")
    except:
        table = client.create_table(table)
        print(f"Created table {table_id}.")

    return table


# this loads data from a CSV file into bigquery


def load_data_into_bigquery(client, file_path, table_ref, job_config):
    with open(file_path, "rb") as source_file:
        load_job = client.load_table_from_file(
            source_file, table_ref, job_config=job_config
        )
    load_job.result()
    return load_job.output_rows


def main():
    PROJECT_ID = "alt-school-424820"
    DATASET_ID = "etl_basics"
    TABLE_ID = "phone_prices"
    FILE_PATH = "C:/Users/HP/altsch_final_semester/final-semester-projects/py_gcs_bq/data/smartphones.csv"

    # Initialize BigQuery client
    client = create_bigquery_client(PROJECT_ID)

    # Define the schema
    schema = [
        bigquery.SchemaField("Smartphone", "STRING"),
        bigquery.SchemaField("Brand", "STRING"),
        bigquery.SchemaField("Model", "STRING"),
        bigquery.SchemaField("RAM", "INTEGER"),
        bigquery.SchemaField("Storage", "INTEGER"),
        bigquery.SchemaField("Color", "STRING"),
        bigquery.SchemaField("Free", "BOOLEAN"),
        bigquery.SchemaField("Final_Price", "FLOAT"),
    ]

    # Create a dataset
    create_dataset(client, DATASET_ID)

    # Create the table
    create_table(client, DATASET_ID, TABLE_ID, schema)

    # Configure the load job
    job_config = bigquery.LoadJobConfig(
        skip_leading_rows=1,
        autodetect=True,
        source_format=bigquery.SourceFormat.CSV,
    )

    # Load data from the CSV file
    rows_loaded = load_data_into_bigquery(
        client, FILE_PATH, f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}", job_config
    )

    print(f"Loaded {rows_loaded} rows into {DATASET_ID}:{TABLE_ID}.")


if __name__ == "__main__":
    main()
