import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


database_uri = os.environ.get('SQLALCHEMY_DATABASE_URI', 'postgresql://warrior:1122334455@postgres-db1.ctyge4wgoiux.eu-central-1.rds.amazonaws.com:5432/postgresdb')

engine = create_engine(database_uri)

Base = declarative_base()
Base.metadata.bind = engine

Session = sessionmaker(bind=engine)
