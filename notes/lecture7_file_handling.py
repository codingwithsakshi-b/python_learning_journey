# 📘 Lecture 7 – File I/O in Python
# ✍️ Notes by Sakshi | 💅 Polished by Aryan

# 🧾 Focus: read(), write(), append(), with, delete

# 🔹 Reading a File (Basic read)
f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()  # 🔐 One of the most underrated but important steps

# 🔹 Reading specific characters
f = open("demo.txt", "r")
data = f.read(5)  # 📏 Reads the first 5 characters
print(data)
f.close()

# 🔹 Reading line by line
f = open("demo.txt", "r")
line1 = f.readline()
print(line1)  # 📝 Line 1

line2 = f.readline()
print(line2)  # 📝 Line 2

line3 = f.readline()
print(line3)  # 📝 Line 3
f.close()

# 🔹 Writing to a File
f = open("demo.txt", "w")  # 🧹 Overwrites everything in the file
f.write("I want to learn JavaScript After Python.")
f.close()

# 🔹 Appending to a File
f = open("demo.txt", "a")  # ➕ Adds to the end of the file
f.write("\nI currently doing some mini project, And doing my best.")
f.close()

# 🔹 Writing to a New File
f = open("sample.txt", "w")  # 📁 Creates and writes to a new file
f.write("this is a new file. say hello")
f.close()

f = open("sample2.txt", "a")  # ➕ Creates/appends if exists
f.write("hey i am created by append mode.")
f.close()

# 🔹 Merging Modes – r+ and a+
f = open("sample.txt", "r+")
f.write("ABC")            # 🧼 Overwrites at beginning
print(f.read())           # Reads the remaining content
f.close()

f = open("sample.txt", "a+")
f.write("\nABC")          # ➕ Adds at the end
print(f.read())           # ❌ Will print nothing (cursor at EOF)
f.close()

# 🔹 With Statement (Auto-close)
with open("sample2.txt", "a+") as f:
    data = f.read()       # Reads content
    f.write("\nagain a new line hie there...")  # ➕ Writes new line

# ✅ No need for f.close() when using 'with' – it auto-closes the file

# 🔥 Deleting a File using OS Module
import os
os.remove("sample.txt")  # ⚠️ Deletes 'sample.txt' permanently


