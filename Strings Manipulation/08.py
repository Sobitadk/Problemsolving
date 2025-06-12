# 58. Remove duplicate characters 

def remove_duplicates(s):
    seen = set()
    result = []

    for char in s:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return ''.join(result)

# Examples
print(remove_duplicates("banana"))  # Output: "ban"
print(remove_duplicates("apple"))   # Output: "aple"
