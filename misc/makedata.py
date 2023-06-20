import os

# Directory path for the 'data' directory
data_directory = '/home/admin/project/data'

# Create the 'data' directory if it doesn't exist
if not os.path.exists(data_directory):
    os.makedirs(data_directory)

# Dictionary of data file names and initial content
data_files = {
    'temperature_celsius.json': {},
    'temperature_fahrenheit.json': {},
    'humidity_percentage.json': {},
    'humidity_ratio.json': {},
    'pressure_pascals.json': {},
    'pressure_bar.json': {},
    'acceleration_meters_per_second.json': {},
    'acceleration_g_force.json': {},
    'gyroscope_radians_per_second.json': {},
    'gyroscope_degrees_per_second.json': {},
    'magnetometer_microteslas.json': {},
    'magnetometer_gauss.json': {},
    'joystick.json': {},
    'rgb_matrix.json': {},
    'led_pixels.json': {},
    'led_update.json': {},
    'led_clear.json': {}
}

# Create empty .json files in the 'data' directory
for file_name, content in data_files.items():
    file_path = os.path.join(data_directory, file_name)
    with open(file_path, 'w') as json_file:
        json_file.write('{}')
