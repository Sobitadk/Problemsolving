# 34. Write a function to count vowels in a string  


def count_vowels(s):
    vowels = 'aeiou'
    count = 0
    for char in s:
        if char in vowels :
            count += 1
    return count

text =input("Ente the text :")

print(f"Number of vowels in {text} is ",count_vowels(text))