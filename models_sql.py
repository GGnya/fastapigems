from sqlalchemy import MetaData, ForeignKey
from sqlalchemy import Table, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base

from utils.db_utils import get_engine_from_settings

engine = get_engine_from_settings()

connection = engine.connect()

metadata = MetaData()

gem = Table(
    'gem',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('price', Float),
    Column('available', Boolean, default=True),
    Column('gem_type', Integer, ForeignKey('gem_type.type_id'))
)

gem_properties = Table(
    'gem_properties',
    metadata,
    Column('id', Integer, ForeignKey('gem.id')),
    Column('size', Float, default=1),
    Column('clarity', Integer, ForeignKey('gem_clarity.clarity_id')),
    Column('color', Integer, ForeignKey('gem_color.color_id'))
)

gem_color = Table(
    'gem_color',
    metadata,
    Column('color_id', Integer, primary_key=True),
    Column('color', String)
)
gem_clarity = Table(
    'gem_clarity',
    metadata,
    Column('clarity_id', Integer, primary_key=True),
    Column('clarity', String)
)

gem_type = Table(
    'gem_type',
    metadata,
    Column('type_id', Integer, primary_key=True),
    Column('type', String)
)

metadata.create_all(engine)

Base = declarative_base()

class Gem(Base):
    __tablename__ = 'gem'
    id = Column(Integer, primary_key=True)
    price = Column(Float)
    available = Column(Boolean, default=True)
    gem_type = Column(Integer, ForeignKey('gem_type.type_id'))

    def __repr__(self):
        return "<User(price='%s', available='%s', gem_type='%s')>" % (
            self.price,
            self.available,
            self.gem_type,
        )

class GemProperties(Base):
    __tablename__ = 'gem_properties'
