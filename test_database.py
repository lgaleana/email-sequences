import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import database
from datetime import datetime

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
