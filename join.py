@app.get("/patients-with-doctors/")
async def get_patients_with_doctors(db: Session = Depends(get_db)):
    return db.query(Patient.name, Doctor.name, Treatment.diagnosis).join(
        Treatment, Patient.id == Treatment.patient_id
    ).join(
        Doctor, Treatment.doctor_id == Doctor.id
    ).all()
