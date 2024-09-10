from fastapi import FastAPI
from server.routers import user_router, task_router

app = FastAPI()

app.include_router(user_router.router, prefix="/users", tags=["Users"])
app.include_router(task_router.router, prefix="/tasks", tags=["Tasks"])
