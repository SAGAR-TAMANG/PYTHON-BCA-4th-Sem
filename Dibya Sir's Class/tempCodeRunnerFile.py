
class Upa:
    def __init__(self, age, school):
        self.agee = age
        self.school = school
    
    def define(self):
        return f"Upasana is {self.agee} years old and goes to {self.school}"
    
    def print(self):
        print(f"Yo I am printing the age of Upa: {self.agee}")
        
obj1 = Upa(19, "MIT")
print(obj1.agee)
print(obj1.school)
print(obj1.define())

obj1.agee = 0
print(obj1.define())
obj1.print()

# Built in Class Attributes

print("This is the __doc__ \n", Upa.__doc__)
print("\n This is the __name__ \n", Upa.__name__)
print("\n This is the __module__ \n", Upa.__module__)
print("\n This is the __dict__ \n", Upa.__dict__)
print("\n This is the __bases__ \n", Upa.__bases__)