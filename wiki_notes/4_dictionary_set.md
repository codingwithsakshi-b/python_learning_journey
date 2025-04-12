# 📘 Dictionary And Set 

---

## 📘 Python Dictionaries
---
### 📌 Creating a Dictionary
```python
my_dict = {
    "name": "Sakshi",
    "age": 18,
    "branch": "CSE-AIML"
}
```
---
### 🔍 Accessing Elements
```python
print(my_dict["name"])      # Output: Sakshi
print(my_dict.get("age"))   # Output: 18
```
---
### 🧰 Dictionary Methods
| Method          | Description                                             |
|----------------|---------------------------------------------------------|
| `dict.get(key)`    | Returns the value for the specified key                |
| `dict.keys()`      | Returns a view object of all keys in the dictionary    |
| `dict.values()`    | Returns a view object of all values                    |
| `dict.items()`     | Returns a view object of key-value pair tuples         |
| `dict.update()`    | Updates the dictionary with elements from another dict |
| `dict.pop(key)`    | Removes the key and returns its value                  |
| `dict.clear()`     | Removes all items from the dictionary                  |
| `dict.copy()`      | Returns a shallow copy of the dictionary               |
| `dict.popitem()`   | Removes and returns the last inserted key-value pair   |
| `dict.setdefault()`| Returns value of key; if not found, inserts with default|

---

### ➕ Adding/Updating Elements
```python
my_dict["college"] = "JECRC"  # Adds new key
my_dict["age"] = 19           # Updates existing key
```
---
### ❌ Removing Elements
```python
my_dict.pop("branch")  # Removes 'branch' key
```
---
### 🧩 Nested Dictionary
```python
student = {
    "name": "Sakshi",
    "marks": {
        "python": 95,
        "maths": 88
    },
    "college": "JECRC"
}
```
---
** Access Nested Value **
```python
print(student["marks"]["python"])  # Output: 95
```

---

## 🪄 Python Sets
---
### 📌 Creating a Set
```python
my_set = {1, 2, 3, 4}
empty_set = set()  # NOT {}
```
---
### ⚙️ Properties of Sets
- Unordered (no index)
- No duplicate values
- Mutable (can add/remove elements)
- Elements must be immutable types

---
### ➕ Adding Elements
```python
my_set.add(5)       # Adds a single element
my_set.update([6, 7])  # Adds multiple elements
```
---
### ❌ Removing Elements
```python
my_set.remove(2)   # Removes element 2 (Error if not present)
my_set.discard(3)  # Removes element 3 (No error if not present)
my_set.pop()       # Removes a random element
my_set.clear()     # Empties the set
```
---
### 🔄 Set Operations
| Operation             | Syntax                          | Description                             |
|-----------------------|----------------------------------|-----------------------------------------|
| Union                 | `set1 | set2` or `set1.union(set2)` | Returns all unique elements from both sets |
| Intersection          | `set1 & set2` or `set1.intersection(set2)` | Returns common elements in both sets       |
| Difference            | `set1 - set2` or `set1.difference(set2)` | Returns elements in set1 but not in set2  |
| Symmetric Difference  | `set1 ^ set2` or `set1.symmetric_difference(set2)` | Elements in either set but not in both |
| Subset Check          | `set1.issubset(set2)`           | Checks if set1 is a subset of set2       |
| Superset Check        | `set1.issuperset(set2)`         | Checks if set1 is a superset of set2     |
| Disjoint Check        | `set1.isdisjoint(set2)`         | Returns True if sets have no elements in common |

---

### 🧪 Set Membership
```python
print(2 in my_set)     # True
print(10 not in my_set)  # True
```
---
### 🧰 Set Methods
| Method                  | Description                                     |
|-------------------------|-------------------------------------------------|
| `add(elem)`             | Adds `elem` to the set                          |
| `update(iterable)`      | Adds multiple elements to the set               |
| `remove(elem)`          | Removes `elem`; throws error if not found       |
| `discard(elem)`         | Removes `elem`; no error if not found           |
| `pop()`                 | Removes and returns a random element            |
| `clear()`               | Empties the entire set                          |
| `union(set2)`           | Returns a new set with all elements from both   |
| `intersection(set2)`    | Returns a set with common elements              |
| `difference(set2)`      | Returns a set with elements only in the original set |
| `symmetric_difference(set2)` | Returns a set with elements in either but not both |
| `copy()`                | Returns a shallow copy of the set               |

---

## 📚Summary 
### Python Dictionaries:
- 📖 Store data as key-value pairs.
- 🔑 Access values using keys (e.g., my_dict["name"]).
- ✍️ Add/Update elements with dict[key] = value.
- ❌ Remove elements using pop(key) or del.
- 🔄 Methods: get(), keys(), values(), items(), and more.
- 🧩 Nested Dictionaries: Store dictionaries inside other dictionaries.
- 🔍 Efficient for fast lookups and data organization.

### Python Sets:
- 🔢 Unordered collection of unique elements.
- 🚫 No duplicates allowed.
- ➕ Add elements with add() and update().
- ❌ Remove elements with remove(), discard(), or pop().
- 🔄 Perform set operations: Union, Intersection, Difference, Symmetric Difference.
- 🔍 Methods: issubset(), issuperset(), isdisjoint(), and more.
- 🧪 Check membership with in or not in.

---

## Quote💫🚀
> "Programming is not about what you know; it's about what you can figure out." – Chris Pine
---
