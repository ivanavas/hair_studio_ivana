from . import Base
from sqlalchemy import *


class Appointment(Base):
    __tablename__="appointments"
    id = Column(Integer, primary_key=True)
    appointments_date = Column(Date)
    appointments_time = Column(Time)
    service_id = Column(Integer, ForeignKey("services.id"))
    customer_id = Column(Integer, ForeignKey("customers.id"))
  