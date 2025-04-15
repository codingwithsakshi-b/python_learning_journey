# 1. Countdown Party 🎉
# Write a recursive function that prints a countdown from a given number down to 1,
# and then prints "🎉 Happy Party Time! 🎉"
# 📚 Concept: Basic recursion with a base case (n == 0) and reducing the problem (n-1)

def print_party():
    print("🎉 Happy party Time! 🎉")

def countdown(n):
    if n == 0:
        return
    print(f"⏳ {n}")
    countdown(n - 1)

countdown(10)
print_party()

# 2. String Reverser 3000 🔁
# Write a recursive function that takes a string and returns it reversed.
# 📚 Concept: Break the string down and build it up from the last character.

def reverse_string(s):
    if len(s) == 0:
        return ""
    else:
        return s[-1] + reverse_string(s[:-1])

print(f"🔁 Reversed: {reverse_string('Sakshi')}")

# 3. Sum of Digits ➕🔢
# Write a function that takes a number and recursively sums its digits until it’s a single digit.
# 📚 Concept: Use recursion to reduce a number to the sum of its digits,
# and keep going until it becomes a single digit (base case: n < 10)
def sum_digits(n):
    if n < 10:
        return n
    else:
        digit_sum = sum(int(digit) for digit in str(n))
        print(f"➕ Intermediate Sum: {digit_sum}")
        return sum_digits(digit_sum)

print(f"🧮 Final Single Digit: {sum_digits(123)}")

# 4. Factorial but Fancy ✨
# Write a recursive function that returns the factorial of a number and prints the process.
# 📚 Concept: Classic factorial recursion — multiply n by factorial(n-1)
# Base case is when n == 0 or 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(f"⚡ Factorial of 5 is: {factorial(5)}")

# 5. Palindrome Checker 🔁✅
# Write a recursive function that checks whether a given string is a palindrome.
# 📚 Concept: Compare first and last characters; if they match, recurse on the inner substring

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])

print(f"🪞 'madam' is palindrome? {is_palindrome('madam')}")
print(f"🪞 'python' is palindrome? {is_palindrome('python')}")

# 🧠💬 Programming Quote of the Day:
print("\n💡 \"Programs must be written for people to read, and only incidentally for machines to execute.\" – Harold Abelson")