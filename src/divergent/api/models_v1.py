from pydantic import BaseModel

class RootRequest(BaseModel):
    pass

class RootResponse(BaseModel):
    server: str
    version: str
