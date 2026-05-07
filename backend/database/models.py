from sqlalchemy import Column, Integer, String
from .db import Base

class Lizard(Base):
    __tablename__ = "lizards"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    votes = Column(Integer, default=0)
