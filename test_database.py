import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import database
from datetime import datetime

@pytest.fixture
def db():
    engine = create_engine('sqlite:///:memory:')
    database.EmailSchedule.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

def test_email_schedule(db):
    email_schedule = database.EmailSchedule(email='test@example.com', subject='Test', body='This is a test.', scheduled_time=datetime.now())
    db.add(email_schedule)
    db.commit()
    assert db.query(database.EmailSchedule).count() == 1
