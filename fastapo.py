from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PatientCreate(BaseModel):
    name: str
    birth_year: int
    social_status: str

@app.post("/patients")
async def create_patient(patient: PatientCreate):
    return {"message": "Пациент добавлен", "data": patient}
