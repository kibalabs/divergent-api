from fastapi import APIRouter
from fastapi import Request

from divergent.api.models_v1 import *


def create_api_v1() -> APIRouter():
    router = APIRouter()

    @router.get('/', response_model=RootResponse)
    async def root(rawRequest: Request) -> RootResponse:  # request: RootRequest
        return RootResponse(message='Welcome to the Divergent API')

    return router
