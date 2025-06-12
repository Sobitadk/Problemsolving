# 51. Reverse a string  



# Idea 1

def reverse_string(s):
    return s[::-1]

print(reverse_string("hello"))  # Output: "olleh"




# Idea 2

def reverse_string(s):
    reversed_str = ""
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

print(reverse_string("hello"))  


# Idea 3

def reverse_string(s):
    return ''.join(reversed(s))


print(reverse_string("hello"))  


