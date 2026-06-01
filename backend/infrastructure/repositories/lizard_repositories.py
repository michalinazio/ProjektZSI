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
    