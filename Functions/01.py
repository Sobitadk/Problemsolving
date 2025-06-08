num = int(input("Enter a number: "))

def prime(num):
    count = 0
    for i in range(1, num + 1):  # check from 1 to num
        if num % i == 0:
            count += 1
    
    if count == 2:
        print("Number is prime")
    else:
        print("Number is not prime")

prime(num)
