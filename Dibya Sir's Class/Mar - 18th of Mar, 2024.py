# Inputs

num = input("Enter Number")
print(num)
name1 = input("Enter Name")
print(name1)

print('Type of number', type(num))
print('Type of name', type(name1))

# Iterator

# Is an object that enables traversing through a collection of data one element at a time.

# Generators

# are functions that return an interator
# Values lazily, one at a time, intead of computing & storing values all at once.
# Maintains their state between function calls, allowing them to resume execution where they left off.
# Generators are defined using a regular function defition with the yield keyword instead of return.
# The body of the function is executed only when the generator's __next__() method is called, 
# typcially using the next() function or within a loop

# yield keyword 

# The yield keyword is used inside a generator funciton to return a value to the caller 
# while preserving the state of the function.
# When yield is encountered, the function's execution is paused, and the value 
# specified by yield is returned to the caller.

def countdown(n):
    while n > 0:
        yield n
        n -= 1

gen = countdown(5)
print(next(gen))
print(next(gen))
print(previous(gen))


# lambda function & inline function

my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(next(my_iterator))

def my_gen():
    yield 1
    yield 2
    yield 3

gen = my_gen()
print(gen)

square = [x ** 2 for x in range(1, 4)]
print(square)

square = {x ** 2 for x in range(1,4)}
print(square)

square = {x:x ** 2 for x in range(1,4)}
print(square)

add = lambda x, y: x+ y
print(add(2,3))








