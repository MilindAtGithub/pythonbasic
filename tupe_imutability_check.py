# This is to check whether any object passed in tuple will be unmutable or not

class Emp:
    
    def __init__(self, name):
        self._name=name
        
    def changename(self, newName):
        self._name=newName
    
    def getname(self):
        return self._name
    
# Creating the objects first
emp1 = Emp('FirstEmp')
emp2 = Emp('SecondEmp')

mytuple = (emp1,emp2)

emp3 = mytuple[0]
emp3.changename("ThirdEmp")

print(emp1.getname())

## Conclusion is that object with in the tuple are not immutaable you can change its value