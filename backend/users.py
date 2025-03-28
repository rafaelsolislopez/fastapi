from pydantic import BaseModel
from fastapi import APIRouter,HTTPException
import logging
from mockusers import MockUsers

class User(BaseModel):
    id:int
    name:str
    mail:str
    age:int



#URL local: http:127.0.0.1:800
#levantar el servidor: python -m uvicorn main:app --reload (Ctr + c para cerrarlo)

"""
CRUD (Create, Read, Update , Delete)
POST: inserción de datos
GET:lectura de datos
PUT:actualización de datos
DEELTE: borrado de datos
"""
router=APIRouter()
#Mock sample list users
user_list=MockUsers().get_user_list()
#for user in user_list:
#    print(user)


def searh_user(id:int):
    try:
        logging.info("searching user")
        user=list(filter(lambda user:user.id==id,user_list))
        if len(user)>0:
            return list(user)[0]
        else:
            return {"detail":"user not found"}  
    except Exception as e:
        logging.error(f"error searching user:{e}" )   
        return {"detail":"error searching user"}


@router.get("/users",request_model=User,status_code=201 )
async def users():
    return user_list  


@router.get("/user",response_model=User,status_code=201 )
async def user(id:int):
    try:
         logging.info("getting user")
         user=searh_user(id)
         return user
    except Exception as e:
        logging.info(f"error getting user:{e}")
        raise HTTPException(status_code=404, detail="user not found")   
   
  

@router.post("/adduser")
async def add_user(user:User):
    pass


@router.put("/updateduser")
async def update_user(id:int):
    pass

@router.delete("/deleteduser")
async def delete_user():
    pass

print(searh_user(id=1))