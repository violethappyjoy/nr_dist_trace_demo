import time

# import newrelic.agent
# newrelic.agent.initialize()

from flask import Flask, jsonify

from aws_xray_sdk.core import xray_recorder, patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

xray_recorder.configure(service="py-cart")
patch_all()

app = Flask(__name__)
XRayMiddleware(app, xray_recorder)


@app.route("/cart")
def get_cart():
    time.sleep(0.15)
    items = [
        {"sku": "book-123", "qty": 1, "price": 10.0},
        {"sku": "pen-456", "qty": 2, "price": 1.5},
    ]
    return jsonify({"service": "cart", "items": items})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)