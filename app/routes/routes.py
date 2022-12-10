from fastapi import APIRouter
from config.db import conn
from schemas.users import  UserEntity, UsersEntity
from models.user import User


User = APIRouter()


@User.get("/users")
def find_all_users():
    return UsersEntity(conn.local.user.find())

@User.post("/users")
def create_user(user: User):
    new_user = dict(user)

    id = conn.local.user.insert_one(new_user).inserted_id
    return str(id)
    

@User.get("/user/{id}")
def find_user():
    return("Hello Wolrd")

@User.put("/users/{id}")
def update_user():
    return("Hello Wolrd")

@User.delete("/users/{id}")
def delete_users():
    return("Hello Wolrd")