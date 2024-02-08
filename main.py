from fastapi import FastAPI, HTTPException, Request
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from database import EmailSchedule, add_email_schedule
from datetime import datetime
from utils import str_to_datetime

app = FastAPI()
templates = Jinja2Templates(directory="templates")

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
def read_root(request: Request):
    return templates.TemplateResponse("email_schedule_form.html", {"request": request})


@app.post("/email-schedules", response_model=EmailScheduleResponse)
def create_email_schedule(request: Request, email_schedule_request: EmailScheduleRequest):
    email_schedule_request.scheduled_time = str_to_datetime(email_schedule_request.scheduled_time)
    email_schedule = EmailSchedule(**email_schedule_request.dict())
    created_email_schedule = add_email_schedule(email_schedule)
    return created_email_schedule