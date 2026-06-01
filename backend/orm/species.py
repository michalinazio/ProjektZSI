import uuid


from backend.utils.uuid import generate_uuid
from sqlalchemy import DateTime, Integer
from sqlalchemy import UUID, Column, String, Text, func

from backend.orm.base import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Species(Base):
    __tablename__ = "species"

    id = Column(String(36), primary_key=True, default=generate_uuid)

    public_id = Column(Integer, autoincrement=True, unique=True)

    common_name = Column(String(255), nullable=False)
    scientific_name = Column(String(255), nullable=False, unique=True)

    family = Column(String(255))
    genus = Column(String(255))

    distribution = Column(Text)  
    habitat = Column(Text) 

    max_length_cm = Column(String(50))
    max_weight_g = Column(String(50))    

    diet = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )


    lizards = relationship("Lizard", back_populates="species")