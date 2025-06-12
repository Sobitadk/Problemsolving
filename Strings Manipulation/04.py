# 54. Remove spaces from a string  

def remove_spaces(s):
    return "".join(c for c in s if c != ' ')

print(remove_spaces("Hello World"))  # Output: "HelloWorld"
