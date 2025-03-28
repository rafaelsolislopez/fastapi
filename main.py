from fastapi import FastAPI
import users


app = FastAPI()

#URL local: http:127.0.0.1:800
#levantar el servidor: python -m uvicorn main:app --reload (Ctr + c para cerrarlo)


app.include_router(users.router)