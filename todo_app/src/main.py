from typing import Union

from fastapi import FastAPI
import uvicorn
import os
from . import logger

app = FastAPI()
LOG = logger.get_logger(__name__)

@app.get("/")
async def root():
    return {"message": "Hello World"}