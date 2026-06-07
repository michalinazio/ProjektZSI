from sqlalchemy.orm import Session

from backend.infrastructure.mappers.species_mapper import SpeciesMapper
from backend.infrastructure.orm.species_model import SpeciesModel

class SpeciesRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_species_by_id(self, species_id: str):

        species_model = self.db_session.query(SpeciesModel).filter(SpeciesModel.id == species_id).first()
        if species_model is None:
            return None
        return SpeciesMapper.to_domain(species_model)

    def get_all_species(self):
        species_models = self.db_session.query(SpeciesModel).all()
        return [SpeciesMapper.to_domain(species_model) for species_model in species_models]

    def create_species(self, species_data):
        species_model = SpeciesModel(
            common_name=species_data.common_name,
            scientific_name=species_data.scientific_name,
            family=species_data.family,
            genus=species_data.genus,
            distribution=species_data.distribution,
            habitat=species_data.habitat,
            max_length_cm=species_data.max_length_cm,
            max_weight_g=species_data.max_weight_g,
            diet=species_data.diet,
            )

        self.db_session.add(species_model)
        self.db_session.flush()

        return SpeciesMapper.to_domain(species_model)

    def delete_species(self, species_id: str):
        species_model = self.db_session.query(SpeciesModel).filter(SpeciesModel.id == species_id).first()
        if species_model is None:
            return False

        self.db_session.delete(species_model)

        return True



   