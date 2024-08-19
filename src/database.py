import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
# import all your models here 
from .models import *

file_path = os.path.join(os.path.abspath(os.getcwd()),"db\\storedb.db")

# database
DATABASE_URL = "sqlite:///" + file_path

engine = create_engine(DATABASE_URL, echo=True)
session_db = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind= engine))
Base.query = session_db.query_property()

def init_db():
    # import all your models here    
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")