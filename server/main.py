from fastapi import FastAPI
from server.routers import user_router, task_router
from .database import init_db
app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await init_db()

app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(task_router.router, prefix="/tasks", tags=["Tasks"])
