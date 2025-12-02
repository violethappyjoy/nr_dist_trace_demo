# payment/app.py
import time
import random

import newrelic.agent
newrelic.agent.initialize()

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/pay")
def pay():
    # Simulate external API or payment gateway latency
    time.sleep(0.25)

    # Randomly be a bit slow to make traces interesting
    if random.random() < 0.3:
        time.sleep(0.4)

    return jsonify({
        "service": "payment",
        "status": "paid",
        "authorization_id": f"AUTH-{random.randint(1000, 9999)}"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)