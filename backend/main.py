from fastapi import FastAPI
from mockusers import MockUsers

#url local: http:127.0.0.1:8000
"""
URL local: http:127.0.0.1:800
levantar el servidor: python -m uvicorn main:app --reload (Ctr + c para cerrarlo)

CRUD (Create, Read, Update , Delete)
POST: inserción de datos
GET:lectura de datos
PUT:actualización de datos
DEELTE: borrado de datos
"""
app=FastAPI()
#Mock sample list users
user_list=MockUsers().get_user_list()


@app.get("/users")
async def users():
    return user_list  


@app.get("/user/{id}")
async def user(id:int):
    user=filter(lambda user:user.id==id,user_list )
    return user




