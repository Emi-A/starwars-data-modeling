import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    username = Column(String(250), nullable=False)
    password = Column(String(250))
   
class Character(Base):
    __tablename__= 'character'
    id= Column(Integer, primary_key=True)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(Integer)
    gender = Column(String(250))
    name = Column(String(250))
  
class Planet(Base):
    __tablename__= 'planet'
    id= Column(Integer, primary_key=True)
    diameter= Column(Integer)
    rotation_period= Column(Integer)
    orbital_period= Column(Integer)
    gravity= Column(Integer)
    population = Column(Integer)
    climate= Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    created = Column(Integer)
    edited = Column(Integer)
    name = Column(String(250))
   
class Favorite(Base):
    __tablename__= 'favorite'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')