from flask import Flask, request, jsonify
from models import Event
from event_manager import EventManager
from reminders import start_reminder_checker
from dotenv import load_dotenv
from datetime import datetime
import threading

app = Flask(__name__)
manager = EventManager()
load_dotenv()
start_reminder_checker(manager)  # Background task

@app.route("/events", methods=["POST"])
def create_event():
    data = request.json
    try:
        event = Event(
            title=data["title"],
            description=data["description"],
            start_time=data["start_time"],
            end_time=data["end_time"],
            recurrence=data.get("recurrence"),
            email=data.get("email")
        )
        manager.add_event(event)
        return jsonify(event.to_dict()), 201
    except KeyError:
        return jsonify({"error": "Missing required fields"}), 400

@app.route("/events", methods=["GET"])
def list_events():
    return jsonify([e.to_dict() for e in manager.get_all_events()])

@app.route("/events/<event_id>", methods=["PUT"])
def update_event(event_id):
    data = request.json
    updated = manager.update_event(event_id, data)
    if updated:
        return jsonify(updated.to_dict())
    return jsonify({"error": "Event not found"}), 404

@app.route("/events/<event_id>", methods=["DELETE"])
def delete_event(event_id):
    manager.delete_event(event_id)
    return jsonify({"message": "Event deleted"}), 200

@app.route("/events/search", methods=["GET"])
def search_events():
    query = request.args.get("q", "")
    results = manager.search(query)
    return jsonify([e.to_dict() for e in results])

if __name__ == "__main__":
    app.run(debug=True)
