from backend.infrastructure.core.db import engine
from backend.infrastructure.orm.base import Base

print("Tworzę tabele...")

Base.metadata.create_all(bind=engine)

print("OK")