from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
import logging
from fastapi.security import Oauth2PasswordBearer, OAuth2PasswordRequestForm

app=FastAPI()
oauth2=Oauth2PasswordBearer(tokenUrl="login")



class User(BaseModel):
    username:str
    name:str
    mail:str
    age:int
    disabled:bool

class UserDB(User):
    password:str


users_db={
"user1": { "username":"usr1","name":"user1","mail":"usr1@mail.com","age":41,"disabled":False,"password":"1234"},    
"user2": { "username":"usr1","name":"user1","mail":"usr1@mail.com","age":41,"disabled":False,"password":"12"} 

}


def search_user(username:str):
   if username in users_db:
         logging.info(f"User {username} found")
         return UserDB(**users_db[username])

@app.post("/login")
async def login(form:OAuth2PasswordRequestForm=Depends()):
    user_db=user_db.get(form.username)
    if not user_db:
        logging.error("User not found")
        raise HTTPException(status_code=400, detail="Incorrect username")
    

    user=search_user(form.username)
    if form.password!=user.password:
        logging.error("Incorrect password")
        raise HTTPException(status_code=400, detail="Incorrect password")
    
    return {"access_token":user.username,"token_type":"bearer"}

@app.get("/users/me",response_model=User)
async def get_current_user(token:str=Depends(oauth2)):
    user=search_user(token)
    if not user:
        logging.error("User not found")
        raise HTTPException(status_code=400, detail="User not found")
    return user