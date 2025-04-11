# 📘 Lecture 7 – File I/O Practice Questions
# 📝 Created by Sakshi | 💅 Polished by Aryan

# 🔹 Q1. Create a file "practice.txt" using Python and add data
# 📄 Data: Contains the word "Java" multiple times

f = open("practice.txt", "w")
f.write("Hi Everyone \nwe are learning File I/O \nusing Java. \nI like programming in Java.")
f.close()

# 🔹 Replace all occurrences of "Java" with "python"
f = open("practice.txt", "r")
data = f.read()

new_data = data.replace("Java", "python")
print(new_data)
f.close()

f = open("practice.txt", "w")
f.write(new_data)
f.close()

# 🔹 Q2. Take a word input from user and search if it exists in the file
# ✅ Using 'with' syntax

def search_word():
    with open("practice.txt", "r") as f:
        data = f.read()
        word = input("Enter your word to find: ")

    if data.find(word) != -1:
        print(f"🎉 '{word}' found!")
    else:
        print(f"❌ Sorry, '{word}' not found in the file.")

# 🔹 Q3. Find line number where the word first occurs in file

def serach_line_no():
    with open("practice.txt", "r") as f:
        word = input("Enter your word to find: ")
        data = True
        line_no = 1

        while data:
            data = f.readline()
            if word in data:
                print(f"✅ '{word}' found on line {line_no}.")
                return
            line_no += 1
        else:
            print(f"❌ '{word}' not found in any line.")

# 🔹 Q4. From a file containing numbers (comma-separated), count even numbers

count = 0
with open("num.txt", "r") as f:
    data = f.read()

    nums = data.split(",")
    for val in nums:
        if int(val) % 2 == 0:
            count += 1

print(f"🔢 Total even numbers in your data: {count}")
