sqtup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number you searching... :"))
q = len(sqtup) - 1
a = 0
while a <= q:
    if(sqtup[a] == x):
        print("your number found at index ",a)
    else:
        print("finding......")
    a += 1

#if we want to break the loop at that instant we can add break keyword
sqtup = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number you searching... :"))
q = len(sqtup) - 1
a = 0
while a <= q:
    if(sqtup[a] == x):
        print("number FOUND at index ",a)
        break
    else:
        print("finding...")
    a += 1
print("loop ends")

#print all odd numbers from 1 to 100 using loops

c = 1

while c <= 100:
    if(c%2 == 0): # if we choose != operator it will print all even numbers from 1 to 100
        c += 1
        continue
    print(c)
    c += 1

#print the elements of the following list using for loop

list = [1,4,9,16,25,36,49,64,81,100]

for nums in list:
    print(nums)

#using for loop to search a nummber n

tup = (1,4,9,16,25,36,49,64,81,100)
n = int(input("enter a number:"))
idx=0
for el in tup:
    if(el == n):
        print("number found at idx", idx)
        idx += 1
    
#print even numbers from 1 to 100 using range()

for i in range(2, 100, 2): # range(1, 100 , 2) for odd numbers
    print(i)

print("new que")

#using for and range()
#print numbers from 1 to 100

for i in range(1, 101):
    print(i)
    
#print numbers 100 to 1

print("new que")

for i in range(100, 0, -1):
    print(i)

print("new que")

#print multiplication table of number p

p = int(input("enter a number:"))

for i in range(1,11):
    print(p*i)

#WAP to find sum of first n numbers.

n = int(input("sum of n numbers:"))
 #by using for loop
sum = 0
for i in range(1, n+1):
    sum += i
print("total sum=", sum)

#WAP TO FIND factorial of first n numbers

fac = int(input("enter a number:"))
fac_ = 1

for i in range(1, fac+1):
    fac_ *= i
print("factorial is =",fac_)