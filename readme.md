# Library Management System

A LMS created using Django Rest Framework to create users, add book and its details , borrow and return books.

The project runs on [localhost:8080](http://localhost:8080) by default.

### Start:

    git clone [url]

### Setup Environment

    pip -m venv env

### Install Requirements

    pip install -r requirements.txt

### setup postgreSQL

    Create a Database in PostgreSQL.
    In CORE, create a .env file and load your database configurations as :

    DATABASE_ENGINE=django.db.backends.postgresql_psycopg2
    DATABASE_NAME='your_db_name'
    DATABASE_USER='your_pg_user'
    DATABASE_PASSWORD='your_pg_pw'
    DATABASE_HOST='your_pg_host'
    DATABASE_PORT='your_pg_port'

### Run the Server

    python manage.py runserver

### the documentation is hosted on SwaggerUI

    [localhost:8080/swagger](http://localhost:8080/swagger)
