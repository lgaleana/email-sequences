from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, Session, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine('sqlite:///:memory:')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class EmailSchedule(Base):
    __tablename__ = 'email_schedules'

    id = Column(Integer, primary_key=True)
    email = Column(String)
    subject = Column(String)
    body = Column(String)
    scheduled_time = Column(DateTime)


def add_email_schedule(email_schedule: EmailSchedule):
    db: Session = SessionLocal()
    db.add(email_schedule)
    db.commit()