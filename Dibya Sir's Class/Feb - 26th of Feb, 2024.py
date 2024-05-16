City = ('Guwahati', 'Jorhat', 'Dibrugarh')

for i in City:
    print(i)

print("\n List begins \n \n")
    
CityList = ['Guwahati', 'Jorhat', 'Dibrugarh']

for i in CityList:
    print(i)
    
print("\n Custom Function Beings \n")

def Upa(x, y):
    return x + y

print(Upa(2, 2))

print("\n Subtraction Begins \n")

def YugFal(x, y) -> int:
    return x-y;

print(YugFal(2, 2))

print("\n Default Parameter Value Begins \n")

def jugfol(x, y=0) -> int:
    return x+y

print(jugfol(1, 2))
print(jugfol(1))

print("\n Conditional Statements Begins \n")

def div1(x):
    if x%5 == 0:
        return True;
    else:
        return False;

if div1(10):
    print("Divisible by 5")
else:
    print("Not Divisible by 5")










































