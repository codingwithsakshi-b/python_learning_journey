# 🎓 Welcome to Sakshi’s Student Info System 📘
# 💡 Created with love by Sakshi | Polished by Aryan ✨

user_dict = {}

print("🎓 Welcome to Sakshi’s Student Info System 📘")

# 🔹 Input section
def collect_user_info():
    name = input("\n📝 Enter Your Name: ").capitalize()
    age = input("📝 Enter Your Age: ")
    while not age.isdigit():
        print("❌ Invalid Age Input. Please Enter a Valid Age.")
        age = input("📝 Enter Your Age: ")
    course = input("📝 Enter Your Course: ").upper()
    return{"Name": name, "Age": int(age), "Course": course}

def add_university(user_dict):
    #add use university to the user dictionary.
    your_univ = input("🎓🏫 Enter Your University Name: ")
    user_dict.update("University": your_univ)
    print(f\n➕ Adding University = {your_univ}")
    return user_dict

def remove_key_info(user_dict):
    key_remove = input("Enter a KEY wants to remove from your dictionary: ")
    if key_remove in user_dict:
        user_dict.pop(key_remove)
        print(f"❌ removing {key_remove} key...")
    else:
        print(f"{key_remove} key doesn't exist in dictionary")
    return user_dict

def display_final_record(user_dict):
    print("\n🔖 Final Student Record.")
    print(user_dict)
    print("\n📂 Keys:", user_dict.keys())
    print("📜 Values:", user_dict.values())

# Main Program
if __name__ == "__main__":
    print("🎓 Welcome to Sakshi’s Student Info System 📘")
    user_dict = collect_user_info()
    print("\n👩‍🎓 Original Data:")
    print(user_dict)

    user_dict = add_university_info(user_dict)
    user_dict = remove_course_info(user_dict)
    display_final_record(user_dict)


# 🎉 Closing
print("\n✨ Thank you for using Sakshi’s Smart Dictionary Tool!")
print("💻 Created by Sakshi.")
