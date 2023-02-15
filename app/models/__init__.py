# -*- coding: utf-8 -*-

# Import standard library packages

# Import installed packages
from sqlalchemy import Column,  String
from app.core.db.base_class import Base


class Test1(Base):
    __tablename__ = 'test1'
    name = Column(String(200), nullable=True)


def __repr__(self):
    return f'{self.id} {self.name}'
