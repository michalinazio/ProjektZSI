from backend.domain.entities.lizard import Lizard


class LizardService:

    def __init__(self, lizard_repository):
        self.lizard_repository = lizard_repository

    def get_lizards(self) -> list[Lizard]:
        return self.lizard_repository.get_all_lizards()

    def get_lizard_by_id(self, lizard_id: str) -> Lizard | None:
        return self.lizard_repository.get_lizard_by_id(lizard_id)

    def create_lizard(self, lizard_data) -> Lizard:
        return self.lizard_repository.create_lizard(lizard_data)

    def update_lizard(self, lizard_id: str, lizard_data) -> Lizard | None:
        return self.lizard_repository.update_lizard(lizard_id, lizard_data)

    def delete_lizard(self, lizard_id: str) -> bool:
        return self.lizard_repository.delete_lizard(lizard_id)