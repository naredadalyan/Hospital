@app.put("/update-treatment-status/")
async def update_treatment_status(db: Session = Depends(get_db)):
    db.query(Treatment).filter(
        Treatment.end_date < datetime.now()
    ).update({"current_condition": "Выписан"})
    db.commit()
    return {"message": "Statuses updated"}
