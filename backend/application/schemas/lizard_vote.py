from pydantic import BaseModel


class LizardVoteCreateRequest(BaseModel):
    title: str
    lizard_ids: list[str]