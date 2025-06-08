def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    else:
        return x / y

num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter the second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1/2/3/4): "))

if choice == 1:
    print(num_1, "+", num_2, "=", add(num_1, num_2))
elif choice == 2:
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))
elif choice == 3:
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))
elif choice == 4:
    print(num_1, "/", num_2, "=", divide(num_1, num_2))
else:
    print("Invalid input! Please select a valid choice (1/2/3/4).")
