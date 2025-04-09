#1.sum of lists of elements

list = eval(input("enter a list:"))
total = sum(list)
print("sum of list of elements:",total)

#WAP to find the larest number in a list entered by the user

list = eval(input("enter a list:"))
list.sort()
print("largest number in list is:",list[-1])

#WAP to count how many even numbers entered by user in a list

list = eval(input("enter a list:"))
count = 0

for num in list:
    if(num % 2 == 0):
        count += 1
print("number of even elements",count)

#WAP to print the elements of a list in reverse order

list = eval(input("enter a list:"))

reverse = list[::-1]
print("reversed list:", reverse)

#WAP to find the second largest number in a list entered by the user

list = eval(input("enter a list:"))
list.sort()
print("second largest number:",list[-2])

#WAP to count even and odd numbers in a list entered by user

list = eval(input("enter a list:"))
count = 0 
for num in list:
    if(num % 2 == 0):
        count += 1

print("number of even elemens:", count)
print("number of odd elements:", len(list)-count)

#WAP to find the sum of only even numbers in a list entered by the user

list = eval(input("enter a list:"))

s = sum([num for num in list if num % 2 == 0]) # remember this line.ye list comprehension me aata hai
print("sum of even numbers:", s)

#WAP to input a list and print only the elemments which are divisible by 3

list = eval(input("enter a list:"))

div_3 = [num for num in list if num % 3 == 0]
print("divisible by 3:", div_3)


#WAP to input a list and print the square of only the even numbers

list = eval(input("enter a list:"))

even_num = [num for num in list if num % 2 == 0]
result = 1
for num in even_num:
    result *= num
print("product of even numbers:",result)
