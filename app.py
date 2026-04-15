from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# This single line automatically adds a /metrics route and tracks all HTTP traffic!
metrics = PrometheusMetrics(app)

# Add some static info about our app for Grafana to read
metrics.info('app_info', 'Video Platform API', version='1.0.0')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "active", "service": "video-metadata-api"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
