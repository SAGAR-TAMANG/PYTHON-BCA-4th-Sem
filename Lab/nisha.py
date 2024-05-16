# Fibonacci Series

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def print_fibonacci_series(count):
    if count <= 0:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci Series:")
        for i in range(count):
            print(fibonacci(i), end=" ")

count = int(input("Enter the number of terms in Fibonacci series: "))
print_fibonacci_series(count)
