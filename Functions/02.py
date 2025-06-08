num = int(input("Enter a number: "))

def factorial(n):
    if n == 0 or n == 1:
        return 1  
    else:
        return n * factorial(n - 1)  

result = factorial(num)  
print("Factorial of", num, "is", result)
