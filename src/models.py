import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

association_table = Table('personajes_favorito', Base.metadata,
                          Column('usuario_id', ForeignKey('usuario.id')),
                          Column('personaje_id', ForeignKey('personaje.id'))
                          )


class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    apellido = Column(String(100))
    email = Column(String(150))
    password = Column(String(150))
    fecha_subscripcion = Column(String(100))
    children = relationship('Personaje',
                            secondary=association_table)
    children = relationship('Planeta',
                            secondary=association_table)


class Personaje(Base):
    __tablename__ = 'personaje'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    height = Column(String(100))
    mass = Column(String(100))
    hair_color = Column(String(100))
    skin_color = Column(String(100))
    eye_color = Column(String(100))
    birth_year = Column(String(100))
    gender = Column(String(100))
    homeworld = Column(String(150))
    created = Column(String(100))


association_table = Table('planeta_favorito', Base.metadata,
                          Column('usuario_id', ForeignKey('usuario.id')),
                          Column('planeta_id', ForeignKey('planeta.id'))
                          )


class Planeta(Base):
    __tablename__ = 'planeta'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    orbital_period = Column(String(100))
    rotation_period = Column(String(100))
    diameter = Column(String(100))
    climate = Column(String(100))
    gravity = Column(String(100))
    terrain = Column(String(100))
    surface_water = Column(String(100))
    population = Column(String(100))
    created = Column(String(100))

    def to_dict(self):
        return {}
# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
