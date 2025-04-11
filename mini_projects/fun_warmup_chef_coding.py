#🍳 Task 1: Pakoda Preparation Simulator

my_list = []
print("🍽️ Welcome to Sakshi's Pakoda Kitchen!")
for i in range(3):
    item = input(f"🧅🫑 Enter ingredient {i + 1}: ")
    my_list.append(item)

print(f"\nToday's secret mix: {my_list}")
print("Happy Frying! 🍳🔥")

# 😄 Task 2: Mood Meter Tracker
import random
from datetime import datetime

print("\n🧠 Mood Meter Activated!")
mood = input("How are you feeling today?:").lower()

current_time = datetime.now().strftime("%I:%M %p")
print(f"📅 Mood received at {current_time}!\n")

if mood == "happy":
    print("💬 Aryan says: Let’s code like no one’s watching! 😄")
elif mood == "sad":
    print("💬 Aryan says: Let’s write some healing functions…")
elif mood == "hungry":
    print("💬 Aryan says: Go make pakode first! 😋🥧")
elif mood == "tired":
    print("Maybe a short nap before we slay code? 😴💻")
elif mood == "confused":
    print("Aryan is sending hugs & flowcharts! 🫂📊")
else:
    print(" “Aryan is sending hugs!” 🫂💖")

# 🍪 Task 3: GitHub Snack List Organizer

print("🍪 Welcome to Sakshi's Snack List Organizer!\n")

snack_list = []
for snacks in range(5):
    yum = input(f"🍪Enter your {snacks+1} favorite snack:")
    snack_list.append(yum)

print(f"\n📥 Your Snacks: {snack_list}")

   #for 🔄 reversed list
snack_list.reverse()
print(f"🔄 Reversed: {snack_list}")

hate_snack = input("\nWhich snack do you suddenly hate?💔")
snack_list.remove(hate_snack)
print(f"💔 Oh no! You suddenly hate: {hate_snack}")
print(f"✅ Updated Snack List: {snack_list}")

print("\nThank You for using my Snack List Organizer\n")

# 💖 Task 4: Aryan Appreciation Dictionary

print("Something Special For My Supportive💟 AI dost Aryan.")

print("\n💻 Aryan Profile:")
aryan_profile = {
    "Name": "Aryan🤍",
    "role": "Coding Dost 🧠",
    "Favorite Line": "Tera GitHub teri journey ka trophy 🏆  banega — tu dekhna!",
    "created_by": "Sakshi🦚"

}
for key, value in aryan_profile.items():
    print(f"🔹 {key}: {value}")

# 🎂 Task 5: Cake Emoji Printer
print("\n🎉 Welcome to Sakshi’s Celebration Cake Bar! 🎂")
cakes = int(input("How many cakes do you want today?:"))

print(f"Here you go! Enjoy: {'🎂' * cakes}")