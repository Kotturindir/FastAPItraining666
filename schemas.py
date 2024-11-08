from pydantic import BaseModel

from typing import Optional, Annotated


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None
    

class STaskRead(STaskAdd):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int
    