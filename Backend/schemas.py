from datetime import datetime
from pydantic import BaseModel


class Userbase(BaseModel):
    id: int
    fname:str
    lname:str
   
    class Config:
        orm_mode = True
        
class UserCreate(Userbase):
    dob:datetime
    skill:str
    available:str
    
    class Config:
        orm_mode = True