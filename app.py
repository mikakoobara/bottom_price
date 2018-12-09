from flask import Flask, render_template, request, redirect, url_for

import db

app = Flask(__name__)


@app.route("/")
def top():
    products = db.find_all_products()
    return render_template("top.html",  # /にアクセスが来たらtemplates内のindex.htmlが開く
                           products=products)


@app.route("/add", methods=["POST"])
def add_product():
    name = request.form["name"]
    price = request.form["price"]
    jan_code = request.form["jan_code"]

    db.add_products(name, price, jan_code)
    return redirect(url_for("top"))


@app.route("/find", methods=["POST"])
def find_product():
    # name = request.form["name"]
    # price = request.form["price"]
    jan_code = request.form["jan_code"]

    product = db.find_products(jan_code)
    return render_template("index.html",
                           name=product[0], price=product[1], jan_code=product[2])


if __name__ == "__main__":
    app.run(debug=True)
