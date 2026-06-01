
import uuid

from backend.utils.uuid import generate_uuid
from sqlalchemy import DateTime
from sqlalchemy import Column, ForeignKey, Integer, String, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from backend.orm.base import Base

class Lizard(Base):
    __tablename__ = "lizards"

    id = Column(String(36), primary_key=True, default=generate_uuid)

    public_id = Column(Integer, autoincrement=True, unique=True)


    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    species_id = Column(String(36), ForeignKey("species.id"))

    species = relationship("Species", back_populates="lizards")
