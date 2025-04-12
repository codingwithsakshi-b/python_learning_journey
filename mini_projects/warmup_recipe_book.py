# 🧁 Creating and Reading Sakshi's Secret Recipe Book 👩‍🍳✨

# 🎀 Step 1: Write Initial Dessert Names
with open("recipes.txt", "w") as f:
    f.write("Cake\n")
    f.write("Ice Cream\n")
    f.write("Sushi\n")

# 🎀 Step 2: Read & Display Each Dessert Line
with open("recipes.txt", "r") as f:
    lines = f.readlines()

print("📚 Current Recipes:")
for i, line in enumerate(lines, start=1):
    print(f"🍨 Recipe {i}: {line.strip()}")

# 🎯 Step 3: Simulate Mistake – Add 'salt' lines
with open("recipes.txt", "w") as f:
    f.write("cake\nice cream\nsushi\nsalted caramel\nsalt lassi")

# 🎯 Step 4: Read Data
with open("recipes.txt", "r") as f:
    data = f.read()

# 🎯 Step 5: Replace 'salt' with 'sugar'
new_data = data.replace("salt", "sugar")

# 🎯 Step 6: Update the file
with open("recipes.txt", "w") as f:
    f.write(new_data)

# 🎯 Step 7: Show Final Recipes
print("\n🧁 Updated Recipes:\n------------------")
print(new_data)
print("------------------\n")

# 🍽️ Step 8: Search for Favorite Dish
fav_dish = input("🔎 Enter your fav dish: ")

with open("recipes.txt", "r") as f:
    dishes = f.readlines()

found = any(fav_dish.lower() in dish.lower() for dish in dishes)

if found:
    print("🎉 Dish found in your recipe book!")
else:
    print("❌ Sorry! Dish not found.")

print("\n-----------------\n")

# 🔍 Step 9: Find Line Number of Favorite Dish
fav_dish = input("📌 Enter your favorite dish again (for line number): ")

found = False
for line_number, dish in enumerate(dishes, start=1):
    if fav_dish.lower() in dish.lower():
        found = True
        break

if found:
    print(f"🎉 Hooray! '{fav_dish}' found on line {line_number}. 🍰 Time for a feast!")
else:
    print(f"❌ Oh no! '{fav_dish}' not found. Try a new recipe! 🍳")

print("\n----------------\n")

# 🍛 Step 10: Count Even Ingredients (from num.txt)
count = 0
with open("num.txt", "r") as f:
    data = f.read()

nums = data.split(",")
for val in nums:
    if int(val.strip()) % 2 == 0:
        count += 1    

print(f"🔢 Count complete! You've got {count} even ingredients 🧂🧄🥒 — Perfect for a balanced recipe, Chef Sakshi! 👩‍🍳✨")
print("\n-----------------------\n")
