# 21. Generate a simple number triangle pattern 


# Example (for 5 rows):
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5



rows =int(input("Enter the rowws for the pattern : "))

for i in range (1,rows+1):
    
    for j in range (1,i+1):
        print(j,end=" ")
    print()
        
