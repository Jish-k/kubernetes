from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def hello():
    pod_name = socket.gethostname()
    return f"<h1>Hello from Flask!</h1><p>Running on Pod: {pod_name}</p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)