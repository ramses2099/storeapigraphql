import pytest
import os
from src.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import Session 

@pytest.fixture()
def connection():
    file_path = os.path.join(os.path.abspath(os.getcwd()),"src\\db\\storedb.db")

    DATABASE_URL = "sqlite:///" + file_path
    print(f"Using database: {DATABASE_URL}")

    engine = create_engine(DATABASE_URL, echo=True)
    
    return engine

def test_add_user(connection):
    user = User(username="test_user",password="test_password",
        email="test_email@test.com",firstname="juan",lastname="perez")
    
    with Session(connection) as session:
        user_count = session.query(User).count()
        if user_count == 0:        
            session.add(user)
            session.commit()            
            assert session.query(User).count() == 1
            
        assert session.query(User).filter(User.username == "test_user").first().username == "test_user"
        
        
def test_add_category(connection):
    category = Category(description="Test Category", user_id=1)
    
    with Session(connection) as session:
        category_count = session.query(Category).count()
        if category_count == 0:        
            session.add(category)
            session.commit()
            assert session.query(Category).count() == 1
            
        assert session.query(Category).filter(Category.description == "Test Category").first().description == "Test Category"
            
