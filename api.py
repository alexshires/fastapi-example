import logging
from fastapi import FastAPI

app = FastAPI()

logging.basicConfig()
# https://medium.com/@PhilippeGirard5/fastapi-logging-f6237b84ea64

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)



@app.get("/")
async def read_root():
    logger.warning("hello world called")
    return {"Hello": "World"}


@app.get("/health")
async def health_root():
    return {"status": "200 OK"}