from datetime import datetime
import uuid

# model.py
class Event:
    def __init__(self, title, description, start_time, end_time, recurrence=None, email=None, id=None):
        self.id = id or str(uuid.uuid4())
        self.title = title
        self.description = description
        self.start_time = start_time
        self.end_time = end_time
        self.recurrence = recurrence
        self.email = email  # <-- Add email field

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "recurrence": self.recurrence,
            "email": self.email
        }

    @staticmethod
    def from_dict(data):
        return Event(**data)
