# gateway/app.py
import time
import os

import newrelic.agent
newrelic.agent.initialize()  # uses env vars like NEW_RELIC_LICENSE_KEY etc.  [oai_citation:3‡New Relic](https://docs.newrelic.com/docs/apm/agents/python-agent/python-agent-api/initialize-python-agent-api/?utm_source=chatgpt.com)

from flask import Flask, jsonify
import requests

app = Flask(__name__)


@app.route("/")
def root():
    return jsonify({"service": "gateway", "status": "ok"})


@app.route("/checkout")
def checkout():
    # Simulate a bit of work in the gateway
    time.sleep(0.05)

    cart_resp = requests.get("http://cart:5001/cart")
    payment_resp = requests.get("http://payment:5002/pay")

    return jsonify({
        "service": "gateway",
        "cart": cart_resp.json(),
        "payment": payment_resp.json()
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)