import os
import sys
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)

    favoritos = relationship("Favoritos", back_populates="user")


class Favoritos(Base):
    __tablename__ = 'favoritos'
    fav_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    personaje_id = Column(Integer, ForeignKey("personaje.id"), nullable=False)
    planeta_id = Column(Integer, ForeignKey("planeta.id"), nullable=False)
    vehiculo_id = Column(Integer, ForeignKey("vehiculo.id"), nullable=False)

    user = relationship("User", back_populates="favoritos")
    personaje = relationship("Personajes", back_populates="favoritos")
    planeta = relationship("Planetas", back_populates="favoritos")
    vehiculo = relationship("Vehiculos", back_populates="favoritos")


class Personajes(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)

    favoritos = relationship("Favoritos", back_populates="personaje")


class Planetas(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)

    favoritos = relationship("Favoritos", back_populates="planeta")


class Vehiculos(Base):
    __tablename__ = 'vehiculo'
    id = Column(Integer, primary_key=True)

    favoritos = relationship("Favoritos", back_populates="vehiculo")

    def to_dict(self):
        return {}
    
# Draw from SQLAlchemy base   
render_er(Base, 'diagram.png')
