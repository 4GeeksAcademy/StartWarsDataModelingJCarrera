import os
import sys
from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import create_engine, String, ForeignKey
from eralchemy2 import render_er

Base = declarative_base()

class User (Base):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    password: Mapped[str]=mapped_column(nullable=False)
    email: Mapped[str]=mapped_column(nullable=False)

    favoritos:Mapped[list["Favoritos"]]=relationship(back_populates="user")


class Favoritos (Base):
    __tablename__ = 'favoritos'
    fav_id: Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[int]= mapped_column(ForeignKey("user.id"), nullable=False)
    personaje_id:Mapped[int]= mapped_column(ForeignKey("personaje.id"), nullable=False)
    planetas_id:Mapped[int]= mapped_column(ForeignKey("planetas.id"), nullable=False)
    Vehiculos_id:Mapped[int]= mapped_column(ForeignKey("vehiculos.id"), nullable=False)

    user:Mapped["User"]=relationship(back_populates="favoritos")

class Personajes (Base):
    __tablename__ = 'personaje'
    personajes_id: Mapped[int] = mapped_column(primary_key=True)

    favoritos:Mapped[list["Favoritos"]]=relationship(back_populates="personajes")

class Planetas (Base):
    __tablename__ = 'planetas'
    planetas_id: Mapped[int] = mapped_column(primary_key=True)

    favoritos:Mapped[list["Favoritos"]]=relationship(back_populates="planetas")

class Vehiculos (Base):
    __tablename__ = 'vehiculos'
    vehiculos_id: Mapped[int] = mapped_column(primary_key=True)

    favoritos:Mapped[list["Favoritos"]]=relationship(back_populates="vehiculos")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
