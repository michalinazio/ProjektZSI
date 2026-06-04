from backend.domain.entities.lizard import Lizard
from backend.domain.exceptions.custom_exceptions import NotFoundError

class LizardService:

    def __init__(self, lizard_repository):
        self.lizard_repository = lizard_repository

    def get_lizards(self) -> list[Lizard]:
        found_lizard = self.lizard_repository.get_all_lizards()
        if not found_lizard:
            raise NotFoundError("No lizards found")
        return found_lizard

    def get_lizard_by_id(self, lizard_id: str) -> Lizard | None:
        found_lizard = self.lizard_repository.get_lizard_by_id(lizard_id)
        if not found_lizard:
            raise NotFoundError("Lizard not found")
        return found_lizard

    def create_lizard(self, lizard_data) -> Lizard:
        return self.lizard_repository.create_lizard(lizard_data)

    def update_lizard(self, lizard_id: str, lizard_data) -> Lizard | None:
        found_lizard = self.lizard_repository.update_lizard(lizard_id, lizard_data)
        if not found_lizard:
            raise NotFoundError("Lizard not found")
        return found_lizard

    def delete_lizard(self, lizard_id: str) -> bool:
        found_lizard = self.lizard_repository.get_lizard_by_id(lizard_id)
        if not found_lizard:
            raise NotFoundError("Lizard not found")
        return self.lizard_repository.delete_lizard(lizard_id)
    
    def find_lizard_by_name(self, name: str) -> Lizard | None:
        found_lizard = self.lizard_repository.find_lizard_by_name(name)
        if not found_lizard:
            raise NotFoundError("Lizard not found")
        return found_lizard

    def find_lizards_by_phrase(self, phrase: str) -> list[Lizard]:
        return self.lizard_repository.get_lizards_by_phrase(phrase)