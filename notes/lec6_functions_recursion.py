#FUNCTIONS IN PYTHON
#function defination
def calc_sum(a, b): #parameters
    sum = a + b
    print(f"➕ sum of {a} and {b} is {sum}.")
    return sum 

calc_sum(2, 3) #fumction call. 2,3 are arguments. return value 2+3
calc_sum(12, 45)
calc_sum(33, 56) #for remove reduntancy (small readable codes.)

#we want to print hello 
def print_hello(): #bina argument wala func.
    print("hello") 

print_hello() #function call
output = print_hello() #return value nahi h 
print(output) #None value ayega

#we have to calc avg pf any three numbers p,q,r
def calc_avg(p, q, r):
    sum = p + q + r
    avg = sum/3
    print(f"🚀AVERAGE OF {p},{q},{r} 🟰  {avg}")
    return avg

calc_avg(1,2,3) # ans is 2.0 , called function call.

#built inn function
print("JECRC University","sakshi") #sep = " "
    #agr multiple line ko  ek sath print karwana chahte hai toh
print("sakshi and",end=" ") #end = "\n"
print("keshav")
#len(),type(),range()

#USER DEFINED FUNCTION
#wo function jo hum built krte hai apne code me 

#default parameter
  #means pehle se koi value set kar dena agr apne argument me kuch nahi likha toh

def calc_prod(a=1 , b=1):
    prod = a*b
    print(f"PRODUCT ✖️ OF NUMS IS 🟰  {prod}")

calc_prod() #we dont put args by default it takes a=1 and b=1
calc_prod(4,5) #20

#RECURSION(WHEN A FUNCTION CALLS ITSELF REPEATEDLY.)
#call stack
def show(n): #recursive function
    if n == 0:
        return # show() khud ko call karega jb tk n = 0
    print(n)
    show(n-1)
    print("END")# it shows how recursion work

show(5)
#n! through recursion.
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return(n * fact(n-1))
    
print(fact(5))