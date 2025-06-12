# 53. Check if a string is a palindrome  



def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())  
    return s == s[::-1]


print(is_palindrome("RaceCar"))                      
print(is_palindrome("A man a plan a canal Panama"))  






# def is_palindrome(s):
#     return s == s[::-1]

# # Example
# print(is_palindrome("madam"))   
# print(is_palindrome("hello"))   
