from .db import Base
from sqlalchemy import Column, Integer, Numeric

class Sensor(Base):
    __tablename__ = 'sensor'
    id = Column(Integer, primary_key=True)
    temperature = Column(Numeric(5, 2))
    humidity = Column(Numeric(5, 2))
    wind_speed = Column(Numeric(5, 2))
    pressure = Column(Numeric(5, 2))
