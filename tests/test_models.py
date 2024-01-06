from models import EmailSchedule
from datetime import datetime


def test_email_schedule_model():
    email_schedule = EmailSchedule(
        id=1,
        email='test@example.com',
        subject='Test Email',
        body='This is a test email.',
        scheduled_time=datetime.now()
    )
    assert email_schedule.id == 1
    assert email_schedule.email == 'test@example.com'
    assert email_schedule.subject == 'Test Email'
    assert email_schedule.body == 'This is a test email.'