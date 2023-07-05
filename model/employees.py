from . import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Employee(Base):
    __tablename__="employees"
    id = Column(Integer, primary_key=True)
    name = Column(String(25))
    contact_number= Column(String(25))
    email = Column(String(100))
    address = Column(String(20))
    
