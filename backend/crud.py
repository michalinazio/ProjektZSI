from sqlalchemy.orm import Session
from database.models import Lizard

def get_lizards(db: Session):
    return db.query(Lizard).all()

def vote_lizard(db: Session, lizard_id: int):
    lizard = db.query(Lizard).filter(Lizard.id == lizard_id).first()

    if not lizard:
        return {"error": "not found"}

    lizard.votes += 1
    db.commit()
    return {"ok": True}
