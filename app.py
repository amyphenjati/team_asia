
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

# Upon visiting the index page at http://127.0.0.1:5000/, the user will be presented with learn more info on mental health
@app.route("/")
def index():
    return render_template("learn_more.html")


if __name__ == "__main__":
    app.run(debug=True)
