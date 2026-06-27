from sqlalchemy import ColumnInteger, String,Enum,relationship
from database import engine, Base,sessionLocal


class CompanyBase(Base):
    __tablename__ = 'companies'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,  index=True, nullable=False)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)
    jobs = relationship("JobBase", back_populates="company")
