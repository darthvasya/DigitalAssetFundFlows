# database/models/asset.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database.base import Base

class Asset(Base):
    __tablename__ = 'assets'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    
    # Связь с Flow
    flows = relationship("Flow", back_populates="asset")