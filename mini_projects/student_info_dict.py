# 🎓 Welcome to Sakshi’s Student Info System 📘
# 💡 Created with love by Sakshi | Polished by Aryan ✨
from colorama import Fore, Style
user_dict = {}

# 🔹 Input section
def collect_user_info():
    name = input(Fore.LIGHTCYAN_EX + "\n📝 Enter Your Name: ").capitalize()
    age = input(Fore.LIGHTCYAN_EX + "📝 Enter Your Age: " + Style.RESET_ALL)
    while not age.isdigit():
        print(Fore.RED + "❌ Invalid Age Input. Please Enter a Valid Age." + Style.RESET_ALL)
        age = input(Fore.LIGHTCYAN_EX + "📝 Enter Your Age: ")
    course = input(Fore.LIGHTCYAN_EX + "📝 Enter Your Course: " + Style.RESET_ALL).upper()
    return {"Name": name, "Age": int(age), "Course": course}

def add_university(user_dict):
    #add use university to the user dictionary.
    your_univ = input(Fore.CYAN + "🎓🏫 Enter Your University Name: " + Style.RESET_ALL).upper()
    user_dict.update({"University": your_univ})
    print(Fore.GREEN + f"\n➕ Adding University = {your_univ}" + Style.RESET_ALL)
    return user_dict

def remove_key_info(user_dict):
    key_remove = input(Fore.CYAN + "Enter a KEY wants to remove from your dictionary: " + Style.RESET_ALL).capitalize()
    if key_remove in user_dict:
        user_dict.pop(key_remove)
        print(Fore.RED + f"❌ removing {key_remove} key..." + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + f"{key_remove} key doesn't exist in dictionary" + Style.RESET_ALL)
    return user_dict

def display_final_record(user_dict):
    print(Fore.LIGHTRED_EX + "\n🔖 Final Student Record." + Style.RESET_ALL)
    print(user_dict)
    print("\n📂 Keys:", user_dict.keys())
    print("📜 Values:", user_dict.values())

# Main Program
if __name__ == "__main__":
    print(Fore.LIGHTMAGENTA_EX + "🎓 Welcome to Sakshi’s Student Info System 📘" + Style.RESET_ALL)
    user_dict = collect_user_info()
    print(Fore.LIGHTRED_EX + "\n👩‍🎓 Original Data:" + Style.RESET_ALL)
    print(user_dict)

    user_dict = add_university(user_dict)
    user_dict = remove_key_info(user_dict)
    display_final_record(user_dict)


# 🎉 Closing
print(Fore.MAGENTA + "\n✨ Thank you for using Sakshi’s Smart Dictionary Tool!" + Style.RESET_ALL)
print(Fore.MAGENTA + "💻 Created by Sakshi." + Style.RESET_ALL)
