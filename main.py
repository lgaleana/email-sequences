from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import EmailSchedule, add_email_schedule

app = FastAPI()


class EmailScheduleRequest(BaseModel):
    email: str
    subject: str
    body: str
    scheduled_time: str


class EmailScheduleResponse(BaseModel):
    id: int
    email: str
    subject: str
    body: str
    scheduled_time: str


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/email-schedules", response_model=EmailScheduleResponse)
def create_email_schedule(email_schedule_request: EmailScheduleRequest):
    email_schedule = EmailSchedule(**email_schedule_request.dict())
    created_email_schedule = add_email_schedule(email_schedule)
    return created_email_schedule