# 52. Count vowels and consonants in a string  


def count_vowels_consonants(s):
    vowels = 'aeiou'
    vowel_count=0
    consonant_count=0
    
    for char in s:
        if char.isalpha():
            if char.lower() in vowels:
                vowel_count += 1
            else :
                consonant_count += 1
    return vowel_count, consonant_count


v,c = count_vowels_consonants("Hello World")
print(f"Vowels :{v} and Consonants :{c}")  # Output: Vowels :3 and Consonants