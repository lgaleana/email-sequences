from sqlalchemy import Column, Integer, String, DateTime
from .database import Base

class EmailSchedule(Base):
    __tablename__ = "email_schedules"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    subject = Column(String)
    body = Column(String)
    scheduled_time = Column(DateTime)
