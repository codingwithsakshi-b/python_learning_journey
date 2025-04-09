
# Check if Sum of First and Last Elements Exists in the List 

list = eval(input("enter a list:"))
s = list[0] + list[-1]
if(s in list ):
    print("Yes")
else:
    print("No")
