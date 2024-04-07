from sqlalchemy import Column, Integer
from .db import Base

class Sensor(Base):
    __tablename__ = 'sensor'
    __table_args__ = {'schema': 'public'}

    id = Column(Integer, primary_key=True)
    temperature = Column(Integer, nullable=False)
    humidity = Column(Integer, nullable=False)
    wind_speed = Column(Integer, nullable=False)
    pressure = Column(Integer, nullable=False)
