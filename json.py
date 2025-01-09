@app.get("/search/")
async def search_documents(query: str, db: Session = Depends(get_db)):
    sql_query = "SELECT * FROM documents WHERE data::text ~* :query"
    result = db.execute(sql_query, {"query": query}).fetchall()
    return {"result": [dict(row) for row in result]}
