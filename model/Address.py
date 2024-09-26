from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.base import Base


class Address(Base):
    __tablename__ = "addresses"
    id = Column(Integer, primary_key=True, autoincrement=True)
    city = Column(String(100), nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)

    location = relationship('Location', back_populates='addresses')
    country = relationship('Country', back_populates='cities')
    missions = relationship('Mission', back_populates='address')

    def __repr__(self):
        return f"<Address(id={self.id}, city={self.city}, location_id={self.location_id}, country_id={self.country_id})>"

