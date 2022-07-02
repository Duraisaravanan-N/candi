from sqlalchemy.orm import Session
from .models import User

def create_candidate(db:Session,fname,lname,dob,skill,availability):
    new_cand=User(fname=fname,lname=lname,dob=dob,skill=skill,availability=availability)
    db.add(User)
    db.commit()
    db.refresh(new_cand)
    return new_cand

def get_candidate(db:Session, id:int):
    db_cand = db.query(User).filter(User.id==id).first()
    return db_cand

def list_candidate(db:Session):
    all_cand = db.query(User).all()
    return all_cand