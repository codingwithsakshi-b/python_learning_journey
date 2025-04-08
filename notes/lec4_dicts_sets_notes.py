#DICTIONARY IN PYTHON

student = {
       "name": "Sakshi",
       "marks":96.2,
       "subjects":["physics","chemistry","mathematics"],
       "learning": "python from apnacollege",
       "today topics": ("dictionary","set")
}
print(student)
print(type(student))
print(student["learning"])#prints value

student["college"] = "JECRC University" #adds a new key and value
student["marks"] = 98.2 #change the value (mutable)
print(student)

#null dictionary 
null = {}

print(null) 
null["name"] = "sakshi" #add a key and value
print(null)

#nested dictionary

keshavinfo = {
    "name": "keshav",
    "currently": "biotech",
    "class": "12th",
    "subject": ["physics","chemistry","biology"],
    "marks": {
        "phy": 91,
        "che": 98,
        "bio": 95,
    }
}
print(keshavinfo)
print(keshavinfo["name"])
print(keshavinfo["marks"])
print(keshavinfo["marks"]["bio"])

#DICTIONARY METHOD
#chalo keshavinfo wala dictionary ka method use me dalte hain

print(keshavinfo.keys())#print all the keys
print(list(keshavinfo.keys()))#we typecast the keys into list
print(len(list(keshavinfo.keys())))#length of list of keys in keshavinfo dict

print(keshavinfo.values())#print all the values in dictionary
print(list(keshavinfo.values()))#type cast to list

print(keshavinfo.items())#print pair of (key,value) as tuples
print(list(keshavinfo.items()))#type cast

pairs = list(keshavinfo.items())
print(pairs[0])
print(pairs[2])

print(keshavinfo.get("marks"))

keshavinfo.update({"city":"Bihar"})
print(keshavinfo)
UPDATEITEM = {"age" : "19" , "class" : "semester 2" , "currently": "Bpharma" , "city": "Jaipur"}
keshavinfo.update(UPDATEITEM)
print(keshavinfo)
# print(keshavinfo.update({"university":"JECRC"})) isko aise nahi likh sakte

#SET IN PYTHON
#set is collection of the unordered items.set is mutable
#each elements in the set must be unique and immutable.

nums = {1,2,3,4,"hello",5} #wee cannot store dictionary and lists bc they are mutable
set1 = {1,2,2,2,2}
print(set1)
print(type(nums))
print(len(set1))
print(nums)

nulldict = {} #null dict
nullset = set() #null set
print(type(nulldict))
print(type(nullset))

#SET METHODS

nullset.add(1) #add an element to set
nullset.add(4)
nullset.add("world")
nullset.add((1,2,6,7)) #double bracket dena pdega tuple add karne k liye
print(nullset)
nums.add("world")
print(nums)

nums.remove(2)# removes an element
print(nums)
nullset.remove(4)
print(nullset)

nullset.clear() #empties the set
print(nullset)

nums.pop() #removvve a random value
print(nums.pop())

set2 = {1,2,3,"sakshi", "keshav","Jaipur"}
set3 = {"sakshi","Bihar","kota",2,6,8}

print(set2.union(set3))# {1,2,3,6,8,"sakshi","keshav","jaipur","bihar","kota"}
print(set2.intersection(set3))#{2,sakshi}

# Dictionary check:
my_dict = {"name": "Sakshi", "age": 19}
print("name" in my_dict)        # True
print("Sakshi" in my_dict)      # False (because keys are checked)

# Set check:
my_set = {1, 2, 3}
print(2 in my_set)              # True
print(5 in my_set)              # False

# --------------------------------------------
# 🔁 Difference Between Dictionary and Set:

# Dictionary:
# - Key-Value pairs (e.g., {"name": "Sakshi"})
# - Mutable, keys must be unique and immutable
# - Ordered (since Python 3.7+)

# Set:
# - Only values, no keys (e.g., {"apple", "banana"})
# - All values are unique
# - Unordered collection
# --------------------------------------------
