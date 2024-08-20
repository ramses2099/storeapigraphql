# imports here
from typing import Optional
from sqlalchemy import select
from .models import *
from .database import Session


class NotFoundError(Exception):
    pass

# functions here

def get_all_categories() -> List[Category]:
    categories = []
    with Session() as session:
        stmt = select(Category)
        rows = session.execute(statement=stmt).all()
        for row in rows:
            categories.append(row[0].serialize)       
        
    return categories

def get_category_by_id(category_id: int) -> Optional[Category]:
    with Session() as session:
        stmt = select(Category).where(Category.id == category_id)
        category = session.execute(statement=stmt).one_or_none()
        if not category:
            raise NotFoundError(f"Category with id {category_id} not found")
        return category[0].serialize 

