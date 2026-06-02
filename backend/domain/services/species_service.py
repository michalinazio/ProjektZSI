from backend.domain.entities.species import Species

class SpeciesService:

    def __init__(self, species_repository):
        self.species_repository = species_repository

    def get_species(self) -> list[Species]:
        return self.species_repository.get_all_species()

    def get_species_by_id(self, species_id: str) -> Species | None:
        return self.species_repository.get_species_by_id(species_id)

    def create_species(self, species_data) -> Species:
        return self.species_repository.create_species(species_data)

    def update_species(self, species_id: str, species_data) -> Species | None:
        return self.species_repository.update_species(species_id, species_data)

    def delete_species(self, species_id: str) -> bool:
        return self.species_repository.delete_species(species_id)