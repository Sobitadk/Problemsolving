# 23. Find the sum of digits of  a number  


num = int(input("Enter a number: "))

sum = 0

while num>0 :
    sum =sum+num%10
    num=num//10
    
print(f"The sum of digits of number is {sum}")