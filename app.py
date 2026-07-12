from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello kumar prem from Azure!"

if __name__ == "__main__":
    app.run()