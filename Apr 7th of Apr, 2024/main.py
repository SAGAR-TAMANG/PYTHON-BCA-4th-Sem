# List
my_list = [1, 2, 3, 4, 5]

# Tuple
my_tuple = (1, 2, 3, 4, 5)

# Modifying list and tuple
try:
    my_list[0] = 10
    
    my_tuple[0] = 10
    
except Exception as e:
    print("Error:", e)

# Print both list and tuple to see the difference
print("List:", my_list)
print("Tuple:", my_tuple)
