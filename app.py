from flask import Flask, jsonify, request
from prometheus_flask_exporter import PrometheusMetrics
import os

app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Video Platform API', version='1.1.0')

# Load the secret from the environment (Injected by Kubernetes)
VALID_API_KEY = os.environ.get('API_KEY')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "active", "service": "video-metadata-api"})

@app.route('/secure-data', methods=['GET'])
def secure_data():
    # Zero Trust: Check if the request has the correct header
    client_key = request.headers.get('x-api-key')
    
    if client_key == VALID_API_KEY:
        return jsonify({"status": "success", "data": "Top secret video metadata!"})
    else:
        return jsonify({"status": "error", "message": "Unauthorized. Invalid or missing API Key."}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
