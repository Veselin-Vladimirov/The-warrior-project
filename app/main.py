from flask import Flask, render_template, request, jsonify
from models.sensor import Sensor
from models.db import Base, engine, Session
from flask_sqlalchemy import SQLAlchemy
import os

print("Database URI:", os.environ.get('SQLALCHEMY_DATABASE_URI'))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
print("Database URI:", os.environ.get('SQLALCHEMY_DATABASE_URI'))

db = SQLAlchemy(app)

with app.app_context(): 
    Base.metadata.create_all(engine)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/temp-graph')
def temp_graph():
    session = Session()
    sensors = session.query(Sensor).all()
    return render_template('temp-graph.html', sensors=sensors)

@app.route('/temp-data')
def get_temperature_data():
    session = Session()
    temperatures = [sensor.temperature for sensor in session.query(Sensor).all()]
    return jsonify(temperatures)

@app.route('/receive-data', methods=['POST'])
def receive_data():
    if request.method == 'POST':
        data = request.json
        temperature = data.get('temperature')
        if temperature is not None:
            new_sensor = Sensor(temperature=temperature)
            Base.session.add(new_sensor)
            Base.session.commit()
            return jsonify({'message': 'Data received successfully'}), 200
        else:
            return jsonify({'error': 'Temperature data not provided'}), 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

print("Database URI:", os.environ.get('SQLALCHEMY_DATABASE_URI'))
