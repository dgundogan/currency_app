FROM python:3.7

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt 

RUN pip install flask gunicorn
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "run"]