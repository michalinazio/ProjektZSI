from domain.entities.lizard import Lizard
from infrastructure.orm.lizard_model import LizardModel
from infrastructure.mappers.species_mapper import SpeciesMapper


class LizardMapper:

    @staticmethod
    def to_domain(model) -> Lizard:
        return Lizard(
            id=model.id,
            public_id=model.public_id,
            name=model.name,
            age=model.age,
            species=(
                SpeciesMapper.to_domain(model.species)
                if model.species
                else None
            )
        )