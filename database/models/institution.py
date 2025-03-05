# database/models/institution.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database.base import Base
from database.models.country import Country  # Импорт модели

class Institution(Base):
    __tablename__ = 'institutions'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    country_id = Column(Integer, ForeignKey('countries.id'))
    
    # Связь с Country
    country = relationship("Country", back_populates="institutions")