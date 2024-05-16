# Destroying Objects

class MyClass:
    def __init__(self, name):
        self.name = name
        
    def __del__(self):
        print(f"I am  going to destroy this object: {self.name}")
    
upa = MyClass("Upasana")

upa.__del__() # use this method

upa = MyClass("Upasana")

del upa # you can either use del keyword

# Try Except Else Finally 
# Else runs only if try block is successful
# Finally runs after try except is done - usually used for cleanup tasks

try:
    var = input("Give a char input: ")
    
    if var == "Upa":
        raise Exception("YOU GAVE UPA AS INPUT (NOT ALLOWED)")
    
    print("Try block run successfully\n")
    
except Exception as e:
    print("\n-----------------------------\nEXCEPTION OCCURED \n", e, "\n-----------------------------")
    
finally:
    print("This is running after try except block")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    