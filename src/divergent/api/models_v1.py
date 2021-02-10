from pydantic import BaseModel

class RootRequest(BaseModel):
    pass

class RootResponse(BaseModel):
    message: str
