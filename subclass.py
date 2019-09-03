# Python code to demonstrate how parent constructors 
# are called. 

# parent class 
class Person( object ):     

        # __init__ is known as the constructor         
        def __init__(self, name, idnumber): 
                self._name = name 
                self._idnumber = idnumber 
        def display(self): 
                print(self._name) 
                print(self._idnumber) 
        def multiply(self):
                return  self._idnumber * 100

# child class 
class Employee( Person ):         
        def __init__(self, name, idnumber, salary, post): 
                self._salary = salary 
                self._post = post 

                # invoking the __init__ of the parent class 
                Person.__init__(self, name, idnumber) 
                

                
# creation of an object variable or an instance 
a = Person('Rahul', 886012)     

# calling a function of the class Person using its instance 
a.display() 
print(a.multiply())
e = Employee('M','O007',100, 'Dev')
e.display()
print(e.multiply())