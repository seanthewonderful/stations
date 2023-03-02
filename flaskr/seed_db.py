from model import db, connect_to_db, User, Station, Bathroom, Shower, Fuel, EVPlug, ElectricVehicle, VehiclePlugJunction
from flaskr import app
from werkzeug.security import generate_password_hash
import os

os.system('source config.sh')
os.system('dropdb stationation')
os.system('createdb stationation')

connect_to_db(app=app)
app.app_context().push()
print("Connected to DB: stationation")
db.create_all()

plug1 = EVPlug(type="Tesla", charge_rate=250)
plug2 = EVPlug(type="Chademo", charge_rate=150)
plug3 = EVPlug(type="J1772", charge_rate=30)

car1 = ElectricVehicle(make="Tesla", model="3", year=2021)
car2 = ElectricVehicle(make="Tesla", model="S", year=2015)
car3 = ElectricVehicle(make="Hyundai", model="Ioniq 5", year=2022)
car4 = ElectricVehicle(make="Nissan", model="Leaf", year=2015)

db.session.add_all([plug1, plug2, plug3, car1, car2, car3, car4])
db.session.commit()

vpj1 = VehiclePlugJunction(ev_id=1, plug_id=1)
vpj2 = VehiclePlugJunction(ev_id=2, plug_id=1)
vpj3 = VehiclePlugJunction(ev_id=3, plug_id=2)
vpj4 = VehiclePlugJunction(ev_id=3, plug_id=3)
vpj5 = VehiclePlugJunction(ev_id=4, plug_id=3)

db.session.add_all([vpj1, vpj2, vpj3, vpj4, vpj5])
db.session.commit()
