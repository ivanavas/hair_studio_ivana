from model import *
from model.relations import *
from model.cache import region, api

k = Employee(name="Ivan", address="Ivic", email="ivan@gmail.com", contact_number="12345")
session.add(k)
session.commit()

ID = 1
KEY = f'employee_{ID}'
k = region.get(KEY)
print(k)
if k is api.NO_VALUE:
    k = session.query(Employee).filter(Employee.id==ID).one()
    region.set(KEY, k)
print(k.name + " " + k.email)

