# 24. Reverse a number using a loop  

num = int(input("Enter the number : "))
reversed_num = 0
while num != 0:
    remainder = num % 10
    reversed_num = reversed_num * 10 + remainder
    num = num // 10
print("Reversed Number is : ", reversed_num)