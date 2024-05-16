# Next & Ranges, use of Ranges

print("Result 1")
for i in range(10):
    print(i)
    
print("Result 2")
for i in range(5, 10):
    print(i)
    
print("Result 3")
for i in range(1, 10, 2):
    print(i)
    
nums = list(range(5))
print(nums)

def sum_of_squares(n):
    return sum(i ** 2 for i in range(1, n + 1))

print(sum_of_squares(5))

pattern1 = [x * x * x  for x in range(100)]
print("Pattern1 :", pattern1, '\n \n')

import math 

def pattern2(n):
    return math.sqrt((n * (n+1) / 2))
                
print("Pattern2 :", pattern2(10), '\n \n')

pattern3 = [x * x  for x in range(1, 100, 3)]
print("Pattern3 :", pattern3, '\n \n')



# dictionary is a collection of key value pair
# values are mutable & un-ordered & can be of any type
# keys must be unique
# keys are immutable
    

upa = {'name': 'Upasana', 'age' : 99}

print(upa['name'])
print(upa.get('name'))
print(upa)
upa.pop('name')
print(upa)
upa.update()
print(upa)



















