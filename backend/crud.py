from sqlalchemy.orm import Session
from database.models import Lizard

def get_lizards(db: Session):
    return db.query(Lizard).all()

def get_lizard(db: Session, lizard_id: int):
    return db.query(Lizard).filter(Lizard.id == lizard_id).first()

def vote_lizard(db: Session, lizard_id: int):
    lizard = db.query(Lizard).filter(Lizard.id == lizard_id).first()

    if not lizard:
        return {"error": "not found"}

    lizard.votes += 1
    db.commit()
    return {"ok": True}

def create_lizard(db: Session, name: str):
    lizard = Lizard(name=name, votes=0)
    db.add(lizard)
    db.commit()
    db.refresh(lizard)
    return lizard

def delete_lizard(db: Session, lizard_id: int):
    lizard = get_lizard(db, lizard_id)
    if not lizard:
        return None

    db.delete(lizard)
    db.commit()
    return True

def reset_votes(db: Session, lizard_id: int):
    lizard = get_lizard(db, lizard_id)
    if not lizard:
        return None

    lizard.votes = 0
    db.commit()
    return lizard