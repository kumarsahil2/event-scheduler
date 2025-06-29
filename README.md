# 📅 Event Scheduler System

This is a Python Flask-based backend application that allows users to create, view, update, delete, and search events. The application also supports recurring events, sends email reminders for upcoming events, and persists data in a local JSON file.

---

## ✅ Features

- Create, read, update, delete events (CRUD)
- Recurring events: daily, weekly, monthly
- Reminder system: alerts within 1 hour of event start
- Email notifications (via Gmail SMTP)
- Persistent data storage (`storage.json`)
- Search by title or description
- Unit tests using Pytest
- Postman-compatible API

---

## 🛠️ Requirements

- Python 3.7+
- Flask
- APScheduler
- python-dotenv
- pytest (for testing)

Install all dependencies:

```bash
pip install -r requirements.txt

=================================================================================
Setup Email for Notifications
Step 1: Enable 2-Step Verification in your Gmail account
Step 2: Generate an App Password
Go to: https://myaccount.google.com/apppasswords

Choose app: "Mail"

Choose device: "Other"

Copy the generated 16-digit password
============================================================
Create a .env file

EMAIL_ADDRESS=youremail@gmail.com
EMAIL_PASSWORD=your_generated_app_password
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587

=========================================================
▶️ How to Run the Application
Start the Flask server:  python app.py
Server will run at: http://127.0.0.1:5000

A background thread will also start checking for upcoming reminders every minute.

============================================================
🧪 Example Commands (Postman)
✅ Create an Event

POST /events
Example:
POSTMAN -X POST http://127.0.0.1:5000/events \
-Header-Section "Content-Type: application/json" \
-Body-Raw-JSON '{
  "title": "Project Demo",
  "description": "Final year project demo",
  "start_time": "2025-07-01T10:00:00",
  "end_time": "2025-07-01T11:00:00",
  "recurrence": "daily",
  "email": "youremail@gmail.com"
}'
---------------------------------------------------------
📋 List All Events
GET /events
POSTMAN http://127.0.0.1:5000/events
✅ Sample output:
json
[
  {
    "id": "e7fa0c78-1cda-4e1c-abc9-f1c2a35a67b7",
    "title": "Project Demo",
    "description": "Final year project demo",
    "start_time": "2025-07-01T10:00:00",
    "end_time": "2025-07-01T11:00:00",
    "recurrence": "daily",
    "email": "youremail@gmail.com"
  }
]

--------------------------------------------------------------------
✏️ Update an Event
PUT /events/<event_id>

POSTMAN -X PUT http://127.0.0.1:5000/events/<event_id> \
-Header section "Content-Type: application/json" \
-Body-Raw-Json '{"title": "Updated Meeting"}'

----------------------------------------------------------------------
❌ Delete an Event
DELETE /events/<event_id>
POSTMAN -X DELETE http://127.0.0.1:5000/events/<event_id>

-----------------------------------------------------------------------
🔍 Search Events

GET /events/search?q=demo
POSTMAN "http://127.0.0.1:5000/events/search?q=demo"
Reminder Example Output
Every minute, reminders will be checked. Sample output:

 Reminder: 'Project Demo' at 2025-07-01T10:00:00
 Email sent to youremail@gmail.com
-----------------------------------------------------------------------------
-----------------------------------------------------------------------------
🧪 Run Tests
Use Pytest to test your API:
pytest test_app.py
✅ Example output:

diff
Copy
Edit
============================= test session starts ==============================
collected 1 item

test_app.py .                                                            [100%]

============================== 1 passed in 0.41s ===============================

-------------------------------------------------------------------------------------------------
```
