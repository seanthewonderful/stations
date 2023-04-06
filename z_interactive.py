from flaskr.model import db, connect_to_db, User, Station, Bathroom, Shower, Fuel, EVPlug, ElectricVehicle, VehiclePlugJunction
from flaskr import app
# from werkzeug.security import generate_password_hash
import os

os.system('source config.sh')


if __name__ == "__main__":
    from flaskr import app
    connect_to_db(app, db)
    app.app_context().push()