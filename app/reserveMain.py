from flask import Flask, render_template, request, jsonify
from models.sensor import Sensor
from models.db import Base, engine, Session

app = Flask(__name__)

with app.app_context(): 
    Base.metadata.create_all(engine)

@app.route('/')
def mainPage():
    return render_template('mainPage.html')

@app.route('/graph')
def index():
    session = Session()
    sensors = session.query(Sensor).all()
    return render_template('index.html', sensors=sensors)

@app.route('/temperature_data')
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
    app.run(port=5000, debug=True)
