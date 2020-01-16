from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    base = db.Column(db.String(10))
    currency = db.Column(db.String(10))
    rate = db.Column(db.Integer())


class CurrencySchema(ma.Schema):
    base = fields.String(required=True)
    currency = fields.String(required=True)
    rate = fields.String(required=True)
