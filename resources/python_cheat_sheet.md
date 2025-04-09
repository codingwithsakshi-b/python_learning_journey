#🐍 Sakshi's Python Cheat Sheet - Beginner to Basic+
🔢1. Input/Output
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello", name, "you are", age, "years old.")

🔢2. Data Types
int, float, str, bool

Type conversion:
int("5"), float("5.2"), str(10)

🔢 3. Strings
s = "hello"
print(s[0])         # h
print(s[-1])        # o
print(s[::-1])      # reverse
.upper(), .lower(), .replace(), .find(), .strip()

📋 4. Lists
my_list = [1,2,3]
my_list.append(4)
my_list.sort()
print(my_list[::-1]) # Reverse
~List comprehension:
even = [x for x in my_list if x % 2 == 0]

📙 5. Tuples
tup = (1, 2, 3)
print(tup[1]) # Access element

📚 6. Dictionaries
student = {
  "name": "Sakshi",
  "age": 18,
  "hobby": "Coding"
}
print(student["name"])
.update(), .keys(), .values()

🔐 7. Sets
my_set = {1, 2, 2, 3}
my_set.add(4)
print(my_set)  # No duplicates

🔁8. Loops
# for loop
for i in range(1, 6):
    print(i)

# while loop
i = 1
while i <= 5:
    print(i)
    i += 1
break, continue, pass

🧠 9. Practice Snippets
# Sum of list
lst = [1, 2, 3]
print(sum(lst))

# Factorial
n = 5
f = 1
for i in range(1, n+1):
    f *= i
print(f)

# Palindrome Check
word = input("Enter word: ")
print("Palindrome" if word == word[::-1] else "Not Palindrome")

🛠️ 10. Useful Built-ins
len(), type(), sum(), input(), print()

sorted(), range(), zip()











