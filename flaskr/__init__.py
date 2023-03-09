from flask import Flask
from os import environ
from flask_simple_geoip import SimpleGeoIP
from flaskr.model import connect_to_db

app = Flask(__name__)
app.secret_key = environ["SECRET_KEY"]
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"]=False
app.config["GEOIPIFY_API_KEY"] = environ["GEOIPIFY_API_KEY"]
connect_to_db(app)

simple_geoip = SimpleGeoIP(app)

from flaskr import views