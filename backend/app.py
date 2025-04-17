from flask import Flask, request, jsonify

# Create the Flask app
app = Flask(__name__)

# Route 1: Home / Health check
@app.route('/')
def home():
    return "🚀 SIEM Flask API is running!"

# Route 2: Log ingestion endpoint
@app.route('/ingest-log', methods=['POST'])
def ingest_log():
    data = request.json  # Read the incoming JSON log
    print("📥 Received log:", data)  # Print it in the terminal

    # Just send back the same log for now
    return jsonify({"status": "Log received", "log": data}), 200

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
