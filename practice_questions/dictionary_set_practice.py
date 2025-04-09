#store the following word meaning in a dictionary

Dictionary = {}

Dictionary.update({"table":("a peice of furniture","list of facts & figures")})
Dictionary.update({"cat":"a small animal"})

print(Dictionary)

             #we can directly make a dict
dictionary = {
    "table": ("a peice of furniture","list of facts & figures"),#we can store them in a list
    "cat" : "a small animal"
}
print(dictionary)

#you are given a list of subject for students . assume one classroom is required for 1 subject how many classroom are needed by all students

subjects = {
    "python","java","c++","python","javascript","java","python","java",
    "c++","c"
    } #case sensitive c++ != C++
classes = len(subjects)
print("number of classroom needed:", classes)

#WAP to enter marks and enter 3 subjects from the userr and store them in a dictionary. start with an empty dictionary & add one by one. use subject as key & marks as value

grade = {}
sub1 = input("enter 1st subject name:")
marks1 = float(input("enter marks of 1st subject:"))
sub2 = input("enter 2nd subject name: ")
marks2 = float(input("enter marks of 2nd subject:"))
sub3 = input("enter 3rd subject name:")
marks3 = float(input("enter marks of 3rd subject:"))

grade.update({sub1:marks1})
grade.update({sub2:marks2})
grade.update({sub3:marks3})

print("hey student here is your info:",grade)

#figure out a way to store 9 and 9.0 as a seperate values in a set

set = set()

integer = "9" # as a string it is different
decimal = float("9.0")

set.add(integer)
set.add(decimal)

print(set)
