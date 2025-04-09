#create a dictionary that stores the names of three students as keys
#and print their marks neatly

file = {
    "Karan":96,
    "Arjun":89,
    "Govind":90,
}

print("three students marks:",file)

#create a dictionary that stores info about a person.
#it should contain their name , age, and favorite language.

name = input("enter your name:")
age = input("enter your age:")
fav_lan = input("input your favorite language:")

info = {
    "name": name,
    "age": age,
    "favorite language": fav_lan
}

print("welcome", name)
print("your information:", info)

#create a dictionary from two lists 
#one list contains student names and other list corresponding marks
#a dictionary where name is a key and the mark is the value

names = ["Sakshi","Keshav","Govind"]
marks = ["98","97","94"]

Grades = {
    names[0] : marks[0],
    names[1] : marks[1],
    names[2] : marks[2]
}

print("students marks:", Grades)

#create a dictionary where each student name maps to another dict 
#contains their marks in math and science

student = input("enter names of student:").split()
m1 = list(map(float, input("enter math marks:").split()))
m2 = list(map(float, input("enter science marks:").split()))

result = dict(zip(student, [{'math': m1, 'science': m2}for m1 , m2 in zip(m1,m2)]))

print(result)

#WAP that user first and last name and print their full name

first_name = input("enter you first name:").capitalize()
last_name = input("enter you last name:").capitalize()

print("your full name is:", first_name + " " + last_name)

#wap that takes input from user name age and fav hobbie

user = input("enter your name:").capitalize()
user_age = input("enter your age:")
favorite_hobby = input("enter your favorite hobby:").capitalize()

print("Hello, my name is "+ user+".")
print("I am "+user_age+" years old.")
print("My favorite hobby is "+favorite_hobby+".")

#WAP to take two numbers from the user and print sum avg and product

f1 = float(input("enter you first number:"))
f2 = float(input("enter you second number:"))

sum_ = f1+f2
prod = f1*f2
avg = sum_/2

print("------RESULTS------")
print("Their sum is:",sum_)
print("Their product is:",prod)
print("Their average is:",avg)

#take name as input from the use and print

n1 = input("enter your name:").capitalize()

print("Hello, "+n1+ "! Welcome to Python.")

#take input of first and last name and print

n1 = input("enter your first name:").capitalize()
n2 = input("entr your surname:").capitalize()

full_name = n1 + n2
len_fullname = str(len(full_name))

print("hello, "+ n1 + " " + n2 + "! Your name has " + len_fullname + " characters.")

#ask user name and birth year and print name and age

user_name = input("enter your name:").capitalize()
birth_year = int(input("enter birth year:"))

current_year = 2025
current_age = current_year - birth_year

print(f"Hello, {user_name}! you are {current_age} years old.")

#take name and age as input and print when they turned 100

user_name = input("enter your name:").capitalize()
user_age = int(input("enter your age:"))

current_year = 2025
turned_100 = (100 - user_age) + current_year

print(f"Hello, {user_name}! you will turn 100 years old in the year {turned_100}.")


