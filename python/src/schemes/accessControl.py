from pydantic import BaseModel

class refresh_token(BaseModel):
    refresh_token: str