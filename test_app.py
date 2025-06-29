import pytest
from app import app

@pytest.fixture
def client():
    return app.test_client()

def test_event_lifecycle(client):
    # Create event with email
    event_data = {
        "title": "Test Email Event",
        "description": "This is a test with email",
        "start_time": "2025-07-01T10:00:00",
        "end_time": "2025-07-01T11:00:00",
        "email": "test@example.com"
    }

    res = client.post("/events", json=event_data)
    assert res.status_code == 201
    event = res.get_json()
    assert event["title"] == "Test Email Event"
    assert event["email"] == "test@example.com"

    # List events
    res = client.get("/events")
    events = res.get_json()
    assert any(e['id'] == event['id'] for e in events)

    # Search event
    res = client.get("/events/search?q=Email")
    search_results = res.get_json()
    assert any("Email" in e['title'] for e in search_results)

    # Update event
    res = client.put(f"/events/{event['id']}", json={"title": "Updated Title"})
    assert res.status_code == 200
    assert res.get_json()["title"] == "Updated Title"

    # Delete event
    res = client.delete(f"/events/{event['id']}")
    assert res.status_code == 200

    # Confirm deletion
    res = client.get("/events")
    assert not any(e['id'] == event['id'] for e in res.get_json())
