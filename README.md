## Requirements

[Install docker](https://docs.docker.com/install/)   
[Install docker-compose](https://docs.docker.com/compose/install/)

## Database Configuration

python manage.py db init

python manage.py db migrate

python manage.py db upgrade


## Run

### Run server

    sudo docker-compose up -d


## Run tests

	sudo docker-compose run web bash

then run the following in container shell:

	pytest -v


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




curl https://gist.githubusercontent.com/richardARPANET/79434d9995585f639344e17c35476728/raw/36e9ca68088ee7832220a20c31997a25a0bbd271/lint.sh | sh


