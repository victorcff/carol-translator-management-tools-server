from fastapi import FastAPI
from app.database.db import engine, Base
from app.routers.users import users_router
import uvicorn

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8081, reload=True)
    
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users_router)