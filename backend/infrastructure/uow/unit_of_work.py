from backend.infrastructure.core import SessionLocal
from infrastructure.repositories.lizard_repositories import LizardRepository



class UnitOfWork:

    def __init__(self):
        self.db = SessionLocal()

        self.lizards = LizardRepository(self.db)

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def close(self):
        self.db.close()