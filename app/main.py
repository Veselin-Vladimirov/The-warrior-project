from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models.sensor import Sensor

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graphs')
def graphs():
    return render_template('graphs.html')

@app.route('/sensor-data')
def get_sensor_data():
    sensors = Sensor.query.all()
    sensor_data = [{
        'temperature': sensor.temperature,
        'humidity': sensor.humidity,
        'wind_speed': sensor.wind_speed,
        'pressure': sensor.pressure
    } for sensor in sensors]
    return jsonify(sensor_data)


@app.route('/receive-data', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        data = request.json
        new_sensor = Sensor(
            temperature=data.get('temperature'),
            humidity=data.get('humidity'),
            wind_speed=data.get('wind_speed'),
            pressure=data.get('pressure')
        )
        db.session.add(new_sensor)
        db.session.commit()
        return jsonify({'message': 'Sensor data received successfully'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5564, debug=True, use_reloader=True)
