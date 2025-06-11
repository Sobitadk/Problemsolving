# 39. Remove duplicates from a list  


my_list = [1, 2, 2, 3, 3, 4, 5, 6]
print("Original list:", my_list)

unique_set = set(my_list)  # Convert to set removes duplicates

unique_list = list(unique_set)  # Convert back to list

print("List without duplicates:", unique_list)
