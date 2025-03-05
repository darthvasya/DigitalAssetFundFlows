# database/models/country.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.base import Base

class Country(Base):
    __tablename__ = 'countries'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    
    # Связь с Institution
    institutions = relationship("Institution", back_populates="country")