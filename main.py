from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import EmailSchedule, add_email_schedule

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


class EmailScheduleRequest(BaseModel):
    email: str
    subject: str
    body: str
    scheduled_time: str


@app.post("/email-schedules")
def create_email_schedule(email_schedule_request: EmailScheduleRequest):
    email_schedule = EmailSchedule(**email_schedule_request.dict())
    add_email_schedule(email_schedule)
    return {"message": "Email schedule created successfully."}