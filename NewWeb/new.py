from flask import Flask, redirect, url_for, render_template, request
from stockdata import stockdata
import yfinance as yf
import pandas as pd 

app = Flask(__name__)



@app.route("/")
def homepages():
    return render_template("index.html", content = "sjndaskndsamdbasndbmas")

@app.route("/updatedata", methods=["POST", "GET"])
def update_data():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("usersss", usr=user))
    else:
        return render_template("update.html")
    
@app.route("/<usr>")
def usersss(usr):
    return f"<h1>{usr}</h1>" 

app.register_blueprint(stockdata)




# @app.route("/<name>")
# def home(name):
#     return render_template("index.html", content = name)


# @app.route("/<name>")
# def home(name):
#     return render_template("index.html", content=name, hehe = 2)

# @app.route("/<name>")
# def user(name):
#     return f"Hellos {name}"

# @app.route("/admin")
# def admin():
#     return redirect(url_for("user", name="Admin"))

if __name__ == "__main__":
    app.run(debug=True)