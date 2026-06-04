from backend.domain.entities.species import Species
from backend.domain.exceptions.custom_exceptions import NotFoundError

class SpeciesService:

    def __init__(self, species_repository):
        self.species_repository = species_repository

    def get_species(self) -> list[Species]:
        found_species = self.species_repository.get_all_species()
        if not found_species:
            raise NotFoundError("No species found")
        return found_species

    def get_species_by_id(self, species_id: str) -> Species | None:
        found_species = self.species_repository.get_species_by_id(species_id)
        if not found_species:
            raise NotFoundError("Species not found")
        return found_species

    def create_species(self, species_data) -> Species:
        return self.species_repository.create_species(species_data)

    def update_species(self, species_id: str, species_data) -> Species | None:
        found_species = self.species_repository.update_species(species_id, species_data)
        if not found_species:
            raise NotFoundError("Species not found")
        return found_species

    def delete_species(self, species_id: str) -> bool:
        found_species = self.species_repository.get_species_by_id(species_id)
        if not found_species:
            raise NotFoundError("Species not found")
        return self.species_repository.delete_species(species_id)