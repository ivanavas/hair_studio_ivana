from . import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Service(Base):
    __tablename__="services"
    id = Column(Integer, primary_key=True)
    service_name = Column(String(25))
    price = Column(String(25))
    description = Column(String(100))
    employee_id = Column(Integer, ForeignKey("employees.id"))

 

    
    
