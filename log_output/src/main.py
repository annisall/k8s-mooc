import random
import string
from datetime import datetime, timezone
import logger
from fastapi import FastAPI

app = FastAPI()
LOG = logger.get_logger(__name__)


@app.get("/")
async def root():
    time_now = datetime.now(timezone.utc)
    return {"message": f"{time_now}: {random_str}"}

def generate_random_str():
    rand_list = random.choices(string.ascii_letters + string.digits + string.punctuation, k = 24)
    rand_str = ''.join(rand_list)
    return rand_str

random_str = generate_random_str()