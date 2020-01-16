FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt 

RUN pip install flask gunicorn

ENV WEBAPP_ENV=prod

RUN chmod +x entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]