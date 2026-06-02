from dataclasses import dataclass


@dataclass
class Species:
    id: str
    public_id: int | None

    common_name: str
    scientific_name: str

    family: str | None
    genus: str | None

    distribution: str | None
    habitat: str | None

    max_length_cm: str | None
    max_weight_g: str | None

    diet: str | None