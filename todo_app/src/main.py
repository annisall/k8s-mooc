from fastapi import FastAPI
from . import logger

app = FastAPI()
LOG = logger.get_logger(__name__)

@app.get("/")
async def root():
    return {"message": "Hello World"}