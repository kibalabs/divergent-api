import os
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from databases import Database

from divergent.api.api_v1 import create_api as create_v1_api
from divergent.api.health import create_api as create_health_api

logging.basicConfig(level=logging.INFO)
database = Database(f'mysql://{os.environ["DB_USERNAME"]}:{os.environ["DB_PASSWORD"]}@{os.environ["DB_HOST"]}:{os.environ["DB_PORT"]}/{os.environ["DB_NAME"]}')

app = FastAPI()
app.include_router(router=create_health_api())
app.include_router(prefix='/v1', router=create_v1_api())
app.add_middleware(CORSMiddleware, allow_credentials=True, allow_methods=['*'], allow_headers=['*'], allow_origins=[
    'https://divergent-console.kibalabs.com',
])

@app.on_event('startup')
async def startup():
    await database.connect()

@app.on_event('shutdown')
async def shutdown():
    await database.disconnect()
