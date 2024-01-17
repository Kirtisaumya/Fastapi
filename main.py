from fastapi import FastAPI,HTTPException
from uuid import UUID
from typing import List
from models import User,Gender,Role,UserUpdateRequest


app=FastAPI()

db:List[User]=[
    User(
        id=UUID("0473283e-69cc-4b04-806a-f71c98e5bca8"),
         first_name="Saumya",
         last_name="Joshi",
         middle_name=None,
         gender=Gender.male,
         roles=[Role.student]
         ),
          User(
         id=UUID("a69371fa-e155-4714-9290-3acbc23fc174"),
         first_name="Kamala",
         last_name="Joshi",
         middle_name=None,
         gender=Gender.female,
         roles=[Role.user,Role.admin]
         )
         ]


@app.get("/users")
async def fetch_users():
    return db;

@app.post("/users")
async def register_user(user: User):
    db.append(user)
    return{"id":user.id}

@app.delete("/users/{user_id}")
async def delete_user(user_id:UUID):
    for user in db:
        if user.id==user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} does not exists"
    )
@app.put("/users/{user_id}")
async def update_user(user_update:UserUpdateRequest,user_id:UUID):
    for user in db:
        if user.id == user_id:
            if user_update.first_name is not None:
              user.first_name=user_update.first_name
            if user_update.last_name is not None:
              user.last_name=user_update.last_name
            if user_update.middle_name is not None:
              user.middle_name=user_update.middle_name
            if user_update.roles is not None:
              user.roles=user_update.roles
            if user_update.gender is not None:
              user.gender=user_update.gender
             
            return
        
    raise HTTPException(
        status_code=404,
        detail=f"user with id:{user_id} does not exists"
        )
            

        

