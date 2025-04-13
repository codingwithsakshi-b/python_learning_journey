#OOPS in python
a = 10
b = 20

sum = a + b
diff = a - b
print(sum)
print(diff) #procedurel prpgramming

#then we discuss about functions(reusebility,reduce reduntancy)
#procedurel -> functional -> object oriented programming

#Class & Object in python
#creating class
class Student:
    name = "Sakshi Sharma"

#creating object (instances of object)
s1 = Student()
print(s1.name)
print(s1)

#making a factory of ccar
class Car:
    colour = "red"
    brand = "mercedes"
car1 = Car()
print(car1.colour)
print(car1.brand)

#__init__ function
#data stores in class or object called Attributes

class Student:
    college_name = "JECRC University"
#default constructor
    def __init__(self):
      pass

#parameterized constructor
    def __init__(self, fullname, marks):
        self.name = fullname
        self.mark = marks
        print("Adding new student.....")
        print(f"\nStudent Name: {self.name}")
        print(f"Student Marks: {self.mark}")
        print(f"College Name: {self.college_name}")
        print("------------------\n")
s1 = Student("Sakshi Kumari", 98.6)
s2 = Student("Keshav Sharma", 78.6)  

#Class Methods
class Student_info:
    college_name = "JECRC University"
    def welcome():
        return("📃 Welcome in Student Info...")
        
    def __init__(self, fullname, marks, course):
        self.Name = fullname
        self.Mark = marks
        self.Course = course

        print(Student_info.welcome())
        print(f"\n📛 Student Fullname: {self.Name}")
        print(f"Ⓜ️ Student Marks: {self.Mark}")
        print(f"📚 Student course: {self.Course}")
        print(f"🎓 Student College Name: {self.college_name}")
        print("-------------------\n")

s1 = Student_info("Sakshi Kumari", 89.6, "Btech")
s2 = Student_info("Keshav Sharma", 85.6, "Bpharma")       
#we can add more info of students.

#Static Methods
class Student:
    @staticmethod
    def college():
        print("JECRC University\n")

Student.college()