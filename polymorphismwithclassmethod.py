class India(): 
    def capital(self): 
        print("New Delhi is the capital of India.") 

    def language(self): 
        print("Hindi the primary language of India.") 

    def type(self): 
        print("India is a developing country.") 

class USA(): 
    def capital(self): 
        print("Washington, D.C. is the capital of USA.") 

    def language(self): 
        print("English is the primary language of USA.") 

    def type(self): 
        print("USA is a developed country.") 

obj_ind = India() 
obj_usa = USA() 
for country in (obj_ind, obj_usa): 
    country.capital() 
    country.language() 
    country.type() 


def function1(obj):
    print("Call within the Function ..............")
    obj.capital() 
    obj.language() 
    obj.type() 
    
function1(obj_ind)  
function1(obj_usa)  