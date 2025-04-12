# 🧵 Lecture 3: Lists and Tuples in Python

---

## 📌 1. Lists
>A list is a collection of items in an ordered sequence. Lists are mutable, meaning you can modify them after they are created.
### Creating a list 
```python
my_list = [1, 2, 3, 4, 5]
my_list2 = ["apple", "banana", "kiwi"]
```
### Accessing List Elements
```python
-print(my_list[0])  # Access first element, output: 1
-print(another_list[-1])  # Access last element, output: 'cherry'
```
### Modifying a list
```python
my_list[2] = 10  # Change the third element
print(my_list)  # [1, 2, 10, 4, 5]
```
### 🧰 List Methods

| Method         | Description                                       |
|----------------|---------------------------------------------------|
| `.append(x)`   | Adds an item to the end of the list.              |
| `.insert(i, x)`| Inserts an item at a specified position.          |
| `.remove(x)`   | Removes the first item with the value `x`.        |
| `.pop(i)`      | Removes and returns the item at the specified index. |
| `.sort()`      | Sorts the list in ascending order.                |
```python
my_list.append(6)
my_list.insert(2, 8)
print(my_list)  # [1, 2, 8, 10, 4, 5, 6]
```

---

## 📍 2. Tuples
>A tuple is similar to a list but is immutable, meaning you cannot change its elements once it’s created.
### Creating a Tuple
```python
my_tuple = (1, 2, 3, 4, 5)
another_tuple = ("apple", "banana", "cherry")
```
### Accessing Tuple Elements 
```python
print(my_tuple[0])  # Output: 1
print(another_tuple[-1])  # Output: 'cherry'
```
### Tuple Method
Tuples have fewer methods compared to lists due to their immutability. Here are a few methods:
- .count(x) ~ Returns the number of times x appers in the tuple.
- .index(x) ~ Returns the index of the first occurence of x.
```python
my_tuple = (1, 2, 3, 4, 1)
print(my_tuple.count(1))  # Output: 2
print(my_tuple.index(3))  # Output: 2
```

---

## 📊 Tuple vs List in Python

| Feature           | List                             | Tuple                           |
|------------------|----------------------------------|---------------------------------|
| Syntax           | `my_list = [1, 2, 3]`            | `my_tuple = (1, 2, 3)`          |
| Mutability       | Mutable (can be changed)         | Immutable (cannot be changed)  |
| Methods Available| Many (like append, remove, etc.) | Few (like count, index)         |
| Performance      | Slightly slower                  | Faster than lists               |
| Use Cases        | When data can change             | When data should not change     |
| Memory Usage     | Takes more memory                | Takes less memory               |
| Brackets Used    | Square brackets `[]`             | Round brackets `()`             |

---

## 🔁 3. Converting Between Lists and Tuples
You can easily convert a tuple into a list, and vice versa.
- TUPLE to LIST
```python
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # [1, 2, 3]
```
- LIST to TUPLE
```python
my_list = [4, 5, 6]
my_tuple = tuple(my_list)
print(my_tuple)  # (4, 5, 6)
```

---

## ✨ Summary
-Lists are mutable and can be modified after creation.
-Tuples are immutable and cannot be changed once created.
-Both can store multiple data types and allow access via indexing.
-You can convert between lists and tuples using the list() and tuple() functions.

---

## 💬 Thought of the Day
>"Life is like a tuple; what you choose to add is what you’ll carry forward."

---


