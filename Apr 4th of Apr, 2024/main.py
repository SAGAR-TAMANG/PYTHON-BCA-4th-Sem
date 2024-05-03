def divide_numbers(num1, num2):
  try:
    result = num1 / num2
    print("Result of division:", result)
  except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# Example usage
num1 = 10
num2 = 0
divide_numbers(num1, num2)