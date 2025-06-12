# 57. Find the first non-repeating character 

def firstNonRepeatingChar(s):
    char_count = {}
    
    for char in s:
        char_count[char]=char_count.get(char,0)+1
        
    for char in s:
        if char_count[char]==1:
            return char
        
    return None


print(firstNonRepeatingChar("swiss"))
print(firstNonRepeatingChar("aabbcc"))