# Type()

try:
    # this might raise exception
    
    x = 1/0
    print(x)
except Exception as e:
    print("Exception occured: ", type(e).__name__)
    print("\n Arguemnt:", e.args)
    
# in python, when an exception is raised, you can access
# the exception type using args

def divide_numbers(x, y):
    try:
        result = x/y
        print("result: ", result)
    except ZeroDivisionError as e:
        print("Error: ", type(e).__name__, e.args[0])
    except TypeError as e:
        print("Error", type(e).__name__, e.args[0])
    except Exception as e:
        print("Error", type(e).__name__)
        
divide_numbers(10, "10")
divide_numbers(10, 0)
divide_numbers(10, 10)



def convert_to_int(value):
    try:
        result = int(value)
        print("Conversion successful. Result:")
        
        
# Finish this function and create another one from the screenshots
