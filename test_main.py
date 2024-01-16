from unittest.mock import Mock, patch
from fastapi.testclient import TestClient
from main import app
from datetime import datetime

client = TestClient(app)

@patch('main.add_email_schedule')
def test_create_email_schedule(mocked_add_email_schedule):
    response = client.post(
        "/email-schedules",
        json={
            "email": "test@example.com",
            "subject": "Test",
            "body": "This is a test.",
            "scheduled_time": str(datetime.now())
        },
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Email schedule created successfully."}
    mocked_add_email_schedule.assert_called_once()