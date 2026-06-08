from dataclasses import dataclass


@dataclass
class LizardVote:
    id: str
    title: str

    def __repr__(self) -> str:
        return f"LizardVote(id={self.id}, title={self.title})"