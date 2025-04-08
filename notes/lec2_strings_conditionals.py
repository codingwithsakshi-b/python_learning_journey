# 📘 Lecture 2: Strings & Conditional Statements

# 🔹 Strings in Python
str1 = "hello"
str2 = 'world'
str3 = """multi-line
string"""

print(str1, str2)
print(str3)

# 🔹 Indexing
s = "sakshi"
print(s[0])  # First character
print(s[-1]) # Last character

# 🔹 String Slicing
text = "HelloWorld"
print(text[0:5])   # Hello
print(text[:5])    # Hello (same)
print(text[5:])    # World
print(text[::2])   # Hlool
print(text[::-1])  # Reverse: dlroWolleH

# 🔹 String Functions
demo = "  Hello Python  "
print(demo.upper())      # '  HELLO PYTHON  '
print(demo.lower())      # '  hello python  '
print(demo.strip())      # 'Hello Python'
print(demo.replace("Python", "Sakshi"))  # '  Hello Sakshi  '
print(demo.find("Py"))    # index where 'Py' starts

# 🔹 Conditional Statements

# Simple if
age = 18
if age >= 18:
    print("You are eligible to vote!")

# if-else
num = 5
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# if-elif-else
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D or Fail")

# 🔚 Lecture 2 Completed: Strings & Conditionals mastered! 💪😎
