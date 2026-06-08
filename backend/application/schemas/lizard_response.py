from pydantic import BaseModel

from backend.application.schemas.species_response import SpeciesResponse


class LizardResponse(BaseModel):
    id: str
    name: str
    age: int
    species: SpeciesResponse | None = None