# cart/app.py
import time

import newrelic.agent
newrelic.agent.initialize()

from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/cart")
def get_cart():
    # Pretend we hit a database
    time.sleep(0.15)
    items = [
        {"sku": "book-123", "qty": 1, "price": 10.0},
        {"sku": "pen-456", "qty": 2, "price": 1.5},
    ]
    return jsonify({"service": "cart", "items": items})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)