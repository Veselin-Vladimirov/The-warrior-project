import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_uri = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql://postgres:1234@localhost:5432/sensor_db')

engine = create_engine(database_uri)

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
