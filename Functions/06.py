# 31. Function with variable number of arguments  

#  *args → Variable number of positional arguments
# Use *args to pass any number of positional arguments to a function.
# Inside the function, args will be a tuple.

def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Total:", total)

add_numbers(1, 2, 3)       # 1 + 2 + 3 = 6
add_numbers(10, 20)        # 10 + 20 = 30
add_numbers(5)             # 5


# 2️⃣ **kwargs — Variable Keyword Arguments
# When you use **kwargs, it lets you pass any number of key=value pairs (keyword arguments).

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
print_info(country="Nepal", city="Kathmandu", zip=44600)
