import os

from core.api.kiba_router import KibaRouter
from divergent.api.models_v1 import RootResponse


def create_api_health() -> KibaRouter:
    router = KibaRouter()

    @router.get('/', response_model=RootResponse)
    async def root() -> RootResponse:  # pylint: disable=unused-variable
        return RootResponse(server=os.environ.get('NAME'), version=os.environ.get('VERSION'))

    return router
