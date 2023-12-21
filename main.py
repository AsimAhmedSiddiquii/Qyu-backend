from fastapi import FastAPI
from app.user.routes import router as user_router
from app.org.routes import router as org_router

app = FastAPI()

app.include_router(user_router, prefix="/user", tags=["users"])
app.include_router(org_router, prefix="/org", tags=["org"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
