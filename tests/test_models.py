from models import EmailSchedule
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

def test_email_schedule_model():
    engine = create_engine('sqlite:///:memory:')
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    test_email_schedule = EmailSchedule(
        email='test@example.com',
        subject='Test Email',
        body='This is a test email.',
        scheduled_time=datetime.datetime.now()
    )

    session.add(test_email_schedule)
    session.commit()

    assert session.query(EmailSchedule).count() == 1