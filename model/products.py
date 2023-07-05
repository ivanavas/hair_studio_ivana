from . import Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Product(Base):
    __tablename__="products"
    id = Column(Integer, primary_key=True)
    product_name = Column(String(25))
    brand= Column(String(25))
    price = Column(DECIMAL)
    quantity = Column(String(20))
    expiry_date = Column(Date)
    service_id = Column(Integer, ForeignKey("services.id"))
    appointment_id = Column(Integer, ForeignKey("appointments.id"))
    
    

