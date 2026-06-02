from dataclasses import dataclass
from backend.domain.entities.species import Species


@dataclass
class Lizard:
    id: str
    public_id: int | None
    name: str
    age: int
    species: Species | None