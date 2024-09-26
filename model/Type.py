from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.base import Base


class Type(Base):
    __tablename__ = "types"
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(100), nullable=False)

    missions = relationship("Mission", back_populates="type")

    def __repr__(self):
        return f"<Type(id={self.id}, name={self.name})>"
