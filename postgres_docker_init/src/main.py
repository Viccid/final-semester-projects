import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()


# this create connection


def _get_postgres_creds():
    return {
        "user": os.environ.get("POSTGRES_USER"),
        "password": os.environ.get("POSTGRES_PASSWORD"),
        "port": os.environ.get("POSTGRES_PORT", "5434"),
        "host": os.environ.get("POSTGRES_HOST", "localhost"),
        "dbname": os.environ.get("POSTGRES_DB"),
    }


# this function handle any error if it occur


def _start_postgres_connection():
    creds = _get_postgres_creds()
    try:
        connection = psycopg2.connect(
            dbname=creds["dbname"],
            user=creds["user"],
            password=creds["password"],
            host=creds["host"],
            port=creds["port"],
        )
        return connection
    except psycopg2.OperationalError as e:
        print(f"Error: Could not connect to the PostgreSQL server: {e}")
        return None


def query_database(connection, query_str):
    if connection is None:
        print("No connection to the database.")
        return []

    cursor = connection.cursor()
    cursor.execute(query_str)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


# finally query to counts number of record

if __name__ == "__main__":
    conn = _start_postgres_connection()
    if conn is not None:
        query = "SELECT COUNT(*) AS total_records FROM netflix_data.netflix"
        result = query_database(connection=conn, query_str=query)
        print(result)
    else:
        print("Failed to connect to the database. Exiting.")
