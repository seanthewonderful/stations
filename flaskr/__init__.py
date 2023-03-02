from os import environ, system
from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect


app = Flask(__name__)
app.secret_key = environ["SECRET_KEY"]
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False


@app.route('/')
def home():
    """Homepage"""
    variable = ["Bucee's", "QuikTrip", "Maverik", "Pilot"]
    return render_template("homepage.html", variable=variable)



if __name__ == "__main__":
    system("source config.sh")
    app.run()