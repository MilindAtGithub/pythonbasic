# Python example to show working of multiple 
# inheritance 
class Base1(object): 
    def __init__(self): 
        self._str1 = "Geek1"
        print("Base1")

class Base2(object): 
    def __init__(self): 
        self._str2 = "Geek2"     
        self._str1='Base2 Str'   
        print ("Base2")

class Derived(Base2, Base1): 
    def __init__(self): 
        
        # Calling constructors of Base1 
        # and Base2 classes 
        Base1.__init__(self) 
        Base2.__init__(self) 
        print("Derived")
        
    def printStrs(self): 
        print(self._str1, self._str2) 
        

ob = Derived() 
ob.printStrs() 
