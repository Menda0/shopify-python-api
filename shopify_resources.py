from flask_restful import Resource, reqparse
from flask_injector import inject
import os
import requests


class Version(Resource):
    DECORATORS = []
    ENDPOINT = "/version"

    def get(self):
        VERSION = os.environ.get("VERSION", "1.0.0")
        return f"Shopify Test API - Version {VERSION}"


class Products(Resource):
    DECORATORS = []
    ENDPOINT = "/products"

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument("title", type=str)
        self.reqparse.add_argument("description", type=str)
        self.reqparse.add_argument("vendor", type=str)
        self.reqparse.add_argument("type", type=str)
        self.reqparse.add_argument("image_url", type=str)

        self.url = "https://c63d9fdab773b109d5e1d81f439ad29d:850eeb42e98ac060bf97942dcbf2a324@formacao-react.myshopify.com/admin/api/2020-01/products.json"


    def get(self):
        r = requests.get(self.url)
        return r.json()

    def post(self):

        args = self.reqparse.parse_args()

        data = {
            "product": {
                "title": args.title,
                "body_html": args.description,
                "vendor": args.vendor,
                "product_type": args.type,
                "images": [
                    {
                        "src": args.image_url
                    }
                ]
            }
        }

        r = requests.post(url=self.url, json=data)

        return r.json()


API_HANDLERS = [Version, Products]
