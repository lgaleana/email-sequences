from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import EmailSchedule, add_email_schedule
from datetime import datetime

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class EmailScheduleBase(BaseModel):
    email: str
    subject: str
    body: str
    scheduled_time: str


@app.post("/email-schedules")
def create_email_schedule(email_schedule: EmailScheduleBase):
    email_schedule_dict = email_schedule.dict()
    email_schedule_dict["scheduled_time"] = datetime.fromisoformat(email_schedule_dict["scheduled_time"])
    email_schedule = EmailSchedule(**email_schedule_dict)
    add_email_schedule(email_schedule)
    return {"message": "Email schedule created successfully."}