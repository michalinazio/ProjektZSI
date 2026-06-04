from backend.infrastructure.core.db import SessionLocal

from backend.infrastructure.repositories.species_repositories import SpeciesRepository
from backend.domain.services.species_service import SpeciesService
from backend.domain.services.lizard_service import LizardService
from backend.domain.entities.lizard import Lizard
from backend.domain.entities.species import Species
from backend.infrastructure.repositories.lizard_repositories import LizardRepository

from backend.domain.entities.species import Species
from backend.application.schemas.species import SpeciesCreateRequest


def main():
    db = SessionLocal()

    repo = LizardRepository(db)
    service = LizardService(repo)

    lizard = service.find_lizards_by_phrase("est")
    print(lizard)


    db.close()


if __name__ == "__main__":
    main()