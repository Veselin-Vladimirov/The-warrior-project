from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)

from models.sensor import Sensor
from models.db import Base, engine

with app.app_context():
    Base.metadata.create_all(engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temp-graph')
def temp_graph():
    sensors = Sensor.query.all()
    return render_template('temp-graph.html', sensors=sensors)

@app.route('/temp-data')
def get_temperature_data():
    temperatures = [sensor.temperature for sensor in Sensor.query.all()]
    return jsonify(temperatures)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        data = request.json
        temperature = data.get('temperature')
        if temperature is not None:
            new_sensor = Sensor(temperature=temperature)
            db.session.add(new_sensor)
            db.session.commit()
            return jsonify({'message': 'Temperature data received successfully'}), 200
        else:
            return jsonify({'error': 'Temperature data not provided'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5564, debug=True)
