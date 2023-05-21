import sqlalchemy as sql
from sqlalchemy import Integer, String, Boolean, ForeignKey, Column, Table
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = sql.create_engine('')  # локальная БД, мною использовалась PostgreSQL
Session = sessionmaker(bind=engine)


class App_User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    vk_id = Column(Integer)
    birth_year = Column(Integer)
    gender = Column(Integer)
    city_id = Column(Integer)

    results = relationship('Results', secondary='userresult', back_populates='users')


userresult = Table(
    'userresult', Base.metadata,
    Column('user_id', Integer, ForeignKey('User.id')),
    Column('result_id', Integer, ForeignKey('results.id'))
)


class Results(Base):
    __tablename__ = 'results'

    id = Column(Integer, primary_key=True)
    result_vk_id = Column(Integer)
    url = Column(String(30))
    photo_id = Column(Integer)
    favorite = Column(Boolean)
    black_list = Column(Boolean)

    users = relationship(App_User, secondary=userresult, back_populates='results')


if __name__ == '__main__':
    Base.metadata.create_all(engine)