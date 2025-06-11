# 45. Sort a dictionary by value  

student_details = {
    "Ram": 60,
    "Shyam": 70,
    "Hari": 80,
    "Sita": 75
}

# Sort dictionary items by value (marks), ascending order
sorted_by_value = dict(sorted(student_details.items(), key=lambda item: item[1]))

print("Sorted by value (ascending):", sorted_by_value)
