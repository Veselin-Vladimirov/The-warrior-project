import random
import threading
import time
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Replace 'your_new_user', 'your_password', 'your_database', and 'public' with your actual values
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://student:student@localhost:5432/sensor_db'
db = SQLAlchemy(app)

class Sensor(db.Model):
    __tablename__ = 'sensor'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer, nullable=False)

with app.app_context(): 
    db.create_all()

'''
def continuous_sensor_data():
    with app.app_context():
        while True:
            # Generate random values for temperature
            temperature = random.randint(1, 100)
    
            # Add the sensor to the database
            new_sensor = Sensor(temperature=temperature)
            db.session.add(new_sensor)
            db.session.commit()

            # Sleep for some time before adding the next temperature data
            time.sleep(1)  # Adjust the sleep time as needed


continuous_sensor_thread = threading.Thread(target=continuous_sensor_data)
continuous_sensor_thread.daemon = True  # Daemonize the thread so it stops with the main program
continuous_sensor_thread.start()
'''

@app.route('/')
def mainPage():
    return render_template('mainPage.html')

@app.route('/graph')
def index():
    sensors = Sensor.query.all()
    return render_template('index.html', sensors=sensors)

@app.route('/temperature_data')
def get_temperature_data():
    temperatures = [sensor.temperature for sensor in Sensor.query.all()]
    return jsonify(temperatures)

if __name__ == '__main__':
    app.run(debug=True)
