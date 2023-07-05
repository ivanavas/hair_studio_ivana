from sqlalchemy.orm import relationship

from .appointments import Appointment
from .customers import Customer
from .employees import Employee
from .products import Product
from .services import Service
from . import Base
from . import engine

Customer.appointments = relationship("Appointment", back_populates="customer")
Appointment.service = relationship("Service", back_populates="appointments")
Appointment.products = relationship("Product", back_populates="appointments")
Appointment.customer = relationship("Customer", back_populates="appointments")
Employee.services = relationship("Service", back_populates="employee")
#Service.products = relationship("Product", back_populates="services")
Service.appointments = relationship("Appointment", back_populates="service")
Service.employee = relationship("Employee", back_populates="services")
#Product.services = relationship("Service", back_populates="products")
Product.appointments = relationship("Appointment", back_populates="products")

Base.metadata.bind = engine
Base.metadata.create_all(engine)
