# Importing necessary module
import time
from colorama import Fore, Style # For colored text in terminal #pip install colorama
from datetime import datetime

# Get the current time in HH:MM:SS format
timestamp = time.strftime('%H:%M:%S')
print(Fore.LIGHTCYAN_EX + f"⏰ Current Time: {timestamp}" + Style.RESET_ALL)

# Convert the current time into a datetime object for accurate comparison
current_time = datetime.strptime(timestamp, '%H:%M:%S')

# Define time ranges for greetings
morning_start = datetime.strptime('05:00:00', '%H:%M:%S')
noon = datetime.strptime('12:00:00', '%H:%M:%S')
afternoon_end = datetime.strptime('16:00:00', '%H:%M:%S')
evening_end = datetime.strptime('19:00:00', '%H:%M:%S')

# Greet the user based on current time
if morning_start <= current_time <= noon:
    print(Fore.LIGHTYELLOW_EX + "🌄 GOOD MORNING SIR!" + Style.RESET_ALL)
elif noon < current_time <= afternoon_end:
    print(Fore.LIGHTGREEN_EX + "🕑 GOOD AFTERNOON SIR!" + Style.RESET_ALL) 
elif afternoon_end < current_time <= evening_end:
    print(Fore.LIGHTRED_EX + "🌆 GOOD EVENING SIR!" + Style.RESET_ALL)
else:
    print(Fore.LIGHTMAGENTA_EX + "🌃 GOOD NIGHT SIR!" + Style.RESET_ALL)

# 📝 Points to Note:
# - Using datetime objects for accurate time comparisons.
# - Emojis make the interaction more engaging.
# - Proper structure and comments help in readability and future modifications.
