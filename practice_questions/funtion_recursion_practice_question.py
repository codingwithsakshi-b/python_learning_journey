cities = ["Jaipur", "Patna", "Mumbai"]
nums = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#WAF to print the length of list. (list is a paracmeter)
def len_list(p):
    print(f"🔖🧾LENGTH OF YOUR LIST IS {len(p)}")

#WAF to print the elements of a list in a single line. (list is the parameter.)
 
def el_list(p):
    print("ELEMENTS IN YOUR LIST ARE: ")
    for el in p:
        print(el, end = " ")

#WAF to find the factorial of n. (n is the parameter.)

def print_fac(n):
    fac = 1
    for val in range(1, n+1):
        fac *= val
    print(f"FACTORIAL! OF {n} 🟰  {fac}")

#WAF to covert USD TO INR

def chng_currency(usd_val):
    print("1 dollar = 86 rupees ,")
    rupee = usd_val*86
    print(f"{usd_val}$🤑 = {rupee} 💵 RUPEES/ONLY®️")

#WAF for even number gives output even and odd number give output odd
def even_odd(n):
    if n%2 == 0:
        print("NUMBER IS A EVEN NUMBER.")
    else:
        print("NUMBER IS A ODD NUMBER.")

# Write a recursive function to calculate the sum of first n natural number.
def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1) #call function ; print(sum(n))
    
# Write a recursive function to print all elements in a list
def char_list(l, idx = 0):
    if idx == len(l):
        return 
    print(l[idx])
    char_list(l, idx+1)



    