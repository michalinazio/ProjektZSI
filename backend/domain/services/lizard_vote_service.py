from uuid import uuid4

from backend.infrastructure.orm.lizard_vote_model import LizardVoteModel
from backend.infrastructure.orm.lizard_vote_candidate_model import LizardVoteCandidateModel


class LizardVoteService:

    def __init__(self, uow):
        self.uow = uow

    def create_vote(self, title: str, lizard_ids: list[str]) -> str:
        if len(lizard_ids) != 4:
            raise ValueError("Exactly 4 lizards required")

        vote_id = str(uuid4())

        vote_model = LizardVoteModel(
            id=vote_id,
            title=title,
        )

        self.uow.lizard_votes.create_vote(vote_model)

        for lizard_id in lizard_ids:
            candidate_model = LizardVoteCandidateModel(
                id=str(uuid4()),
                vote_id=vote_id,
                lizard_id=lizard_id,
                votes_count=0,
            )

            self.uow.lizard_votes.add_candidate(candidate_model)

        self.uow.commit()

        return vote_id

    def vote(self, candidate_id: str) -> None:
        self.uow.lizard_votes.increment_vote(candidate_id)
        self.uow.commit()

    def get_results(self, vote_id: str):
        vote = self.uow.lizard_votes.get_vote(vote_id)
        candidates = self.uow.lizard_votes.get_candidates(vote_id)

        return {
            "vote": vote,
            "candidates": candidates,
        }