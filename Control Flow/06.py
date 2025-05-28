# 16. Display multiplication table of a number  


num =int(input("Enter the Number for Multiplication Table: "))

for i in range (1,11):
    print(f"{num} x {i} = {num*i}")