from fastapi import FastAPI

#url local: http:127.0.0.1:8000
app=FastAPI()

@app.get("/")
async def root():
    return "Hello World"  
#python -m uviccorn api/main:app --reload
