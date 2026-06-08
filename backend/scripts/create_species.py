from backend.infrastructure.core.db import SessionLocal

from backend.infrastructure.repositories.species_repositories import SpeciesRepository
from backend.domain.services.species_service import SpeciesService

from backend.domain.entities.species import Species
from backend.application.schemas.species import SpeciesCreateRequest


def main():
    db = SessionLocal()

    repo = SpeciesRepository(db)
    service = SpeciesService(repo)

    print("Tworzę species...")

    payload = SpeciesCreateRequest(
        common_name="Leopard Gecko",
        scientific_name="Eublepharis macularius",
        family="Eublepharidae",
        genus="Eublepharis",
        distribution="Pakistan",
        habitat="Dry areas",
        max_length_cm="28",
        max_weight_g="90",
        diet="Insects",
    )

    created = service.create_species(payload)

    print("UTWORZONO:")
    print(created)

    db.close()


if __name__ == "__main__":
    main()