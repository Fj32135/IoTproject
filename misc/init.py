import subprocess
import os

# Set the project directory path
PROJECT_DIR = '/home/admin/project'

def start_iot_system():
    # Change to the project directory
    os.chdir(PROJECT_DIR)

    # Start the Flask server with HTTPS using the keypair.pem file
    subprocess.Popen(['flask', 'run', '--host', '0.0.0.0', '--port', '5000', '--cert', 'keypair.pem'])

    print('IoT system has been started.')

def stop_iot_system():
    # Find the Flask server process and terminate it
    subprocess.call(['pkill', '-f', 'flask run'])

    print('IoT system has been stopped.')

# Start or stop the IoT system based on user input
choice = input('Enter "start" to start the IoT system, or "stop" to stop it: ')

if choice == 'start':
    start_iot_system()
elif choice == 'stop':
    stop_iot_system()
else:
    print('Invalid choice. Please enter either "start" or "stop".')
