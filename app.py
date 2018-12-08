from flask import Flask, render_template

import db

app = Flask(__name__)


@app.route("/")
def index():
    products = db.find_all_products()
    return render_template("index.html",
                           products=products)


@app.route("/goodbye")
def goodbye():
    return "Good Bye"


if __name__ == "__main__":
    app.run(debug=True)
