import datetime
from app.db_models import EmailSchedule, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def test_email_schedule():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    now = datetime.datetime.now()
    email_schedule = EmailSchedule(email='test@example.com', subject='Test', body='This is a test.', scheduled_time=now)
    session.add(email_schedule)
    session.commit()

    assert session.query(EmailSchedule).filter_by(email='test@example.com').first() is not None
