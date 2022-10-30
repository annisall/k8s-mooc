from typing import Union

from fastapi import FastAPI
import uvicorn
import os
import logger

app = FastAPI()
LOG = logger.get_logger(__name__)

if __name__ == '__main__':
    port_number = os.environ.get('PORT', 5000)
    LOG.info(f'Server started in port {port_number}')
    uvicorn.run('main:app', port=port_number)