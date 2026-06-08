from backend.domain.entities.lizard_vote import LizardVote
from backend.infrastructure.orm.lizard_vote_model import LizardVoteModel


class LizardVoteMapper:

    @staticmethod
    def to_entity(
        model: LizardVoteModel,
    ) -> LizardVote:
        return LizardVote(
            id=model.id,
            title=model.title,
        )

    @staticmethod
    def to_model(
        entity: LizardVote,
    ) -> LizardVoteModel:
        return LizardVoteModel(
            id=entity.id,
            title=entity.title,
        )