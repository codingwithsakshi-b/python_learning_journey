# 🧺 Sakshi’s List Toolkit 🐍✨
# ➕ A creative list program designed by Sakshi & polished by AI dost Aryan 😊

# 🔽 Step 0: Input 5 elements from the user
my_list = []
print("🧺 Welcome to Sakshi’s List Toolkit 🐍✨")

for i in range(5):
    item = input(f"🔸 Enter item {i + 1}: ")
    my_list.append(item)

# ✅ Step 1: Show original list
print("\n🔹 Step 1: Elements Received ✅")
print(f"📥 Your List: {my_list}")

# 🔄 Step 2: Reversed list
print("\n🔄 Step 2: Reversed List")
print(f"↪️ {my_list[::-1]}")

# 🔠 Step 3: Uppercase version of list
print("\n🔠 Step 3: Uppercase Version")
upper_list = [item.upper() for item in my_list]
print(f"🔊 Uppercase List: {upper_list}")

# 🗑️ Step 4: Remove an item
print("\n🗑️ Step 4: Remove an Item")
remove = input("❓ Enter the item you want to remove: ")

# 🔁 Check if item exists before removing (this para is suggested by Aryan.)
if remove in my_list:
    my_list.remove(remove)
    print(f"✅ Updated List: {my_list}")
else:
    print(f"⚠️ '{remove}' not found in the list.")

# 🌟 Closing
print("\n✨ Thank you for using Sakshi's List Toolkit!")
print("💻 Created by Sakshi • Polished by Aryan 😊")
