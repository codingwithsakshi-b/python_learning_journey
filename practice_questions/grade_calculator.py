#i tried this question by meself and also i write code of my educator 

#BY MESELF

marks = input("enter the marks of the student:")

if(marks >= "90"):
    print("grade A")
elif(marks >= "80"):
    print("grade B")
elif(marks >= "70"):
    print ("grade C")
elif (marks >= "60"):
    print("grade D")
else:
    print("failed the examination")

#BY EDUCATOR (she used and operator!)

marks = int(input("enter student marks:"))

if(marks >= 90):
    grade= "A"
elif(marks >= 80 and marks < 90):
    grade = "B"
elif (marks >=70 and marks< 80):
    grade = "C"
else:
    grade = "D"

print("student grade is -->", grade)