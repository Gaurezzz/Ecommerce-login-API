from sqlalchemy.orm import Session
from services.initDB import init_db
from fastapi import FastAPI
from routers.defaultAuth import router as defAuthRouter
from routers.accessControl import router as accessControlRouter

app = FastAPI()
init_db()
print("Servidor reiniciado")

app.include_router(defAuthRouter, prefix="/auth")
app.include_router(accessControlRouter, prefix="/access")

@app.get("/hi")
def read_root(a1: int, a2: int):
    return {"Hello": "World"}


