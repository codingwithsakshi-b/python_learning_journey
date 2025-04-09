# Print "hello" 5 times
for i in range(5):
    print("hello")

# Print "sakshi" with numbers 1 to 100
i = 1
while i <= 100:
    print(f"{i}. 🌸 sakshi")
    i += 1
    #or

print("Counting my Sakshi vibes! 💖")
i = 1
while i <= 100:
    print(f"{i}) sakshi")
    i += 1

# Print numbers from 1 to 100
for i in range(1, 101):
    print(i)

# Print numbers from 100 to 1 (reverse loop)
for i in range(100, 0, -1):
    print(f"⏳ Counting down: {i}")
print("🚀 Blast off! 🎉")

# Demonstrate break in while loop (stop at 3)
i = 1
while i <= 5:
    print(i)
    
    # Break loop when i becomes 3
    if i == 3:
        break
    
    i += 1

# Demonstrate continue in while loop (skip 3)
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

# Print multiplication table of a number n
n = int(input("Enter a number: "))
i = 1
print(f"\n🔢 MULTIPLICATION TABLE OF {n} 🔢\n")

while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1

# Print square numbers from 1 to 10
i = 1
while i <= 10:
    print(f"SQUARE OF {i} = {i**2}")
    i += 1

# Print elements from list using indexing
num_list = [1, 2, 3, 4, 5]
idx = 0

while idx < len(num_list):
    print(f"Number at index {idx} → {num_list[idx]}")
    idx += 1

# Search a number in tuple with and without break
num_tup = (1, 4, 9, 16, 25)
idx = 0
search = int(input("ENTER A NUMBER TO SEARCH: "))

while idx < len(num_tup):
    if num_tup[idx] == search:
        print("SEARCHED NUMBER FOUND!")  # This will print every time match is found
    else:
        print("SEARCHING...")
    idx += 1

num_tup = (1, 4, 9, 16, 25)
idx = 0
search = int(input("ENTER A NUMBER TO SEARCH: "))

while idx < len(num_tup):
    if num_tup[idx] == search:
        print(f"SEARCHED NUMBER FOUND at INDEX: {idx}")
        break
    else:
        print("SEARCHING...")
    idx += 1

# Print all odd numbers from 1 to 100 using continue
for i in range(1, 101):
    if i % 2 == 0:
        continue
    print(i)

# Print elements of list [1,4,9,...] using for loop
squares = [1,4,9,16,25,36,49,64,81,100]

print("🔢 Printing Square Numbers:")
for num in squares:
    print(f"➡️ {num}")

# Search a number in tuple using for loop
num_tup = (1,4,9,16,25,36,49,64,81,100)
search = int(input("ENTER A NUMBER FOR SEARCH: "))
idx = 0

for el in num_tup:
    if el == search:
        print(f"HURRAYYYY! 🎉 NUMBER FOUND at INDEX {idx}")
        break
    idx += 1
else:
    print("NUMBER NOT FOUND! 😓")

# Print odd numbers from 1 to 100 using range()
print("ODD NUMBERS FROM 1 TO 100💙")
for el in range(1, 101, 2):
    print(el)


# Print even numbers from 1 to 100 using range()
print("NUMBERS FROM 1 TO 100 🧮")
for el in range(1, 101):
    print(el, end=" ")

# Print numbers from 10 to 1 using range()
import time

for el in range(10, 0, -1):
    print(f"⏳ Counting down: {el}")
    time.sleep(1)

print("BLAST OFFFFFFF.....🚀🚀")

# Print multiplication table of number p using for loop
# Print multiplication table of a number using for loop

p = int(input("Enter a number: "))
print(f"\n🔢 Multiplication Table of {p}:\n")

for el in range(1, 11):
    print(f"{p} x {el} = {p * el}")

# Find sum of first n numbers
# Find sum of first n natural numbers

n = int(input("ENTER A NUMBER TO FIND SUM OF FIRST N NATURAL NUMBERS: "))
total_sum = 0

for i in range(1, n + 1):
    total_sum += i

print(f"\nTOTAL ➕ SUM OF FIRST {n} NATURAL NUMBERS 🟰 {total_sum}")

# Find factorial of a number
# Find factorial of a number

f = int(input("ENTER A NUMBER TO FIND FACTORIAL❗: "))
fac = 1

for i in range(1, f + 1):
    fac *= i

print(f"\n❗ FACTORIAL of {f} is ➡️ {fac}")

# Print each element of a string (e.g. "sakshicoder") until 'o' is found, then break
