from dataclasses import dataclass
from backend.domain.entities.species import Species


@dataclass
class Lizard:
    id: str
    public_id: int | None
    name: str
    age: int
    species: Species | None

    def __repr__(self) -> str:
        return f"Lizard(id={self.id}, public_id={self.public_id}, name={self.name}, age={self.age}, species={self.species})"        