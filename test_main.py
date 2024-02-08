from unittest.mock import Mock, patch
from fastapi.testclient import TestClient
from main import app
from datetime import datetime
from utils import str_to_datetime

client = TestClient(app)

@patch('main.add_email_schedule')
def test_create_email_schedule(mocked_add_email_schedule):
    scheduled_time = str(datetime.now())
    mocked_add_email_schedule.return_value = {
        "id": 1,
        "email": "test@example.com",
        "subject": "Test",
        "body": "This is a test.",
        "scheduled_time": scheduled_time
    }
    response = client.post(
        "/email-schedules",
        json={
            "email": "test@example.com",
            "subject": "Test",
            "body": "This is a test.",
            "scheduled_time": scheduled_time
        },
    )
    assert response.status_code == 200
    assert response.json()['id'] == 1
    assert response.json()['email'] == 'test@example.com'
    assert response.json()['subject'] == 'Test'
    assert response.json()['body'] == 'This is a test.'
    assert 'scheduled_time' in response.json()
    mocked_add_email_schedule.assert_called_once()


def test_form_display():
    response = client.get("/")
    assert response.status_code == 200
    assert 'Schedule an Email' in response.text


@patch('main.add_email_schedule')
def test_form_submission(mocked_add_email_schedule):
    scheduled_time = str(datetime.now())
    mocked_add_email_schedule.return_value = {
        "id": 1,
        "email": "test@example.com",
        "subject": "Test",
        "body": "This is a test.",
        "scheduled_time": scheduled_time
    }
    response = client.post(
        "/email-schedules",
        json={
            "email": "test@example.com",
            "subject": "Test",
            "body": "This is a test.",
            "scheduled_time": scheduled_time
        }
    )
    assert response.status_code == 200
    assert response.json()['id'] == 1
    assert response.json()['email'] == 'test@example.com'
    assert response.json()['subject'] == 'Test'
    assert response.json()['body'] == 'This is a test.'
    assert 'scheduled_time' in response.json()
    mocked_add_email_schedule.assert_called_once()