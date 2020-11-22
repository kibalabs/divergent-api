import os

from fastapi import APIRouter


def create_api_health() -> APIRouter:
    router = APIRouter()

    @router.get('/')
    async def root():
        return {'server': os.environ.get('NAME'), 'version': os.environ.get('VERSION')}

    return router
