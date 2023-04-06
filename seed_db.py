from flaskr.model import db, connect_to_db, User, Station, Bathroom, Shower, Fuel, EVPlug, ElectricVehicle, VehiclePlugJunction
from flaskr import app
# from werkzeug.security import generate_password_hash
import os


os.system('dropdb stationation')
os.system('createdb stationation')

app.app_context().push()
db.create_all()

station1 = Station(name="Flying J Travel Center",
                   city="Nephi",
                   state="UT",
                   truck_parking=True,
                   ev_charging=False,
                   coffee_quality=3,
                   showers=False,
                   lat=36.68521,
                   lng=-111.83660)

station2 = Station(name="Flying J Dealer--Eagle's Landing Travel Plaza",
                   city="Scipio",
                   state="UT",
                   truck_parking=True,
                   ev_charging=False,
                   coffee_quality=2,
                   showers=False,
                   lat=39.25542,
                   lng=-112.11717)

station3 = Station(name="Maverik Adventure's First Stop",
                   city="Fillmore",
                   state="UT",
                   truck_parking=False,
                   ev_charging=True,
                   coffee_quality=3,
                   showers=False,
                   lat=38.94814,
                   lng=-112.34550)

station4 = Station(name="Beaver Valley Chevron",
                   city="Beaver",
                   state="UT",
                   truck_parking=True,
                   ev_charging=True,
                   coffee_quality=2,
                   showers=False,
                   lat=38.24965,
                   lng=-112.65284)

station5 = Station(name="Sinclair Gas Station",
                   city="Hamilton's Fort",
                   state="UT",
                   truck_parking=False,
                   ev_charging=True,
                   coffee_quality=1,
                   showers=False,
                   lat=37.60657,
                   lng=-113.16076)
db.session.add_all([station1, station2, station3, station4, station5])
db.session.commit()

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


if __name__ == "__main__":
    os.system('source config.sh')
    from flaskr import app
    connect_to_db(app=app, db=db)