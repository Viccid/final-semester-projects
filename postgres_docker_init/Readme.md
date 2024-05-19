# Alt School AssignmentPostgres infrastructure with Docker
## Overview:
This project demonstrates how to set up a PostgreSQL server using Docker and Docker Compose. The setup includes creating a schema and a table, loading data from a CSV file into the PostgreSQL database, and interacting with the database using a Python script.

## Structure Of Directory/Folder:
- Postgres_docker_init
  - data
  - infra_scripts
     ->  init.sql
  - src -> postgres_interaction.py
  - docker-compose.yml'
  - readme.md

## Prerequisites:
- psycopg2 library installed for PostgreSQL interaction from Python (installed via pip).
- Python 3 was installed, as this code is compatible with it.
- Vscode (visual enviroment) was choosen for easy implementation of the code.
- Git was easily installed for smooth remote repository to github.
- Docker and Docker Compose installed on your machine.

## Project Structure

postgres_docker_init/

├── data/

└── Netflix.csv

├── infra_scripts/

  └── init.sql

├── src/

  └── main.py

├── docker-compose.yml

└── README.md

## Setup Instructions:
Create a New Branch and Project Directory Structure

    - git checkout -b projstart

    - mkdir -p postgres_docker_init/{data,infra_scripts,src}
      cd postgres_docker_init

    - cd postgres_docker_init

In your new branch, create a folder called postgres_docker_init and navigate into it.

#### Docker Compose Configuration:
version: '3'

- services:
  - postgres:
    - image: postgres:latest
  - environment:

      - POSTGRES_USER: netflix_data_user

      - POSTGRES_PASSWORD: Viccid11001

      - POSTGRES_DB: netflix_data_db
  - ports:
      - "5434:5432"
  - volumes:
      - ./postgres_data:/var/lib/postgresql/data
      - ./data:/data
      - ./infra_scripts/init.sql:/docker-entrypoint-initdb.d/init.sql

## Usage:
This project demonstrates the usage of docker and docke-compose-yml in adding new movie records to the Netflix Movies database, retrieving and displaying movie records, updating existing records, and removing records from the database. These functionalities can be adapted and extended based on specific requirements.

## Note:
The python script Expense and ExpenseDatabase class explained the functionality of expense tracker.

License:
MIT License

Copyright (c) [2024] [Idiyeli Sunday]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Author Info:
Twitter : https://twitter.com/idiyeli

linkedin : https://www.linkedin.com/in/idiyeli-sunday-8182b259/



  
