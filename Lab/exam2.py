def check_even(Num):
  if Num % 2 == 0:
    return True
  else:
    return False

# Calling the Function
  
checker = int(input("Number:"))

if (check_even(checker)):
  print("Even")
else:
  print("Odd")
  
# recursion Function
  
def recur_function(Num):
  if Num == 0:
    return Num
  else:
    return recur_function(Num - 1) + Num
  
num =int(input("Give a num:"))
print(recur_function(num))