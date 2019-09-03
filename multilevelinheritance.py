# A Python program to demonstrate inheritance 

# Base or Super class. Note object in bracket. 
# (Generally, object is made ancestor of all classes) 
# In Python 3.x "class Person" is 
# equivalent to "class Person(object)" 
class Base(): 
    
    # Constructor 
    def __init__(self, name): 
        self._name = name 

    # To get name 
    def getName(self): 
        return self._name 


# Inherited or Sub class (Note Person in bracket) 
class Child(Base): 
    
    # Constructor 
    def __init__(self, name, age): 
        Base.__init__(self, name) 
        self._age = age 

    # To get name 
    def getAge(self): 
        return self._age 

# Inherited or Sub class (Note Person in bracket) 
class GrandChild(Child): 
    
    # Constructor 
    def __init__(self, name, age, address): 
        Child.__init__(self, name, age) 
        self._address = address 

    # To get address 
    def getAddress(self): 
        return self._address         

# Driver code 
g = GrandChild("Geek1", 23, "Noida") 
print(g.getName(), g.getAge(), g.getAddress()) 
