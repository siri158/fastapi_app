from sqlite3 import Column,integer,String,Enum,relationship,ForeignKey

from sqlalchemy import Integer
from models.company import company
from sqlalchemy.orm import declarative_base
from database import engine, Base,sessionLocal

Base = declarative_base()


class JobBase(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String,  index=True, nullable=False)
    description = Column(String)
    salary = Column(Integer)
    company_id = Column(Integer,ForeignKey('companies.id'))

    company = relationship("CompanyBase", back_populates="jobs")

