from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from config.base import Base


class Mission(Base):
    __tablename__ = "missions"
    id = Column(Integer, primary_key=True, autoincrement=True)
    priority = Column(Integer, nullable=False)
    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=False)
    type_id = Column(Integer, ForeignKey('types.id'), nullable=False)
    industry_id = Column(Integer, ForeignKey('industries.id'), nullable=False)

    address = relationship('Address', back_populates='missions')
    type = relationship('Type', back_populates='missions')
    industry = relationship('Industry', back_populates='missions')