import time
import random

from flask import Flask, jsonify

# import newrelic.agent
# newrelic.agent.initialize()

from aws_xray_sdk.core import xray_recorder, patch_all
from aws_xray_sdk.ext.flask.middleware import XRayMiddleware

xray_recorder.configure(service="py-payment")
patch_all()

app = Flask(__name__)
XRayMiddleware(app, xray_recorder)


@app.route("/pay")
def pay():
    time.sleep(0.25)

    if random.random() < 0.3:
        time.sleep(0.4)

    return jsonify({
        "service": "payment",
        "status": "paid",
        "authorization_id": f"AUTH-{random.randint(1000, 9999)}"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)