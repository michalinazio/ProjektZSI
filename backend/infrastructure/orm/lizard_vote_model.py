from sqlalchemy import Column, DateTime, Integer, String, func

from backend.utils.uuid import generate_uuid
from backend.infrastructure.orm.base import Base
from sqlalchemy.orm import relationship

class LizardVoteModel(Base):
    __tablename__ = "lizard_votes"

    id = Column(
        String(36),
        primary_key=True,
        default=generate_uuid,
    )

    public_id = Column(
        Integer,
        unique=True,
        nullable=True,
    )

    title = Column(
        String(100),
        nullable=False,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    candidates = relationship(
        "LizardVoteCandidateModel",
        back_populates="vote",
        cascade="all, delete-orphan",
    )