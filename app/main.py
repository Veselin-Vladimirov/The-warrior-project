from flask import Flask, rendertemplate, request, jsonify
from models.sensor import Sensor
from models.db import Base, engine, Session
from flasksqlalchemy import SQLAlchemy
import os
from sqlalchemy.orm import sessionmaker

print("Database URI:", os.environ.get('SQLALCHEMYDATABASEURI'))

app = Flask(name)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
print("Database URI:", os.environ.get('SQLALCHEMY_DATABASE_URI'))
db = SQLAlchemy(app)
Session = sessionmaker(bind=db.engine)


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
            session = Session()
            new_sensor = Sensor(temperature=temperature)
            session.add(new_sensor)
            session.commit()
            session.close()
            return jsonify({'message': 'Temperature data received successfully'}), 200
        else:
            return jsonify({'error': 'Temperature data not provided'}), 400


if __name == '__main':
    app.run(host='0.0.0.0', port=5564, debug=True)

print("Database URI:", os.environ.get('SQLALCHEMY_DATABASE_URI'))