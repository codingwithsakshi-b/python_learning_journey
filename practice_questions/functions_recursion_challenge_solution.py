# 📄 Sakshi's Functions & Recursion Challenge Solutions
# 💡 Created by Sakshi | Lightly Polished by Aryan 💅

# ✅ Q1: Prime Number Checker
# 🧠 Returns True if n is prime, else False
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# 🔍 Test
print(is_prime(8))        # False
print(is_prime(104729))   # True


# ✅ Q2: Factorial Using Recursion
# 🧠 Returns the factorial of a number using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 🔍 Test
print(factorial(5))   # 120
print(factorial(1))   # 1
print(factorial(0))   # 1


# ✅ Q3: Greet Function with Default Argument
# 🧠 Greets a user, defaults to "Guest" if no name is provided
def greet(name="Guest"):
    print(f"👋 Hello {name}! Welcome to Python Cafe ☕🍵.")

# 🔍 Test
greet("Sakshi")
greet()
greet("Aryan")
greet("Keshav")


# ✅ Q4: Calculator Function with Operator
# 🧠 Performs basic arithmetic operations (+, -, *, /)
def calculator(operator, a=1, b=1):
    print(f"\n📌 Operation: {operator} | a = {a}, b = {b}")
    
    if operator == "+":
        print(f"✅ Sum ➕ of numbers is: {a + b}")
    
    elif operator == "-":
        print(f"✅ Difference ➖ of numbers is: {a - b}")
    
    elif operator == "*":
        print(f"✅ Product ✖️ of numbers is: {a * b}")
    
    elif operator == "/":
        if b == 0:
            print("⚠️ Cannot divide by 0. Please try again with b ≠ 0.")
        else:
            print(f"✅ Division ➗ of numbers is: {a / b}")
    
    else:
        print("❌ Invalid Operator! Please use +, -, *, or /")

# 🔍 Test
calculator("-", 7, 8)
calculator("/", 8, 0)
calculator("y", 9, 8)
calculator("+")


# ✅ Q5: Count Vowels in a String
# 🧠 Counts and prints total vowels in the input string
def count_vowel(s):
    count = 0
    for el in s.lower():
        if el in "aeiou":
            count += 1
    print(f"\n🌟💫 Total Vowel characters in your string: {count}")

# 🔍 Test
count_vowel("Sakshi and Aryan are Coding Buddies!")


# ✅ Q6: Recursive Countdown
# 🧠 Prints numbers from n down to 1 using recursion
def print_blastoff():
    print("🚀🚀 Blast offff!!!!!...")

def print_reverse(n=1):
    if n == 0:
        return
    print(n)
    print_reverse(n - 1)

# 🔍 Test
print_reverse(10)
print_blastoff()
