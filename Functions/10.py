# 35. Function to check if a string is an anagram


# 👉 Anagram:
# Two strings are anagrams if they contain the same characters in the same count, but possibly in a different order.
def is_anagram(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    
    return sorted(str1) == sorted(str2)

print(is_anagram("listen", "silent"))  
print(is_anagram("hello", "world"))    
