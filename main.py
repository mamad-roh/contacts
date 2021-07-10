from fastapi import FastAPI
from database import database
from routers import (
    user,
    authentication
)

app= FastAPI();

database.Base.metadata.create_all(bind= database.engine)

app.include_router(user.router)
app.include_router(authentication.router)