# Simple Inheritance 

class Person:
    
    def __init__(self, name):
        self._name = name
    
    def getname(self):
        return self._name
    
    def ismale(self):
        return False
    
    
class Emp(Person):
    
    def __init__(self, name):
        Person.__init__(self, name)
        
    def ismale(self):
        return True

p = Person('First')
print (p.getname())
print(p.ismale())
e = Emp('Emp Second')
print (e.getname())
print(e.ismale())
