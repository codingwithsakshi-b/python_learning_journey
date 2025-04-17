# Importing necessary module
import time
from datetime import datetime

# Get the current time in HH:MM:SS format
timestamp = time.strftime('%H:%M:%S')
print(f"⏰ Current Time: {timestamp}")

# Convert the current time into a datetime object for accurate comparison
current_time = datetime.strptime(timestamp, '%H:%M:%S')

# Define time ranges for greetings
morning_start = datetime.strptime('05:00:00', '%H:%M:%S')
noon = datetime.strptime('12:00:00', '%H:%M:%S')
afternoon_end = datetime.strptime('16:00:00', '%H:%M:%S')
evening_end = datetime.strptime('19:00:00', '%H:%M:%S')

# Greet the user based on current time
if morning_start <= current_time <= noon:
    print("🌄 GOOD MORNING SIR!")
elif noon < current_time <= afternoon_end:
    print("🕑 GOOD AFTERNOON SIR!")
elif afternoon_end < current_time <= evening_end:
    print("🌆 GOOD EVENING SIR!")
else:
    print("🌃 GOOD NIGHT SIR!")

# 📝 Points to Note:
# - Using datetime objects for accurate time comparisons.
# - Emojis make the interaction more engaging.
# - Proper structure and comments help in readability and future modifications.
