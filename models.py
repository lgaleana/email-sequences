from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class EmailSchedule(Base):
    __tablename__ = 'email_schedules'

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    body = Column(String, nullable=False)
    scheduled_time = Column(DateTime, nullable=False)