import json
from datetime import datetime
from models import Event

STORAGE_FILE = 'storage.json'

class EventManager:
    def __init__(self):
        self.events = []
        self.load()

    def load(self):
        try:
            with open(STORAGE_FILE, 'r') as f:
                data = json.load(f)
                self.events = [Event.from_dict(event) for event in data]
        except (FileNotFoundError, json.JSONDecodeError):
            self.events = []

    def save(self):
        with open(STORAGE_FILE, 'w') as f:
            json.dump([event.to_dict() for event in self.events], f, indent=4)

    def add_event(self, event):
        self.events.append(event)
        self.save()

    def get_all_events(self):
        return sorted(self.events, key=lambda e: e.start_time)

    def get_event_by_id(self, event_id):
        return next((e for e in self.events if e.id == event_id), None)

    def update_event(self, event_id, data):
        event = self.get_event_by_id(event_id)
        if not event:
            return None
        for key, value in data.items():
            if hasattr(event, key):
                setattr(event, key, value)
        self.save()
        return event

    def delete_event(self, event_id):
        self.events = [e for e in self.events if e.id != event_id]
        self.save()

    def search(self, query):
        return [e for e in self.events if query.lower() in e.title.lower() or query.lower() in e.description.lower()]
