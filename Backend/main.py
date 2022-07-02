from datetime import datetime
from subprocess import call
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/create_candidate")
def create_candidate(fname:str, lname:str,dob:datetime,skill:str,availability:str, db:Session = Depends(get_db)):
    cand = crud.create_candidate(db=db, fname=fname,lname=lname,dob=dob,skill=skill,availability=availability)
    return {"candidate": cand}

@app.get("/get_candidate/{id}/") 
def get_candidate(id:int, db:Session = Depends(get_db)):
     cad1 = crud.get_candidate(db=db, id=id)
     return cad1

@app.get("/list_candidate")
def list_friends(db:Session = Depends(get_db)):
    cand_list = crud.list_candidate(db=db)
    return cand_list