from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId  # ✅ import this

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017/")
db = client['siem']
logs_collection = db['logs']

def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
    return doc


@app.route('/')
def home():
    return "🚀 SIEM Flask API is running!"

@app.route('/ingest-log', methods=['POST'])
def ingest_log():
    data = request.json
    print("📥 Received log:", data)

    # Insert the log into MongoDB
    result = logs_collection.insert_one(data)

    # Return custom JSON response
    return jsonify({
        "status": "Log saved to MongoDB",
        "log_id": str(result.inserted_id)  # ✅ convert ObjectId to string
    }), 200

@app.route('/logs', methods=['GET'])
def get_logs():
    logs = list(logs_collection.find())
    serialized_logs = [serialize_doc(log) for log in logs]
    return jsonify(serialized_logs), 200


if __name__ == '__main__':
    app.run(debug=True)
