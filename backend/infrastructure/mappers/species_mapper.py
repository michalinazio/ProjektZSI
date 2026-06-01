from backend.domain.entities.species import Species


class SpeciesMapper:

    @staticmethod
    def to_domain(model) -> Species:
        return Species(
            id=model.id,
            common_name=model.common_name,
            scientific_name=model.scientific_name,
        )