from asn1crypto.core import InstanceOf

x = 47
y = divmod(x, 7)  # Returns tuple with divisor and reminder
print(y)

class marks:
    def __init__(self, nbr):
        self._total = nbr
    def __repr__(self):
        return f"This is Repr call {self._total}"
    def __str__ (self):
         return f"This is Str call {self._total}"

m = marks(4)
print(m)
print(repr(m))
print(chr(128406))  #Char function

#Reversing
a = (1,2,3,4,5)
b = reversed(a)
print (list(b))

#Zip Function
t1 = (1,2,3,6)
t2=(4,5,6,7,8)
t3 = zip(t1,t2)
for x, y in t3: print(f'{x}-{y}') #Note it will ignore the extra element

#Class Functions
t4 = 56
t5= type(t4)
print(t5)
t6 = isinstance(t4,int)
print(t6)
t7 = id(t4)
print(t7)