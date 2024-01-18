from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///email_schedules.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class EmailSchedule(Base):
    __tablename__ = 'email_schedules'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    subject = Column(String)
    body = Column(String)
    scheduled_time = Column(DateTime)


def add_email_schedule(email_schedule: EmailSchedule, session: Session = None):
    if session is None:
        session = SessionLocal()
    session.add(email_schedule)
    session.commit()
    session.refresh(email_schedule)
    session.close()
    return email_schedule