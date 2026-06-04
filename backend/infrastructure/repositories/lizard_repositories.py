from sqlalchemy.orm import Session

from backend.infrastructure.orm.lizard_model import LizardModel
from backend.infrastructure.mappers.lizard_mapper import LizardMapper


class LizardRepository:

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_lizard_by_id(self, lizard_id: str):
        lizard_model = (
            self.db_session.query(LizardModel)
            .filter(LizardModel.id == lizard_id)
            .first()
        )

        if lizard_model is None:
            return None

        return LizardMapper.to_domain(lizard_model)

    def get_all_lizards(self):
        lizard_models = self.db_session.query(LizardModel).all()

        return [
            LizardMapper.to_domain(lizard_model)
            for lizard_model in lizard_models
        ]

    def create_lizard(self, lizard_data):
        lizard_model = LizardModel(
            name=lizard_data.name,
            age=lizard_data.age,
            species_id=lizard_data.species_id,
        )

        self.db_session.add(lizard_model)
        self.db_session.commit()
        self.db_session.refresh(lizard_model)

        return LizardMapper.to_domain(lizard_model)

    def delete_lizard(self, lizard_id: str):
        lizard_model = (
            self.db_session.query(LizardModel)
            .filter(LizardModel.id == lizard_id)
            .first()
        )

        if lizard_model is None:
            return False

        self.db_session.delete(lizard_model)
        self.db_session.commit()

        return True

    def find_lizard_by_name(self, name: str):
        lizard_model = (
            self.db_session.query(LizardModel)
            .filter(LizardModel.name == name)
            .first()
        )

        if lizard_model is None:
            return None

        return LizardMapper.to_domain(lizard_model)

    def update_lizard(self, lizard_id: str, lizard_data):
        lizard_model = (
            self.db_session.query(LizardModel)
            .filter(LizardModel.id == lizard_id)
            .first()
        )

        if lizard_model is None:
            return None

        lizard_model.name = lizard_data.name
        lizard_model.age = lizard_data.age
        lizard_model.species_id = lizard_data.species_id

        self.db_session.commit()
        self.db_session.refresh(lizard_model)

        return LizardMapper.to_domain(lizard_model)
    
    def get_lizards_by_phrase(self, phrase: str):
        lizard_models = (
            self.db_session.query(LizardModel)
            .filter(LizardModel.name.ilike(f"%{phrase}%"))
            .all()
        )

        return [
            LizardMapper.to_domain(lizard_model)
            for lizard_model in lizard_models
        ]