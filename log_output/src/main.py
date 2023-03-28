import random
import string
from datetime import datetime, timezone
import logger
from fastapi import FastAPI
import requests

app = FastAPI()
LOG = logger.get_logger(__name__)


@app.get("/")
async def root():
    time_now = datetime.now(timezone.utc)
    resp = requests.get('http://ping-pong-scv:3456/pingpong')
    response_text = (f"""{time_now}: {random_str}
    {resp.text}""")
    return response_text

def generate_random_str():
    rand_list = random.choices(string.ascii_letters + string.digits + string.punctuation, k = 24)
    rand_str = ''.join(rand_list)
    return rand_str

random_str = generate_random_str()