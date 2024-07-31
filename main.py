from typing import Optional
from models import Base, User
from pydantic import BaseModel
from schemas import UserSchema
from database import engine,Sessionlocal
from sqlalchemy.orm import session
from fastapi import FastAPI,Depends

Base.metadata.create_all(bind=engine)

app = FastAPI()
def get_db():
    try:
        db = Sessionlocal()
        yield db
    finally:
        db.close()

#
#
# @app.post("/adduser")
# def add_user(request:UserSchema, db: session = Depends(get_db)):
#     user = User(name=request.name, email = request.email,nickname=request.nickname)
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return user
#
# @app.get("/user/{user_name}")
# def get_user(user_name,db:session = Depends(get_db)):
#     users = db.query(User).filter(User.name == user_name).first()
#     return users


from fastapi import FastAPI, Depends

app = FastAPI()

# Assuming User is a dictionary to store user data
User = {}


@app.delete("/delete/")
def delete(user_name: str):
    if user_name not in User:
        return {"Error": "User does not exist"}

    del User[user_name]
    return {"user_name": user_name, "message": "Deleted successfully"}