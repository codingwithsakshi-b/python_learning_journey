# Print "hello" 5 times

count = 1
while count <= 5:
    print("hello")
    count += 1

# Print "sakshi" with numbers 1 to 100

i = 1
while i <= 100:
    print("sakshi",i)
    i += 1

# Print numbers from 1 to 100

i = 1
while i <= 100:
    print(i)
    i += 1

# Print numbers from 100 to 1 (reverse loop)
i = 100
while i >= 1:
    print(i)
    i -= 1

# Demonstrate break in while loop (stop at 3)
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1

# Demonstrate continue in while loop (skip 3)
i = 1
while i <= 5:
    if(i == 3):
        i += 1
        continue
    print(i)
    i += 1

# Print multiplication table of a number n
n = int(input("Enter a number:"))
i = 1
print (f"MULTIPLICATION TABLE OF {n}:")
while i <= 10:
    print(n*i)
    i += 1

# Print square numbers from 1 to 10
i = 1
while i <= 10:
    print(f"SQUARES OF NUMBER {i}={i**2}")
    i += 1

# Print elements from list using indexing

num_list = [1,2,3,4,5]
idx = 0
while idx < len(num_list):
    print(f"Number at Index {idx} is {num_list[idx]}")
    idx += 1

# Search a number in tuple with and without break
num_tup = (1,4,9,16,25)
idx = 0
search = int(input("ENTER A NUMBER FOR SERACH:"))
while idx < len(num_tup):
    if(num_tup[idx] == search):
        print("SEARCHED NUMBER FOUND!") # without break
    else:
        print("SEARCHING")
    idx += 1

num_tup = (1,4,9,16,25)
idx = 0
search = int(input("ENTER A NUMBER FOR SERACH:"))
while idx < len(num_tup):
    if(num_tup[idx] == search):
        print(f"SEARCHED NUMBER FOUND! at INDEX:{idx}") # with break
        break 
    else:
        print("SEARCHING")
    idx += 1
    
# Print all odd numbers from 1 to 100 using continue
i = 1
print("ODD NUMBERS FROM 1 TO 100 ARE:")
while i <= 100:
    if(i%2 == 0): #if we choose != instead of == then it will print all even numbers.
        i += 1
        continue #it skips the even numbers.
    print(i)
    i += 1

# Print elements of list [1,4,9,...] using for loop

list = [1,4,9,16,25,36,49,64,81,100]

for el in list:
    print(el)

# Search a number in tuple using for loop
num_tup = (1,4,9,16,25,36,49,64,81,100)
search = int(input("ENTER A NUMBER FOR SEARCH:"))
idx = 0

for el in num_tup:
    if(el == search):
        print(f"HURRAYYYY! NUMBER FOUND🎉 at INDEX {num_tup[idx]}")
        break
    idx += 1
else:
    print("NUMBER NOT FOUND!😓")

# Print even numbers from 1 to 100 using range()
print("EVEN NUMBERS FROM 1 TO 100❤️")
for el in range(2,101,2):
    print(el)

# Print numbers from 1 to 100 using range()
for el in range(1,101):
    print(el)
    #if wanting to write in a same line
for el in range(1,101):
    print(el, end=" ")

# Print numbers from 100 to 1 using range()
for el in range(100,0,-1):
    print(f"⏳ Counting down: {el}")

print("BLAST OFFFFFFF.....🚀🚀")

# Print multiplication table of number p using for loop
p = int(input("ENTER A NUMBER:"))
print(f"\nMULTIPLICATION TABLE OF {p}:")

for el in range(1,11):
    print(f"{p} x {el} = {p*el}")

# Find sum of first n numbers

n = int(input("ENTER A NUMBER YOU WANT TO SUM OF FIRST N NUMBERS:"))
total_sum = 0

for i in range(1,n+1):
    total_sum += i

print(f"TOTAL ➕ SUM OF {n} NATURAL NUMBER 🟰  {total_sum}")

# Find factorial of a number

f = int(input("ENTER A NUMBER TO FIND FACTORIAL!:"))
fac = 1

for i in range(1, f + 1):
    fac *= i

print(f"❗ FACTORIAL! of {f} IS ➡️  {fac}.")

# Print each element of a string (e.g. "sakshicoder") until 'o' is found, then break
name = "sakshicoder"
idx = 0
for el in name:
    if(el=="o"):
        print(f"WE FOUND! 🎉 ALPHABET ⭕ 'O' AT INDEX {idx}")
        break
    print(el)
    idx += 1

# Use of for loop with else block
numbers = [2, 4, 6, 8, 10]
search = int(input("Enter a number to search: "))

for num in numbers:
    if num == search:
        print(f"Number {search} found!")
        break  # Exit the loop if the number is found
else:
    print(f"Number {search} not found in the list.")
