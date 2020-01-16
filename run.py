from flask import Flask
import flask_monitoringdashboard as dashboard
import os

from app.config import app_config

def create_app(config_name):
    app = Flask(__name__)
    dashboard.bind(app)
    app.config.from_object(app_config[config_name])
    
    from app import api_bp
    app.register_blueprint(api_bp, url_prefix='/api')

    from app.Model import db
    db.init_app(app)

    return app

if __name__ == "__main__":
    env = os.environ.get('WEBAPP_ENV', 'dev')
    app = create_app(env)
    app.run(host='0.0.0.0')