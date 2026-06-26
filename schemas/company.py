from pydantic import BaseModel
from typing import Optional

class companycreate(BaseModel):
    name: str
    location: str

class companyupdate(BaseModel):
    name: Optional[str]=None
    location: Optional[str]=None


