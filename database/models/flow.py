# database/models/flow.py
from sqlalchemy import Column, Integer, String, ForeignKey, DATE
from sqlalchemy.orm import relationship
from database.base import Base
from database.models.asset import Asset
from database.models.institution import Institution

class Flow(Base):
    __tablename__ = 'flows'
    
    id = Column(Integer, primary_key=True)
    asset_id = Column(Integer, ForeignKey('assets.id'))
    institution_id = Column(Integer, ForeignKey('institutions.id'))
    amount=Column(Integer)
    date=Column(DATE)
    # Связи
    asset = relationship("Asset", back_populates="flows")
    institution = relationship("Institution")