from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.base import Base


class Location(Base):
    __tablename__ = "locations"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Latitude = Column(String(100), nullable=False)
    Longitude = Column(String(100), nullable=False)

    address = relationship("Address", back_populates="location")

    def __repr__(self):
        return f"<Location(id={self.id}, Latitude={self.Latitude}, Longitude={self.Longitude})>"
