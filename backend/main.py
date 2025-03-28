from fastapi import FastAPI
import users


app = FastAPI()

# Assuming MockUsers has a `router` attribute
app.include_router(users.router)