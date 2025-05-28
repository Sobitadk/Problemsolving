# 13. Check if a year is a leap year  



# Required Conditions for it to be a leap year:

# If a year is divisible by 4 and not by 100, it's a leap year.
# But if it is divisible by 100, then 
# it must also be divisible by 400 to be a leap year.



year = int(input("Enter a year: "))
if year % 4 ==0 and (year % 100 != 0 or year % 400 == 0):
    print (f"{year} is a leap year")
else:
    print (f"{year} is not a leap year")