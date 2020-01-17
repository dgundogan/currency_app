## Requirements

[Install docker](https://docs.docker.com/install/)   
[Install docker-compose](https://docs.docker.com/compose/install/)

## Run

### Run server

    sudo docker-compose up -d


## Run tests

	sudo docker-compose run web bash

then run the following in container shell:

    python manage.py test

##  DB creation

    Please run it after starting the server

    docker-compose exec web python manage.py db init
    docker-compose exec web python manage.py db migrate
    docker-compose exec web python manage.py db upgrade

## REST API 

### POST 
When executed it will ingest the data from 3rd party API. You can use it as a CLI like below.
    curl -X POST http://0.0.0.0:5000/api/currencies

### GET
The GET API can be used to retrieve the currency rates for a given date.
    http://0.0.0.0:5000/api/currencies?date=2020-01-15

## Monitoring

    The Flask Monitoring Dashboard is designed to easily monitor your Flask application.
    https://flask-monitoringdashboard.readthedocs.io/en/latest/#

    4 main functionalities
    - Monitor the performance and utilization
    - Profile requests and endpoints
    - Collect extra information about outliers
    - Collect additional information about your Flask-application

### Monitoring UI

    http://0.0.0.0:5000/dashboard/overview




