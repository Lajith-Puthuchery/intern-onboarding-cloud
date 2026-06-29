import os
import socket

from flask import Flask


app = Flask(__name__)

# Hands-on task: change this message, rebuild the image, and redeploy.
MESSAGE = os.environ.get("MESSAGE", "Hello from your container!")


@app.route("/")
def home():
    hostname = socket.gethostname()
    return (
        f"<h1>{MESSAGE}</h1>"
        f"<p>Served by pod/container: <b>{hostname}</b></p>"
        "<p>If you see this page, your Python app is running inside a container.</p>"
    )


@app.route("/health")
def health():
    return {"status": "ok", "hostname": socket.gethostname()}, 200


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
