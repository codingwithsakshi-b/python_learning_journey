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



