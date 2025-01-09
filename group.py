@app.get("/patients-grouped-by-status/")
async def group_patients_by_status(db: Session = Depends(get_db)):
    return db.query(Patient.social_status, func.count(Patient.id)).group_by(
        Patient.social_status
    ).all()
