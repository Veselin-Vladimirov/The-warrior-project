import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Replace 'your_new_user', 'your_password', 'your_database', and 'public' with your actual values
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
db = SQLAlchemy(app)

class Sensor(db.Model):
    __tablename__ = 'sensor'
    __table_args__ = {'schema': 'public'}

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer, nullable=False)

with app.app_context(): 
    db.create_all()

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

# @app.route('/receive-data', methods=['POST'])
# def receive_data():
#     if request.method == 'POST':
#         data = request.json
#         temperature = data.get('temperature')
#         if temperature is not None:
#             new_sensor = Sensor(temperature=temperature)
#             db.session.add(new_sensor)
#             db.session.commit()
#             return jsonify({'message': 'Data received successfully'}), 200
#         else:
#             return jsonify({'error': 'Temperature data not provided'}), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)
