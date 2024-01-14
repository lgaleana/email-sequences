import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import database
from datetime import datetime
from fastapi.testclient import TestClient
from main import app
from unittest.mock import patch


@pytest.fixture
def session():
    engine = create_engine('sqlite:///:memory:')
    database.EmailSchedule.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def test_email_schedule(session):
    email_schedule = database.EmailSchedule(email='test@example.com', subject='Test', body='This is a test.', scheduled_time=datetime.now())
    session.add(email_schedule)
    session.commit()
    assert session.query(database.EmailSchedule).count() == 1


@patch('database.add_email_schedule')
@patch('database.SessionLocal')
def test_create_email_schedule(mock_add_email_schedule, mock_session_local):
    mock_session = mock_session_local.return_value
    mock_session.commit.return_value = None

    client = TestClient(app)
    response = client.post('/email-schedules', json={'email': 'test@example.com', 'subject': 'Test', 'body': 'This is a test.', 'scheduled_time': '2022-01-01T00:00:00'})

    assert response.status_code == 200
    assert response.json() == {'message': 'Email schedule created successfully.'}
    mock_add_email_schedule.assert_called_once()