@app.post("/add-document/")
async def add_document(data: dict, db: Session = Depends(get_db)):
    new_document = Document(data=data)
    db.add(new_document)
    db.commit()
    db.refresh(new_document)
    return new_document
