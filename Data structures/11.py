# 46. Count frequency of elements in a list using dictionary  

my_list = [1, 2, 2, 3, 4, 4, 4, 5]

frequency = {}

for item in my_list:
    if item in frequency:
        frequency[item] += 1  # Increase count
    else:
        frequency[item] = 1   # First time, set to 1

print("Element frequencies:", frequency)



