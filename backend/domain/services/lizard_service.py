from backend.domain.entities.lizard import Lizard
from backend.domain.exceptions.custom_exceptions import NotFoundError


class LizardService:

    def __init__(self, uow):
        self.uow = uow

    def get_lizards(self) -> list[Lizard]:
        found_lizard = self.uow.lizards.get_all_lizards()
        if not found_lizard:
            raise NotFoundError("No lizards found")
        return found_lizard

    def get_lizard_by_id(self, lizard_id: str) -> Lizard:
        found_lizard = self.uow.lizards.get_lizard_by_id(lizard_id)
        if not found_lizard:
            raise NotFoundError("Lizard not found")
        return found_lizard

    def create_lizard(self, lizard_data) -> Lizard:
        result = self.uow.lizards.create_lizard(lizard_data)
        self.uow.commit()
        return result

    def update_lizard(self, lizard_id: str, lizard_data) -> Lizard:
        result = self.uow.lizards.update_lizard(lizard_id, lizard_data)
        if not result:
            raise NotFoundError("Lizard not found")
        self.uow.commit()
        return result

    def delete_lizard(self, lizard_id: str) -> bool:
        found = self.uow.lizards.get_lizard_by_id(lizard_id)
        if not found:
            raise NotFoundError("Lizard not found")

        result = self.uow.lizards.delete_lizard(lizard_id)
        self.uow.commit()
        return result

    def find_lizard_by_name(self, name: str) -> Lizard:
        found = self.uow.lizards.find_lizard_by_name(name)
        if not found:
            raise NotFoundError("Lizard not found")
        return found

    def find_lizards_by_phrase(self, phrase: str) -> list[Lizard]:
        return self.uow.lizards.get_lizards_by_phrase(phrase)