from backend.core.db import engine
from backend.orm.base import Base

import backend.orm.species
import backend.orm.lizards

print("Tworzę tabele...")

Base.metadata.create_all(bind=engine)

print("OK")