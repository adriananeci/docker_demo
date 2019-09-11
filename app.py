from flask import Flask
import os
import socket

app = Flask(__name__)


@app.route("/")
def hello():
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname of container:</b> {hostname}<br/>" \
           "<b>IP of container:</b> {ip}<br/>"

    return html.format(
                name=os.getenv("NAME", "world"),
                hostname=socket.gethostname(),
                ip=socket.gethostbyname(socket.gethostname())
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)