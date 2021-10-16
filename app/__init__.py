from flask import Flask

from app.camera.routes import camera_blueprint
from app.television.routes import tv_blueprint


def create_app():
    app = Flask("BestBuyAPI")
    app.register_blueprint(tv_blueprint)
    app.register_blueprint(camera_blueprint)
    return app
