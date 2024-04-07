from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

class Sensor(db.Model):
    __tablename__ = 'sensor'
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer, nullable=False)
    humidity = db.Column(db.Numeric(5,2))
    wind_speed = db.Column(db.Numeric(5,2))
    pressure = db.Column(db.Numeric(5,2))
