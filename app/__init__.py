from flask import Flask
from .routes import bp
import os


def create_app():
    app = Flask(__name__)

    # Externalized configuration via environment variables
    app.config["APP_VERSION"] = os.getenv("APP_VERSION", "1.0.0")
    app.config["MAX_TASKS"]= int(os.getenv("MAX_TASKS", "100"))

    app.register_blueprint(bp)
    return app
