import logger
from fastapi import FastAPI

app = FastAPI()
LOG = logger.get_logger(__name__)

ping = 0

@app.get("/")
async def root():
    global ping
    resp_body = f"Pong {ping}"
    ping = ping+1
    return resp_body