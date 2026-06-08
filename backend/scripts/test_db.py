from backend.infrastructure.core.db import engine
from backend.infrastructure.orm.base import Base
from backend.infrastructure.orm.lizard_vote_model import LizardVoteModel
from backend.infrastructure.orm.lizard_vote_candidate_model import LizardVoteCandidateModel
from backend.infrastructure.orm.lizard_model import LizardModel
from backend.infrastructure.orm.species_model import SpeciesModel

print("Zarejestrowane tabele:")
print(Base.metadata.tables.keys())

print("Tworzę tabele...")
Base.metadata.create_all(bind=engine)
print("OK")