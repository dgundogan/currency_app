import requests
import datetime

from flask import request, Response
from flask_restful import Resource
from app.Model import db, Currency, CurrencySchema
from environs import Env

currencies_schema = CurrencySchema(many=True)
currency_schema = CurrencySchema()

env = Env()
env.read_env()
api_key = env("API_KEY")
url = "http://data.fixer.io/api/latest?access_key={}".format(api_key)


class CurrencyResource(Resource):
    def get(self):
        date = request.args.get('date')
        if not date:
            return {"status": "error",
                    'message': 'No date parameter provided'}, 400

        currencies = Currency.query.filter_by(date=date).all()
        if not currencies:
            return {"status": "error", 'message': 'No data found'}, 404
        currencies = currencies_schema.dump(currencies)

        return {'status': 'success', 'data': currencies}, 200

    def post(self):
        response = requests.get(url)
        data = response.json()

        if not data:
            return {"status": "error",
                    'message': 'Cannot access the source'}, 500
        if not data['success']:
            return {"status": "error", 'message': data['error']}, 500

        date = datetime.datetime.strptime(data["date"], '%Y-%m-%d').date()
        record_count = 0
        for currency, rate in data["rates"].items():
            # check whether the record exists or not.
            exist = Currency.query.filter_by(date=date, base=data["base"],
                                             currency=currency).first()
            if not exist:
                curr = Currency(date=date, base=data["base"],
                                currency=currency, rate=rate)
                db.session.add(curr)
                record_count += 1
        db.session.commit()
        return Response("{} records is inserted".format(record_count),
                        status=201)
