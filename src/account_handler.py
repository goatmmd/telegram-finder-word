from pydantic import BaseModel


class Account(BaseModel):
    api_id: int
    api_hash: str
