import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# os.environ['SQLALCHEMY_DATABASE_URI']
# 'postgresql://postgres:1234@localhost:5432/sensor_db'
engine = create_engine('postgresql://postgres:1234@localhost:5432/sensor_db')

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
