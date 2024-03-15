from models.db import Base
from sqlalchemy import Column, Integer

class Sensor(Base):
    __tablename__ = 'sensor'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    temperature = Column(Integer, nullable=False)