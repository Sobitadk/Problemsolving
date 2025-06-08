# 33. Return multiple values from a function  


def calculate(a, b):
    sum_ = a + b
    product = a * b
    return sum_, product

result_sum, result_product = calculate(3, 4)
print("Sum:", result_sum)         # Output: Sum: 7
print("Product:", result_product) # Output: Product: 12
