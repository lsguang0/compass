from flask import Flask

from apps.apis.user_api import user_bp
from exts import db
import settings


def create_app():
    app = Flask(__name__, static_folder='../static')
    app.config.from_object(settings.DevelopmentConfig)
    db.init_app(app=app)
    app.register_blueprint(user_bp)
    print(app.url_map)
    return app
