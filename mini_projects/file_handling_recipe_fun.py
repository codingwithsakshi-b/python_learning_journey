# 🧁 Creating and reading a secret recipe book

# Writing dessert names to file
with open("recipes.txt", "w") as f:
    f.write("Cake\n")
    f.write("Ice Cream\n")
    f.write("Sushi\n")

# Reading all lines from the file
with open("recipes.txt", "r") as f:
    lines = f.readlines()

# Printing each line with 🍨 flair
for i, line in enumerate(lines, start=1):
    print(f"Recipe {i}: {line.strip()}")

# 🧂 Replacing 'salt' with 'sugar' in recipes.txt

# Step 1: Add some data with 'salt' to simulate the mistake
with open("recipes.txt", "w") as f:
    f.write("cake\nice cream\nsushi\nsalted caramel\nsalt lassi")

# Step 2: Read original content
with open("recipes.txt", "r") as f:
    data = f.read()

# Step 3: Replace 'salt' with 'sugar'
new_data = data.replace("salt", "sugar")

# Step 4: Write the updated content back to the file
with open("recipes.txt", "w") as f:
    f.write(new_data)

# Step 5: Print the final content
print("\n-------------\n")
print("\n🧁 Updated Recipes:\n")
print(new_data)
print("\n----------------\n")

# 🧑‍🍳 Find My Favorite Dish

fav_dish = input("Enter your fav dish: ")

# Open the file and read line by line
with open("recipes.txt", "r") as f:
    dishes = f.readlines()

# Check if the favorite dish exists
found = False
for dish in dishes:
    if fav_dish.lower() in dish.lower():  # Case insensitive search
        found = True
        break

# Print appropriate message
if found:
    print("🎉 Dish found!")
else:
    print("❌ Dish not found")

print("\n-----------------\n")

# 🎩 Line Detective - Find the Line Number of Your Favorite Dish

fav_dish = input("🔍 Enter your favorite dish: ")

# Open the file and read line by line
with open("recipes.txt", "r") as f:
    dishes = f.readlines()

# Searching for the dish in the file
found = False
for line_number, dish in enumerate(dishes, start=1):
    if fav_dish.lower() in dish.lower():  # Case-insensitive search
        found = True
        break

# Output the result creatively
if found:
    print(f"🎉 Hooray! '{fav_dish}' found on line {line_number}. 🍰 Time for a feast!")
else:
    print(f"❌ Oh no! '{fav_dish}' not found in any line. Try a new recipe! 🍳")

print("\n----------------\n")

#🍛 Warm-Up 5: Count the Even Ingredients

count = 0
with open("num.txt", "r") as f:
    data = f.read()

nums = data.split(",")
for val in nums:
    if int(val) % 2 == 0:
        count += 1    

print(f"🔢 Count complete! You've got {count} even ingredients in your data. 🧂🧄🥒  Perfect for a balanced recipe, Chef Sakshi! 👩‍🍳✨")
print("\n-----------------------\n")