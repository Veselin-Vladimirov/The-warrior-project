from flask import Flask, render_template, request, jsonify
from .models.sensor import Sensor
from .models.db import db, engine, Base
import os

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    Base.metadata.create_all(engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temp-graph')
def temp_graph():
    return render_template('temp-graph.html')

@app.route('/sensor-data')
def get_sensor_data():
    sensors = Sensor.query.all()
    sensor_data = {
        'temperatures': [sensor.temperature for sensor in sensors],
        'humidities': [sensor.humidity for sensor in sensors],
        'wind_speeds': [sensor.wind_speed for sensor in sensors],
        'pressures': [sensor.pressure for sensor in sensors]
    }
    return jsonify(sensor_data)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        data = request.json
        sensor = Sensor(
            temperature=data.get('temperature'),
            humidity=data.get('humidity'),
            wind_speed=data.get('wind_speed'),
            pressure=data.get('pressure')
        )
        db.session.add(sensor)
        db.session.commit()
        return jsonify({'message': 'Sensor data received successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5564, debug=True, use_reloader=True)
