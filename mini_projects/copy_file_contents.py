# 🌟 Mini Project: File Content Copier by Sakshi 🌟
# 🔄 This script copies content from one file to another
# 📁 Source file: data.txt (or any file you choose)
# 📁 Destination file: copy.txt (or any file you choose)
import os
import shutil
from tqdm import tqdm
from termcolor import colored

print("👋 Welcome to Sakshi's File Copy Content Function 🎉🎉")

source_file = input("\nEnter a Source file you Want to copy(.txt):")
destination_file = input("\nEnter a Destination file you want to create(.txt):")

if not source_file.endswith('.txt') or not destination_file.endswith('.txt'):
    print("❌ Only .txt Files are supported.")
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
        print(f"⚠️ Backup created: {backup_file}")

    try:
        with open(source_file, "rb") as source, open(destination_file, "wb") as dest:
            for chunk in tqdm(source, desc="Copying" , unit="B" , unit_scale=True):
                dest.write(chunk)
      
        print(colored("\n✅ Content copied successfully! 🎉💫","green"))

    except FileNotFoundError:
        print(colored("❌ Source File not Found! Make sure the file exists.","red"))
    except Exception as e:
        print(colored(f"⚠️ Unexpected Error: {e}","red"))
    
    print("\n🙏 Thank you for using this Tool 😌💫")

# 🚀 Function call with sample file names
copy_file_contents("data.txt", "copy.txt")

if input("\nDo You want to undo the last operation? (yes/no): ").lower() == "yes":
    backup_file = destination_file + ".bak"
    if os.path.exists(backup_file):
        shutil.copy(backup_file, destination_file)
        print(colored("✅ Undo completed!","green"))
    else:
        print(colored("❌ No Backup found to undo","red"))
    

