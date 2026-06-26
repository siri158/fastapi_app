from pydantic import BaseModel
from typing import Optional

class jobcreate(BaseModel):
    title: str
    salary: int

class jobupdate(BaseModel):
    title: Optional[str]=None
    salary:Optional[int]=None
