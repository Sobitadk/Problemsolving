
# 30. Function with default arguments  


# What is a function with default arguments?
# A function can have default values for some of its parameters.
# If you do not provide a value for those parameters when calling the function, the default value will be used.



def greet(name, message="Hello"):
    print(f"{message}, {name}!")

# Calling the function with both arguments
greet("Alice", "Good Morning")   # Output: Good Morning, Alice!

# Calling the function with only one argument
greet("Bob")                     # Output: Hello, Bob!
