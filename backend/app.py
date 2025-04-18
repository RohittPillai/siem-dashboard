from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime, timedelta

app = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['siem']
logs_collection = db['logs']
alerts_collection = db['alerts']

# Helper function to convert ObjectId to string
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@app.route('/')
def home():
    return "🚀 SIEM Flask API is running!"

# Ingest log + detect brute-force
@app.route('/ingest-log', methods=['POST'])
def ingest_log():
    data = request.json
    data["timestamp"] = datetime.utcnow()  # Add timestamp

    print("📥 Received log:", data)

    # Save the log
    logs_collection.insert_one(data)

    # Detection logic: brute-force (3+ failed logins from same IP in 60 seconds)
    source_ip = data.get("source_ip")
    event_type = data.get("event")

    if source_ip and event_type == "login_failed":
        one_minute_ago = datetime.utcnow() - timedelta(seconds=60)

        recent_failures = logs_collection.count_documents({
            "source_ip": source_ip,
            "event": "login_failed",
            "timestamp": {"$gte": one_minute_ago}
        })

        if recent_failures >= 3:
            alert = {
                "source_ip": source_ip,
                "type": "brute_force_attempt",
                "message": f"Detected {recent_failures} failed logins from {source_ip} in 60 seconds",
                "timestamp": datetime.utcnow()
            }
            alerts_collection.insert_one(alert)
            print("🚨 Alert Raised:", alert["message"])
            return jsonify({
                "status": "Log saved to MongoDB",
                "alert": alert["message"]
            }), 200

    return jsonify({
        "status": "Log saved to MongoDB",
        "log_id": str(data.get("_id", ""))
    }), 200

# View all logs
@app.route('/logs', methods=['GET'])
def get_logs():
    logs = list(logs_collection.find())
    serialized_logs = [serialize_doc(log) for log in logs]
    return jsonify(serialized_logs), 200

# Optional: View all alerts
@app.route('/alerts', methods=['GET'])
def get_alerts():
    alerts = list(alerts_collection.find())
    serialized_alerts = [serialize_doc(alert) for alert in alerts]
    return jsonify(serialized_alerts), 200

if __name__ == '__main__':
    app.run(debug=True)
