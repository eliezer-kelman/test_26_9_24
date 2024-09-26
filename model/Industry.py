from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.base import Base


class Industry(Base):
    __tablename__ = "industries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Industry = Column(String(100), nullable=False)

    missions = relationship("Mission", back_populates="industry")

    def __repr__(self):
        return f"<Industry(id={self.id}, Industry={self.Industry})>"
