#leap year checker
yr = int(input("enter year:"))

if(yr%4 == 0 and yr%100 != 0) or (yr%400 == 0):
    print("leap year")
else:
    print("not a leap year")