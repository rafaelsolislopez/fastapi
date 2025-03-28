from pydantic import BaseModel
from fastapi import APIRouter,HTTPException
import logging


class User(BaseModel):
    id:int
    name:str
    mail:str
    age:int


class MockUsers():
    def __init__(self):
        self.user1=User(id=1,name="Rafa",mail="rafa@mail.com",age=41)
        self.user2=User(id=2,name="Leo",mail="leo@mail.com",age=9)
        self.user3=User(id=3,name="jorge",mail="gorge@mail.com",age=6)

    def get_user_list(self)->list:
        user_list=[self.user1,self.user2,self.user3]
        return user_list
    
    def new_user(self,id:int)->User:
        self.user=User(id=id,name=f"Name{id}",mail="name{id}@mail.com",age=id*5)
        return self.user




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


@router.get("/users",response_model=User,status_code=201 )
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