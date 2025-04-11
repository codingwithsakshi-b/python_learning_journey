# 🎓 Welcome to Sakshi’s Student Info System 📘
# 💡 Created with love by Sakshi | Polished by Aryan ✨

my_dict = {}

print("🎓 Welcome to Sakshi’s Student Info System 📘")

# 🔹 Input section
name = input("\n📝 Enter Your Name: ").capitalize()
age = int(input("📝 Enter Your Age: "))
course = input("📝 Enter Your Course: ").upper()

# 👩‍🎓 Store initial data
print("\n👩‍🎓 Original Data:")
new_dict = {
    "Name": name,
    "Age": age,
    "Course": course
}
my_dict.update(new_dict)
print(my_dict)

# ➕ Add university info
your_univ = input("\n🏫 Enter your University: ").upper()
my_dict.update({"University": your_univ})
print(f"\n➕ Adding University = {your_univ}")

# ❌ Remove course info
my_dict.pop("Course")
print("❌ Removing 'Course' key...")

# 📦 Final output
print("\n📦 Final Student Record:")
print(my_dict)

# 🔍 Show keys & values separately
key = my_dict.keys()
print(f"\n🗂️ Keys: {key}")
value = my_dict.values()
print(f"📄 Values: {value}")

# 🎉 Closing
print("\n✨ Thank you for using Sakshi’s Smart Dictionary Tool!")
print("💻 Created by Sakshi.")
