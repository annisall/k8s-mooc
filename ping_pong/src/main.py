import logger
from fastapi import FastAPI

app = FastAPI()
LOG = logger.get_logger(__name__)

ping = 0

@app.get("/pingpong")
async def root():
    global ping
    resp_body = f"Ping / pongs: {ping}"
    ping = ping+1
    return resp_body