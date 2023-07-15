#factorial function
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Prompt the user for input
#number = int(input("Enter a non-negative integer: "))

# Calculate the factorial
result = factorial(3)

# Display the result
print("The factorial of", 3, "is", result)