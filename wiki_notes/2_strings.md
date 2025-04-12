# 🧵 Lecture 2: Strings in Python

---

## 📌 1. Creating Strings

### python
str1 = 'Hello'
str2 = "World"
str3 = '''This is
a multi-line string.'''

---

## Indexing and Slicing

### 📍 Indexing
| Operation           | Code             | Output |
|---------------------|------------------|--------|
| Access 1st character | "Python"[0]       | 'P'    |
| Access last char    | "Python"[-1]      | 'n'    |

### ✂️ Slicing
| Operation           | Code             | Output |
|---------------------|------------------|--------|
| Basic slice         | "Python"[1:4]    | 'yth'  |
| Slice from start    | "Python"[:3]     | 'Pyt'  |
| Slice to end        | "Python"[3:]     | 'hon'  |
| Reverse string      | "Python"[::-1]   | 'nohtyP' |

---

## 🔁 4. Palindrome Checker
### python
word = input("Enter a word: ")
if word == word[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

---

## ✨ String Methods
### Common Methods
- .upper() – Converts a string to uppercase.
- .lower() – Converts a string to lowercase.
- .replace(old, new) – Replaces a substring with another.
- .split(separator) – Splits the string by a separator and returns a list.
- .find(sub) – Returns the index of the first occurrence of a substring.
### python
text = "Hello, world!"
print(text.upper())  # 'HELLO, WORLD!'
print(text.lower())  # 'hello, world!'
print(text.replace("world", "Python"))  # 'Hello, Python!'

---

### 💡 Escaping Characters
n strings, you can escape characters using a backslash (\) to insert special characters:
- \n for new line
- \t for Tab
- \\ backslash

---

## ✨ Summary
- Strings are immutable.
- Access via indexing, modify/view with slicing.
- Use string functions for case change, splitting, searching, etc.
- You can check for palindromes using slicing.
- Escape characters allow inserting special characters in strings.



