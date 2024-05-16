# Write a python program to check whether a given nunber is divisible by 5 or not.

def isDivisibleByFive(num) -> bool:
    if (num % 5 == 0):
        return True
    else:
        return False

num = int(input("Give a number: "))
print(isDivisibleByFive(num))

# String - Slicing

str1 = "This is the IT department of the SCS!"
print(str1[3:5])
print(str1[4:6])
print(str1[:7]) # This particular syntax will give you the output 
# from the start to postiton k which is specified
print(str1[7:]) # This particular syntax will give you the output from
# a specified position k to the end 
print(str1[-7: -3])

print(str1.upper())
print(str1.lower())

str1 = "This is the IT department of the SCS!"
print(str1)
str1 = "           This is the IT department of the SCS!               "
print(str1.strip())

str1 = "This is the IT department of the SCS!"
print(str1.replace("I", "C"))
print(str1.replace("SCS", "STS"))

str2 = "This is the IT dept, SCS!"
print(str2.split(","))
print(str2.split(" "))