from fastapi import APIRouter
from fastapi import Request

from core.api.kiba_router import KibaRouter


def create_api_v1() -> KibaRouter():
    router = KibaRouter()

    return router
