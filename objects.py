# This will give insight about the objects and calss
from boto.gs.lifecycle import AGE


class Employee:
    
    company = None    
    def __init__(self, name, age):
        self._name = name
        self._age = AGE
    
    def setcompany(self,company):
        Employee.company = company
        
    def getname(self):
        return self._name
    
    def getage(self):
        return self._age
    
    def __str__(self):
        return f'Emp: {self._name}, {self._age} and works in {Employee.company} '
    
    
e1 = Employee("Milind",21)
print(e1)
e1.setcompany('Chalu')
e2 = Employee('Another Emp', 56)
print(e2)



