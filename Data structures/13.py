# 48. Add/remove elements from a set  


my_set = {1, 2, 3}
print("Original set:", my_set)

my_set.add(4)
my_set.add(2)  
print("After adding elements:", my_set)

my_set.remove(2)
print("After removing 2:", my_set)



popped = my_set.pop()
print("Popped element:", popped)
print("Set after pop:", my_set)

# Clear all elements
my_set.clear()
print("After clearing:", my_set)


# Discard elements (won't give error if not found)
my_set.discard(10)  
print("After discarding 10 (which is not present):", my_set)
