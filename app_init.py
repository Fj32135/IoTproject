from flask import Flask, render_template, jsonify, request
import ssl
import os
import signal
import json
from sense_emu import SenseHat

app = Flask(__name__)

# Set the project directory path
PROJECT_DIR = '/home/admin/project'
SSL_DIR = os.path.join(PROJECT_DIR, 'ssl')

# Load the SSL files
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
ssl_context.load_cert_chain(os.path.join(SSL_DIR, 'ssl_certificate.crt'), os.path.join(SSL_DIR, 'private_key.key'))

# Initialize the Sense HAT
sense = SenseHat()

# Add your Flask routes and logic here

@app.route('/api/write', methods=['POST'])
def write_data():
    data = request.get_json()
    file_name = request.args.get('file_name')
    if file_name:
        data_file_path = os.path.join(PROJECT_DIR, 'data', file_name)
        with open(data_file_path, 'w') as file:
            json.dump(data, file)
        return jsonify({'message': 'Data written successfully'})
    else:
        return jsonify({'message': 'Invalid file name'})

@app.route('/api/update', methods=['POST'])
def update_data():
    data = request.get_json()
    file_name = request.args.get('file_name')
    if file_name:
        data_file_path = os.path.join(PROJECT_DIR, 'data', file_name)
        if os.path.exists(data_file_path):
            with open(data_file_path, 'r') as file:
                existing_data = json.load(file)
                existing_data.update(data)
            with open(data_file_path, 'w') as file:
                json.dump(existing_data, file)
            return jsonify({'message': 'Data updated successfully'})
        else:
            return jsonify({'message': 'File not found'})
    else:
        return jsonify({'message': 'Invalid file name'})



@app.route('/set_temperature/<float:temperature>', methods=['POST'])
def set_temperature(temperature):
    # Set the Sense HAT temperature value
    sense.temperature = temperature

    # Write the updated temperature value to the .json data file
    data = {
        'temperature': temperature,
    }
    data_file_path = os.path.join(PROJECT_DIR, 'data/temperature_celsius.json')
    with open(data_file_path, 'w') as file:
        json.dump(data, file)

    return jsonify({'message': 'Temperature set successfully'})

@app.route('/get_temperature', methods=['GET'])
@app.route('/get_temperature', methods=['GET'])
def get_temperature():
    temperature_data = read_data('temperature_celsius.json')
    if temperature_data is not None:
        temperature = temperature_data.get('temperature')
        return jsonify({'temperature': temperature})
    else:
        return jsonify({'message': 'Temperature data not found'})

@app.route('/')
def index():
    return render_template('index.html')

def start_iot_system():
    # Change to the project directory
    os.chdir(PROJECT_DIR)

    # Start the Flask app with HTTPS
    app.run(host='0.0.0.0', port=443, ssl_context=ssl_context)

    print('IoT system has been started.')

def stop_iot_system():
    # Find the Flask server process and terminate it
    print('IoT system has been stopped.')
    os.kill(os.getpid(), signal.SIGINT)

def handle_shutdown(signal, frame):
    # Stop the IoT system when receiving a shutdown signal (e.g., Ctrl+C)
    stop_iot_system()
    exit(0)

# Register the signal handler for shutdown
signal.signal(signal.SIGINT, handle_shutdown)

# Start the IoT system
start_iot_system()
