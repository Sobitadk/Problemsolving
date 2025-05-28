# 22. Generate a pyramid pattern of stars 

# Example (for 5 rows):
#     *    
#    ***   
#   *****  
#  ******* 
# *********

rows = int(input("Enter the rows for the pattern : "))
for i in range(rows):
    
    for j in range(rows - i - 1):
        print(" ", end="")

    
    for k in range(2 * i + 1):
        print("*", end="")

    print()  
