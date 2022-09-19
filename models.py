from pydantic import BaseModel


class Message(BaseModel):
    text: str
    id: str | None = None
