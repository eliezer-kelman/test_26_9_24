from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from config.base import Base


class Country(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)

    cities = relationship("Address", back_populates="country")

    def __repr__(self):
        return f"<Country(id={self.id}, name={self.name})>"