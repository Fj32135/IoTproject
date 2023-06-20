from sense_emu import SenseHat
from flask import jsonify

sense = SenseHat()

def set_temperature(temperature):
    # Rest of the code...

    # Set the Sense HAT temperature value
    sense.temperature = temperature

    # Write the updated temperature value to the .json data file
    data = {
        'temperature': temperature,
    }

    with open(f"{DATA_DIR}/temperature_celsius.json", 'w') as file:
        json.dump(data, file)