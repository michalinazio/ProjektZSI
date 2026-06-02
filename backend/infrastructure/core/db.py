from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from backend.infrastructure.orm.lizard_model import LizardModel
from backend.infrastructure.orm.species_model import SpeciesModel

DATABASE_URL = "mysql+mysqlconnector://root:1234@localhost/lizards"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
