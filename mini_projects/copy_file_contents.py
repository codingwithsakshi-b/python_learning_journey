# 🌟 Mini Project: File Content Copier by Sakshi 🌟
# 🔄 This script copies content from one file to another
# 📁 Source file: data.txt (or any file you choose)
# 📁 Destination file: copy.txt (or any file you choose)
import os
import shutil
from tqdm import tqdm #pip install tqdm
from termcolor import colored #pip install termcolor
from colorama import Fore, Style

print(Fore.MAGENTA + "👋 Welcome to Sakshi's File Copy Content Function 🎉🎉" + Style.RESET_ALL)

source_file = input(Fore.LIGHTYELLOW_EX + "\nEnter a Source file you Want to copy(.txt):")
destination_file = input(Fore.LIGHTYELLOW_EX + "\nEnter a Destination file you want to create(.txt):" + Style.RESET_ALL)

if not source_file.endswith('.txt') or not destination_file.endswith('.txt'):
    print(Fore.RED + "❌ Only .txt Files are supported." + Style.RESET_ALL)
    exit()

def copy_file_contents(source_file, destination_file):
    """
    📌 Copies content from 'source_file' to 'destination_file'
    🧠 Includes error handling for:
        ❌ Missing source file
        ⚠️ Unexpected exceptions
    """
    if os.path.exists(destination_file):
        backup_file = destination_file + ".bak"
        shutil.copy(destination_file, backup_file)
        print(Fore.LIGHTGREEN_EX + f"⚠️ Backup created: {backup_file}" + Style.RESET_ALL)

    try:
        with open(source_file, "rb") as source, open(destination_file, "wb") as dest:
            for chunk in tqdm(source, desc="Copying" , unit="B" , unit_scale=True):
                dest.write(chunk)
      
        print(colored("\n✅ Content copied successfully! 🎉💫","green"))

    except FileNotFoundError:
        print(colored("❌ Source File not Found! Make sure the file exists.","red"))
    except Exception as e:
        print(colored(f"⚠️ Unexpected Error: {e}","red"))
    
    print(Fore.LIGHTBLUE_EX + "\n🙏 Thank you for using this Tool 😌💫" + Style.RESET_ALL)

# 🚀 Function call with sample file names
copy_file_contents(source_file, destination_file)

if input(Fore.LIGHTYELLOW_EX + "\nDo You want to undo the last operation? (yes/no): " + Style.RESET_ALL).lower() == "yes":
    backup_file = destination_file + ".bak"
    if os.path.exists(backup_file):
        shutil.copy(backup_file, destination_file)
        print(colored("✅ Undo completed!","green"))
    else:
        print(colored("❌ No Backup found to undo","red"))
    

