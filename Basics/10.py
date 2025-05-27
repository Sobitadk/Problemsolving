#  10. Create a calculator using simple input/output 

 
first_num =int(input("Enter the number :"))
second_num = int(input("Enter the number :"))

print("1.Addition")
print("2.Subtraction")  
print("3.Multiplication")
print("4.Division")
print("5.Modulus")
print("6.Exponentiation")
print("7.Exit")

choice = int(input("Enter your choice (1-7): "))

if choice == 1:
    print(first_num + second_num)
elif choice == 2:
    print(first_num-second_num)
elif choice ==3 :
    print(first_num*second_num)
elif choice == 4 :
    print(first_num*second_num)
elif choice == 5 :
    print(first_num%second_num)
elif choice == 6 :
    print(first_num**second_num)
elif choice == 7 :
    print("Exiting the program")