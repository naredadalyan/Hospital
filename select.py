@app.get("/patients/filter/")
async def get_filtered_patients(diagnosis: str, condition: str, db: Session = Depends(get_db)):
    return db.query(Patient).filter(
        Patient.diagnosis == diagnosis, 
        Patient.current_condition == condition
    ).all()
