from pydantic import BaseModel


class LizardCreateRequest(BaseModel):
    name: str
    age: int
    species_id: str