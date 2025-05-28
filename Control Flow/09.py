             # 19. Print the Fibonacci sequence  




   # Fibonacci Sequence:
   # A sequence where each number is the sum of the two previous numbers.
   # It starts with 0 and 1.
   # Example: 0, 1, 1, 2, 3, 5, 8, 13, ...


num = int(input("Enter a number: "))
a,b=0,1
print("Fibonacci sequence:")
for i in range(num):
    print(a,end="") 
    a,b=b,a+b