# AltSchool py_gcs_bq assignment: Loading Data into Google Cloud Storage and BigQuery
## Overview:
### Project demonstration:

This project provides a comprehensive pipeline to load data from CSV files and APIs into Google BigQuery and Google Cloud Storage (GCS). The project pipeline ensures idempotency, reusability, and ease of use, with proper secrets management and documentation.

     - Fetching Data from system file and loading into BigQuery.
     
     - Fetching Data from an API, Storing in GCS, and Loading into BigQuery.

    

### Prerequisites:

    Python 3:  Ensure Python 3 is installed on your machine.

    VSCode: Chosen for easy implementation of the code.

    Git: For smooth remote repository management.

    Google Cloud SDK: Ensure you have the Google Cloud SDK

    installed and configured.

BigQuery and GCS: Ensure you have the necessary permissions to create datasets, tables, and buckets in Google Cloud.

### Project Structure:

    py_gcs_bq/

    └── .env

    └── .env.example

    └── config.py

    └── main.py

    └── sandbox.py

    ├── data/

    └── smartphones.csv

    ├── schemas/playstation_games_schema.json

    ├── Readme.md

### Usage:
This project provides a solution for ingesting data from local CSV files and APIs into Google BigQuery consisting of two main functionalities.This can be adapted and integrated with more functionality and specific requirements.

> Loading CSV to BigQuery :
* python py_gcs_bq/load_csv_to_bigquery.py

> Fetching API Data and Loading to BigQuery:
* python py_gcs_bq/fetch_api_and_load_to_bigquery.py

### Setup instructions:

This setup ensures that all necessary packages are installed and that your project is ready to interact with Google Cloud Storage and BigQuery seamlessly.


> Steps to run the code:

* Python is installed on the machine.

* Installed Visual Studio Code, from VSCode's official website.

* Installed python Extensions view

> Google Cloud dependencies
* google-cloud-storage==2.7.0
* google-cloud-bigquery==3.4.0
* google-auth==2.15.0
* google-auth-oauthlib==0.7.1


### Conclusion:

This project provides a robust and seamless solution for ingesting data from local CSV files and APIs into Google BigQuery. With an emphasis on idempotency, reusability, and ease of use, the pipeline is designed to ensure consistent results, modularity, and straightforward integration into different environments and projects.

### License:
MIT License

Copyright (c) [2023] [Idiyeli Sunday]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author Info:
Twitter : https://twitter.com/idiyeli

linkedin : https://www.linkedin.com/in/idiyeli-sunday-8182b259/











