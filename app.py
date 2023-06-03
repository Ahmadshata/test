from flask import Flask
app = Flask(__name__)
#testing
@app.route("/")
def index():
    return "<p>Hello, from GKE!</p>"
