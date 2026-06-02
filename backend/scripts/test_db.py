from backend.infrastructure.core.db import engine
from backend.infrastructure.orm.base import Base


print("Zarejestrowane tabele:")
print(Base.metadata.tables.keys())

print("Tworzę tabele...")
Base.metadata.create_all(bind=engine)
print("OK")