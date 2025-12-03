import time
import os

from flask import Flask, jsonify
import requests

from aws_xray_sdk.core import xray_recorder, patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

# Configure the recorder with a service name
xray_recorder.configure(service="py-gateway")

# Instrument common libraries like requests
patch_all()

app = Flask(__name__)

# Attach X-Ray middleware to Flask
XRayMiddleware(app, xray_recorder)


@app.route("/")
def root():
    return jsonify({"service": "gateway", "status": "ok"})


@app.route("/checkout")
def checkout():
    time.sleep(0.05)

    cart_resp = requests.get("http://cart:5001/cart")
    payment_resp = requests.get("http://payment:5002/pay")

    return jsonify({
        "service": "gateway",
        "cart": cart_resp.json(),
        "payment": payment_resp.json()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)