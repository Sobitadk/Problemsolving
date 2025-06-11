# 43. Convert list to tuple and vice versa  



my_list = [1, 2, 3, 4]
print("Original list:", my_list, "Type:", type(my_list))


my_tuple = tuple(my_list)
print("Converted to tuple:", my_tuple, "Type:", type(my_tuple))


original_tuple = (5, 6, 7, 8)
print("Original tuple:", original_tuple, "Type:", type(original_tuple))

converted_list = list(original_tuple)
print("Converted to list:", converted_list, "Type:", type(converted_list))
