from fastapi import FastAPI
from starlette.responses import HTMLResponse
from starlette.middleware import cors, trustedhost
from api import rdapi

app = FastAPI()

@app.get("/")
async def root():
    return HTMLResponse("<h1>Backend is Running</h1>")

app.include_router(rdapi.router)