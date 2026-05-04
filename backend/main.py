from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from database.db import Base, SessionLocal, engine, get_db
from database.models import Lizard
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def seed_data():
    db = SessionLocal()
    try:
        if db.query(Lizard).count() == 0:
            db.add_all([
                Lizard(name="Jaszczurka z Warszawy", votes=0),
                Lizard(name="Smok Wawelski (mini)", votes=0),
                Lizard(name="Krakowski gekon", votes=0),
            ])
            db.commit()
    finally:
        db.close()

seed_data()

@app.get("/api/lizards")
def get_lizards(db: Session = Depends(get_db)):
    return crud.get_lizards(db)

@app.get("/api/lizards/{lizard_id}")
def get_lizard(lizard_id: int, db: Session = Depends(get_db)):
    return crud.get_lizard(db, lizard_id)

@app.delete("/api/lizards/{lizard_id}")
def delete(lizard_id: int, db: Session = Depends(get_db)):
    return crud.delete_lizard(db, lizard_id)

@app.post("/api/lizards/{lizard_id}/reset")
def reset(lizard_id: int, db: Session = Depends(get_db)):
    return crud.reset_votes(db, lizard_id)

@app.post("/api/vote/{lizard_id}")
def vote(lizard_id: int, db: Session = Depends(get_db)):
    return crud.vote_lizard(db, lizard_id)

app.mount("/", StaticFiles(directory="static", html=True), name="static")
