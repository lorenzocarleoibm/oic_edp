from flask import Flask, jsonify, request
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/aggregate', methods=['POST'])
def aggregate_metrics():
    data = request.json
    # Store metrics in Redis (temporary storage)
    r.set('metrics', str(data))
    return jsonify({"status": "metrics aggregated"}), 200

@app.route('/metrics', methods=['GET'])
def get_aggregated_metrics():
    data = r.get('metrics')
    return jsonify({"metrics": data.decode('utf-8')}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
