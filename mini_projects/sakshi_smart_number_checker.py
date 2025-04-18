# 🎯 Sakshi's Smart Number Checker 🔢
# ➕ With Input Validation, Timestamp & Re-run Feature

from datetime import datetime

def safe_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("❌ Invalid Input. Please Enter a valid input..")

def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is a 🔢 Even Number.")
    else:
        print(f"{num} is a 🔢 Odd Number.")

def divisibility_test(num):
    if num % 3 == 0 and num % 5 == 0:
        return "🔶 Number is Divisible by both 3 and 5."
    elif num % 3 == 0:
        return "🔶 Number is Divisible by 3."
    elif num % 5 == 0:
        return "🔶 Number is Divisible by 5."
    else:
        return "❌ Number is Not divisible by Either 3 or 5."

def main():
    while True:
        print("\n✨ Number Analyzer 🔢.")

        num = safe_input("\n📜 Enter a number:")
        print(f"\nChecked on: {datetime.now().strftime('%d-%b-%Y  %I:%M:%p')}")
        print(f"\n👉 You Entered: {num}")

        print("\n✨ Even Odd check:")
        check_even_odd(num)

        print("\n✅ Divisibility Test from 3️⃣ and 5️⃣.")
        print(divisibility_test(num))

        again = input("\n🔁 Do You Want to Check Another Number? (yes/no): ").strip().lower()
        if again != "yes":
            print("\n👋 Exiting Sakshi's Smart Number Checker.💖 Thank You For Using it. \n©️ HAPPY CODING...")

if __name__ == "__main__":
    main()



# 💻 Project by Sakshi — with love, logic & a little help from her AI friend Aryan 😊

# 🌸 Every line I write, takes me one step closer to becoming the coder I dream to be 🌈

# 🔚 End of program... but the journey just began 💖

# 🚀 More to come, more to build... One project at a time 💫

# 👑 Coded by Sakshi • Powered by Chai & Dreams ☕✨

