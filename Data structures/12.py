# 47. Use nested dictionaries  

# A nested dictionary means a dictionary inside another dictionary.
# It's useful when you want to store complex data, 
# like student records where each student has their own dictionary of details.



students = {
    "Ram": {
        "Math": 85, 
        "Science": 90
        },
    
    "Sita": {
        "Math": 95, 
        "Science": 88
        },
    
    "Hari": {
        "Math": 70,
        "Science": 80
        }
}

# Accessing one student's subject marks
print("Sita's Math marks:", students["Sita"]["Math"])

# Adding a new subject to Ram
students["Ram"]["English"] = 75

# Printing all student marks
for name, subjects in students.items():
    print(f"{name}'s marks:")
    for subject, marks in subjects.items():
        print(f"  {subject}: {marks}")
