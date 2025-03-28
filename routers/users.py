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
users_list=MockUsers().get_user_list()
#for user in user_list:
#    print(user)


def search_user(id:int):
    try:
        logging.info("searching user")
        user=list(filter(lambda user:user.id==id,users_list))
        if len(user)>0:
            return list(user)[0]
        else:
            return {"detail":"user not found"}  
    except Exception as e:
        logging.error(f"error searching user:{e}" )   
        return {"detail":"error searching user"}


@router.get("/users",status_code=201 )
async def users():
    logging.info("getting users")
    return users_list
    logging.error("error getting users")
    raise HTTPException(status_code=404, detail="user not found")


@router.get("/user",response_model=User,status_code=201 )
async def user(id:int):
    try:
         logging.info("getting user")
         user=search_user(id)
         return user
    except Exception as e:
        logging.info(f"error getting user:{e}")
        raise HTTPException(status_code=404, detail="user not found")   
   
  

@router.post("/adduser",response_model=User,status_code=201 )
async def add_user(user:User):
    if type (search_user(id=user.id))!= User:
        logging.info("adding user")
        users_list.append(user)
        return user
    else:
        raise   HTTPException(status_code=404, detail="user already exists")




@router.put("/updateuser")
async def update_user(user:User):
    found=False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            logging.info("updating user")
            return user
    if not found:
        logging.error("error updating user")
        raise HTTPException(status_code=404, detail="user not found")



@router.delete("/deleteuser")
async def delete_user(user:User):
    found=False
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            del users_list[index]
            found = True
            logging.info("deleting user")
            return {"user":user,"status":"deleted"}
    if not found:
        logging.error("error deleting user")
        raise HTTPException(status_code=404, detail="user not found")