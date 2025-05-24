from pydantic import BaseModel

class ServerStatus(BaseModel):
    server_name: str
    status: str

class ServerActionResponse(BaseModel):
    server_name: str
    action: str
    success: bool
    message: str