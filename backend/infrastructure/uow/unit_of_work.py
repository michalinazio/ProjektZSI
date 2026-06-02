from backend.infrastructure.core import SessionLocal
from backend.infrastructure.repositories.lizard_repositories import LizardRepository
from backend.infrastructure.repositories.species_repositories import SpeciesRepository


class UnitOfWork:

    def __init__(self):
        self.db = SessionLocal()
        self.lizards = LizardRepository(self.db)
        self.species = SpeciesRepository(self.db)

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()

    def close(self):
        self.db.close()