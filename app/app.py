from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, static_folder='static')

app.config['SQLALCHEMY_DATABASE_URI'] = " postgresql://warrior:1122334455@postgres-db1.ctyge4wgoiux.eu-central-1.rds.amazonaws.com:5432/postgresdb"

db = SQLAlchemy(app)

class Sensor(db.Model):
    __tablename__ = 'records'
    __table_args__ = { 'schema': 'public' }

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.now)

    location = db.Column(db.Text, nullable=False)
    air_temperature = db.Column(db.Float, nullable=False)
    wind_speed = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Float, nullable=False)
    clearness = db.Column(db.Float, nullable=False)

    water_temperature = db.Column(db.Float, nullable=False)
    depth = db.Column(db.Float, nullable=False)
    pressure = db.Column(db.Float, nullable=False)

with app.app_context():
    db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graphs/<location>')
def graphs(location):
    return render_template('graphs.html', location=location)


@app.route('/locations/<location>', methods=['GET'])
def get_records_data_by_location(location):
    location_records = Sensor.query.filter_by(location=location).all()

    if not location_records:
        return jsonify({'error': 'Location could not be found!'}), 404

    data = {
        'timestamps': [record.timestamp for record in location_records],
        'air_temperatures': [record.air_temperature for record in location_records],
        'wind_speeds': [record.wind_speed for record in location_records],
        'humidities': [record.humidity for record in location_records],
        'clearness': [record.clearness for record in location_records],
        'water_temperatures': [record.water_temperature for record in location_records],
        'depths': [record.depth for record in location_records],
        'pressures': [record.pressure for record in location_records]
    }

    return jsonify(data)

@app.route('/records', methods=['POST'])
def add_new_record():
    data = request.json

    location = data.get('location')
    air_temperature = data.get('air_temperature')
    wind_speed = data.get('wind_speed')
    humidity = data.get('humidity')
    clearness = data.get('clearness')
    water_temperature = data.get('water_temperature')
    depth = data.get('depth')
    pressure = data.get('pressure')
    
    if None not in [location, air_temperature, wind_speed, humidity, water_temperature, depth, pressure]:
        new_sensor = Sensor(location=location,
                            air_temperature=air_temperature,
                            wind_speed=wind_speed,
                            humidity=humidity,
                            clearness=clearness,
                            water_temperature=water_temperature,
                            depth=depth,
                            pressure=pressure)
        
        db.session.add(new_sensor)
        db.session.commit()

        return jsonify({'message': 'Data received successfully'}), 200
    else:
        return jsonify({'error': 'One or more parameters missing'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5564, debug=True)
