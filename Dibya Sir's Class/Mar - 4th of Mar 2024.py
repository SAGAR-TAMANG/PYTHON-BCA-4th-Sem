# String Operations

# Write a function using python to find out the square root of an irrational number.

import math

def square_root(num):
    return math.sqrt(num)

print(square_root(9))

# consider a variable str 

str = 'Hi, I am sagar'
print(str[2])

for x in str:
    print(x)
      
# Length of the String
print("Number of characters are:", len(str))

# Pattern searching

str1 = "There is a cafeteria below my departmental block"
print("cafeteria" in str1)
print("Upasana" in str1)

# 

str2 = "The best time in life is student's life"
if "student" in str2: 
    print("yes, i am a student")
else:
    print("no, i am not a student")
if "faculty" in str2:
    print("Faculty is there")
else:
    print("Faculty is not there")
if "upasana" not in str2:
    print("upa is not there")
else:
    print("upa is there")

# Concatination of Strings

str1 = "This is "
str2 = "the python programming class"
str3 = str1 + str2

print(str3)








































