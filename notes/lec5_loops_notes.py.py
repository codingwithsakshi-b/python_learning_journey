#LOOPS in python

#1.while loop
 
count = 1
while count <= 5 :
    print("hello")
    count += 1    #print("hello") this will print infinite
print(count) #ans should be 5

i = 1
while i <= 100:
    print("sakshi",i)
    i+=1

#we want to print some numbers 

y = 1
while y <= 100:
    print(y)
    y+=1
print("Loop Ended")

#we can reverse our loop

z = 100
while z >= 1:
    print(z)
    z-=1
print("loop ends") #prefer do not create infinite loops its dangereous and doesn't prefer in real life programming

#break keyword
i = 1
while i <= 5:
    print(i)
    if(i == 3):
        break
    i += 1
print("end of loop")

#continue keyword

t = 0 
while t <= 5:
    if(t == 3):
        t += 1
        continue
    print(t)
    t += 1

#FOR loops

nums = ["rah",1, 2, 3, "tum"]
for val in nums:
    print(val)

veggies = ["potato", "ladyfinger", "tomato"]
for el in veggies:
    print(el)
else:
    print("END") #for specific resons when we use break

str = "sakshicoder"

for char in str:
    if(char == 'o'):
        print("o found")
        break
    print(char)
else:
    print("end")


#range

print(range(5))

set = range(10)

for a in set: #for a in range(10)
    print(a)

for a in range(2, 10):
    print(a)

print("wait")

for a in range(2, 10, 3):
    print(a)
     
#pass statements

for el in range(10):#for avoiding error
    pass
if i>5:
    pass
print("some useful work")