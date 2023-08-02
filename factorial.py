# Find the factorial of the given number.
def factorial(n):
    if n==0:
        return 1
    else:
        result= 1
        for i in range(1, n+1):
            result *= i
        return result
        
   
# Test the function.
print(factorial(0))  # Output: 1
print(factorial(5))  # Output: 120
print(factorial(10)) # Output: 3628800
