str = (input("enter a number:"))
last_digit = str[-1]
print("last digit is:", last_digit)

#now we check what is the last digit
check_digit = input("enter the last digit:")
if (last_digit == check_digit):
    print("true")
else:
    print("false")


