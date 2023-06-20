from flask import Flask, render_template
import ssl

app = Flask(__name__)

# Add your Flask routes and logic here

@app.route('/')
def index():
    return render_template('index.html')

# Start the Flask app with HTTPS
if __name__ == '__main__':
    # Load the key and certificate
    context = ('/home/admin/project/ssl/ssl_certificate.crt', '/home/admin/project/ssl/private_key.key')

    # Run the Flask app with HTTPS
    app.run(host='0.0.0.0', port=443, ssl_context=context)

