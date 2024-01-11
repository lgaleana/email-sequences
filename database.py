from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EmailSchedule(Base):
    __tablename__ = 'email_schedules'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    subject = Column(String)
    body = Column(String)
    scheduled_time = Column(DateTime)
