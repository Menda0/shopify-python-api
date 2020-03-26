#!/usr/bin/env python
import os
import sys
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api
from flask_injector import singleton, FlaskInjector
from shopify_resources import API_HANDLERS

import pony
sys.path.append(os.path.dirname(os.getcwd()))

VERSION = os.environ.get("VERSION", "1.0.0")
PORT = int(os.environ.get("PORT", 5000))

print(f"VERSION: {VERSION}")
print(f"PORT: {PORT}")

API_PREFIX = "/v1"

app = Flask(__name__)
CORS(app)
api = Api(app=app, prefix=API_PREFIX)


for handler in API_HANDLERS:
    handler.decorators = handler.DECORATORS
    api.add_resource(handler, handler.ENDPOINT)


def configure(binder):
    pass


injector = FlaskInjector(app=app, modules=[configure])


if __name__ == "__main__":
    app.run(debug=True, port=PORT, host="0.0.0.0")
