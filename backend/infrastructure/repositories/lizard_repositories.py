from sqlalchemy.orm import Session

from infrastructure.orm.lizard_model import LizardModel
from infrastructure.mappers.lizard_mapper import LizardMapper

def __init__(self, db_session: Session):
    self.db_session = db_session

def get_lizard_by_id(self, lizard_id: int):
    lizard_found_model = self.db_session.query(LizardModel).filter(LizardModel.id == lizard_id).first()
    if lizard_found_model is None:
        return None
    return LizardMapper.to_domain(lizard_found_model)

def get_all_lizards(self):
    lizard_models = self.db_session.query(LizardModel).all()
    return [LizardMapper.to_domain(model) for model in lizard_models]

def create_liazard(self, lizard_data):
    new_lizard_model = LizardModel(
        name = lizard_data.name,
        age = lizard_data.age,
        species_id = lizard_data.species_id
    )

    self.db_session.add(new_lizard_model)
    self.db_session.commit()
    self.db_session.refresh(new_lizard_model)

    return LizardMapper.to_domain(new_lizard_model)

def delete_lizard(self, lizard_id: int):
    lizard_to_delete = self.db.session.query(LizardModel).filter(LizardModel.id == lizard_id).first()
    if lizard_to_delete is None:
        return False
    self.db_session.delete(lizard_to_delete)
    self.db_session.commit()
    self.db_session.refresh(lizard_to_delete)
    return True



    