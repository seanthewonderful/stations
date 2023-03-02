from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import os

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """The users table"""
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    username = db.Column(db.String(50))
    password = db.Column(db.String(250))
    email = db.Column(db.String(75))
    zipcode = db.Column(db.String(5), nullable=True)
    
    def __repr__(self):
        return f"<User: email={self.email}, zipcode={self.zipcode}>"
    
    
class Station(db.Model):
    """The [gas] station table"""
    
    __tablename__ = "stations"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    name = db.Column(db.String(50))
    fuel_type = db.Column(db.String(75))
    ev_charging = db.Column(db.Boolean)
    ev_charge_type = db.Column(db.String(100))
    cuisines = db.Column(db.String(200), nullable=True)
    coffee_quality = db.Column(db.Integer, nullable=True)
    showers = db.Column(db.Boolean)
    
    fuel_options = db.relationship('Fuel', secondary='stations_fuels', back_populates='stations')
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    
class Bathroom(db.Model):
    """The table of bathrooms"""
    
    __tablename__ = "bathrooms"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    gender = db.Column(db.String(25))
    num_stalls = db.Column(db.Integer, nullable=True)
    num_urinals = db.Column(db.Integer, nullable=True)
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    
class Shower(db.Model):
    """The table of showers"""
    
    __tablename__ = "showers"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    size = db.Column(db.Integer) # Small, medium, large? -> 1,2,3
    cleanliness = db.Column(db.Integer) # 1-5 cleanliness rating? Or probably another rating table
    price = db.Column(db.Numeric, nullable=True)
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    
class Fuel(db.Model):
    """Table for each type of fuel"""
    
    __tablename__ = "fuels"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(25))
    octane = db.Column(db.Integer, nullable=True)
    
    stations = db.relationship('Station', secondary='stations_fuels', back_populates='fuel_options')
    
    def __repr__(self):
        return f"<Fuel type:{self.type}, octane:{self.octane}>"
    
    
class StationFuel(db.Model):
    """Junction table to create many-many relationship between stations and fuels"""
    
    __tablename__ = "stations_fuels"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    station_id = db.Column(db.Integer, db.ForeignKey('stations.id'))
    fuel_id = db.Column(db.Integer, db.ForeignKey('fuels.id'))
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    
class EVPlug(db.Model):
    """Table for each type of EV plug"""
    
    __tablename__ = "ev_plugs"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    type = db.Column(db.String(50))
    charge_rate = db.Column(db.Integer)
    
    supported_vehicles = db.relationship('ElectricVehicle', secondary='vehicle_plug_junction', back_populates='plugs')
    
    def __repr__(self) -> str:
        return super().__repr__()
    
    
class ElectricVehicle(db.Model):
    """Table for each EV to relate to 'ev_plugs' """
    
    __tablename__ = "electric_vehicles"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    make = db.Column(db.String(30))
    model = db.Column(db.String(50))
    year = db.Column(db.Integer)
    
    plugs = db.relationship('EVPlug', secondary='vehicle_plug_junction', back_populates='supported_vehicles')
    
    def __repr__(self) -> str:
        return f"<EV: {self.year} {self.make} {self.model}>"
    
    
class VehiclePlugJunction(db.Model):
    """Junction table to create many-many relationship between electric_vehicles and ev_plugs"""
    
    __tablename__ = "vehicle_plug_junction"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
    ev_id = db.Column(db.Integer, db.ForeignKey('electric_vehicles.id'))
    plug_id = db.Column(db.Integer, db.ForeignKey('ev_plugs.id'))
    notes = db.Column(db.String, nullable=True)
    
    def __repr__(self) -> str:
        return super().__repr__()
    

"""DB Connection Function"""
def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['POSTGRES_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['FLASK_DEBUG'] = True
    db.app = app
    db.init_app(app)
    

if __name__ == "__main__":
    os.system('source config.sh')
    from flaskr import app
    connect_to_db(app=app)
    print("Connected to DB: stationation")