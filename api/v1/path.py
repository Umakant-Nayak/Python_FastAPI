from fastapi import APIRouter,HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session as S
from db import Session
from models.user import User

class Item(BaseModel):
    id: int
    name: str

def get_db():
    try:
        db= Session()
        print("in db", db)
        return db
    except Exception as e:
        print("error", e)
    
folder_router = APIRouter()
# class Item(BaseModel):
#     item_id: int 

@folder_router.post("/items/")
async def create_item(item: Item):
    db:S= get_db()
    db_user = User(id=item.id, name=item.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    response_data = {
        "data": db_user
    }
    return response_data

@folder_router.get('/items/{item_id}')
def get_items_by(item_id: int):
    db:S= get_db()
    name=db.query(User.name).filter(User.id== item_id).first()
    print(name)
    return {"name": name[0] }

@folder_router.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: int, item: Item):
    db: S = get_db()
    db_user = db.query(User).filter(User.id == item_id).first()
    db_user.name = item.name
    db.commit()
    db.refresh(db_user)
    return db_user  
 
@folder_router.delete('/items/{item_id}')    
async def delete_item(item_id: int):
    db: S = get_db()
    user = db.query(User).filter(User.id == item_id).first()
    db.delete(user)
    db.commit()
    return {"data":"message : User "+ user.name +" deleted successfully"}

    