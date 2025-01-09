from sqlalchemy import Column, Integer, JSON
from database import Base

class Document(Base):
    __tablename__ = "documents"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(JSON)
