#LISTS IN PYTHON

marks = [94.4, 87.5, 95.2, 56.8, 78.9, 45.5]
print(marks)
print(type(marks))

#we can acess any information from list acc to their index

print(marks[0])
print(marks[1])

#we can print length of the marks
print(len(marks))

student = ["Sakshi", 94.5, 19, "Bihar"]
print(student)
#we can change elements in lists.lists are mutable
student[0]= "Keshav"
print(student)

#LIST SLICING

marks1 = [45,67,89,90,43,67,87,34]
print(marks1[1:])
print(marks1[3:5])
print(marks1[:len(marks1)])
print(marks1[-3:-1])

#LIST METHOD

list = [2,1,3]
print(list)
list.append(4)#add the element at last.mutate the list
print(list)
list.sort()#sort in ascending order
print(list)
list.sort(reverse=True)#sort in descending order
print(list)
list.insert(3,5)#3 jo hai wo index hai or 5 ko index 3 par insert kar dega
print(list)
list.remove(4)#first occurence wala ele ko remove kar dega
print(list)
list.pop(2)#remove ele from given index
print(list)
list.reverse()#reverse the list
print(list)

#TUPLES IN PYTHON
#a built in data type that let us create immutable sequence of values

tup = (87,64,33,95,76,87)
print(tup)
print(type(tup))
print(tup[1])
#tup[0]=5 we cannot do this tuple of python

tup1 = () #empty tuple
tup2 = (1,)# single tuple
print(tup2)
print(type(tup2)) 

print(tup[1:4])#slicing of tuple

#tuple methods
print(tup.index(33))
print(tup.count(87))