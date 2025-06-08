num = int(input("Enter the number: "))

def check_palindrome(n):
    return str(n) == str(n)[::-1]

if check_palindrome(num):
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
