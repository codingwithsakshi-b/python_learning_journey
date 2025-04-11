# 🎯 Sakshi's Smart Number Checker 🔢
# ➕ With Input Validation, Timestamp & Re-run Feature

from datetime import datetime  # 💡Extra features (timestamp added with suggestions from my AI dost Aryan 😊

while True:
    print("\n🎯 Number Analyzer 🔢")
    
    # 🟩 Safe Input
    try:
        num = int(input("\n📥 Enter a number: "))
    except ValueError:
        print("❌ Invalid input! Please enter a valid integer.")
        continue

    # 🕒 Timestamp (Aryan suggestion)
    print(f"\n🕒 Checked on: {datetime.now().strftime('%d-%b-%Y %I:%M %p')}")
    
    # 📌 Input Confirmation
    print(f"\n➡️ You entered: {num}")

    # 🧪 Even or Odd Check 
    print("\n🧪 Even or Odd Check:")
    if num % 2 == 0:
        print("🔹 It is an **even** number.")
    else:
        print("🔹 It is an **odd** number.")

    # 📊 Divisibility Test 
    print("\n📊 Divisibility Test:")
    if num % 3 == 0 and num % 5 == 0:
        print("✅ The number is divisible by **both 3 and 5**")
    elif num % 3 == 0:
        print("✅ The number is divisible by 3.")
    elif num % 5 == 0:
        print("✅ The number is divisible by 5.")
    else:
        print("❌ The number is not divisible by either 3 or 5.")

    # 🔁 Run Again Prompt
    again = input("\n🔁 Do you want to check another number? (yes/no): ").strip().lower()
    if again != "yes":
        print("\n👋 Exiting Sakshi's Smart Checker. Thank you & Happy Coding! 💖")
        break
# 💻 Project by Sakshi — with love, logic & a little help from her AI friend Aryan 😊

# 🌸 Every line I write, takes me one step closer to becoming the coder I dream to be 🌈

# 🔚 End of program... but the journey just began 💖

# 🚀 More to come, more to build... One project at a time 💫

# 👑 Coded by Sakshi • Polished by Aryan • Powered by Chai & Dreams ☕✨

