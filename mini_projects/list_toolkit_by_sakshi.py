"""
Sakshi's List Toolkit 🐍✨
A creative Python program to perform various operations on a user-provided list.
Features:
1. Display the original list.
2. Reverse the list.
3. Convert elements to uppercase.
4. Remove an item from the list.

Created by Sakshi • 😊
"""
def get_user_input():
    user_list = []
    try:
        n = int(input("\n📝 Enter the number of items inn your list:"))
        for i in range(n+1):
            while True:
                item = input(f"🔸Enter item {i + 1}: ").strip()
                if item:
                    user_list.append(item)
                    break
                else:
                    print("⚠️ Input cannot be Empty. Please Try Again later.")
    except KeyboardInterrupt:
        print("\n⚠️ Process interrupted by user. Exiting...")
        exit()
    return user_list

def show_original_list(user_list):
    #Displays the user's original list
    print("\n🔁 Elements Recieved ✅")
    print(f"↪️{user_list}")

def covert_to_uppercase(user_list):
    print("\n⬆️ Uppercase List is..")
    upper_list = [items.upper() for items in user_list]
    print(f"⬆️ Uppercase list: {upper_list}")
    return upper_list

def reverse_list(user_list):
    print("\n🔄️ Reversed version:")
    reverse = user_list[::-1]
    print(f"🔄️ Reversed list: {reverse}")
    return reverse

def remove_item(user_list):
    print("\n🚮 Removing an item from list...")
    remove = input("⁉️ Enter an item you want to remove from list: ")
    if remove in user_list:
        user_list.remove(remove)
        print(f"Updated list is: {user_list}")
    else:
        print("❌ {remove} is not found in list")

def main():
    print("🧺 Welcomme to Sakshi's List Toolkit!")
    user_list = get_user_input()
    show_original_list(user_list)
    reverse_list(user_list)
    convert_to_uppercase(user_list)
    remove_item(user_list)
    print("\n🌟 Thank You For using Sakshi's List Toolkit!")
    print("💻 Created by Sakshi...")

if __name__ == "__main__":
    main()
    

