from model import db, connect_to_db, User, Station, Bathroom, Shower, Fuel, EVPlug, ElectricVehicles, VehiclePlugJunction
from app import app
from werkzeug.security import generate_password_hash
import os

os.system('source config.sh')
os.system('dropdb stationation')
os.system('createdb stationation')

connect_to_db(app=app)
app.app_context().push()
print("Connected to DB: stationation")
db.create_all()

