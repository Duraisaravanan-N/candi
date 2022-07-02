from sqlalchemy import  Column, DateTime,  Integer, String
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fname= Column(String)
    lname = Column(String)
    date = Column(DateTime)
    skill=Column(String)
    available=Column(String)





