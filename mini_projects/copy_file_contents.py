# 🌟 Mini Project: File Content Copier by Sakshi 🌟
# 🔄 This script copies content from one file to another
# 📁 Source file: data.txt (or any file you choose)
# 📁 Destination file: copy.txt (or any file you choose)

print("👋 Welcome to Sakshi's File Copy Content Function 🎉🎉")

def copy_file_contents(source_file, destination_file):
    """
    📌 Copies content from 'source_file' to 'destination_file'
    🧠 Includes error handling for:
        ❌ Missing source file
        ⚠️ Unexpected exceptions
    """

    try:
        # 📖 Reading from the source file
        with open(source_file, "r") as source:
            data = source.read()

        # ✍️ Writing to the destination file
        with open(destination_file, "w") as dest:
            dest.write(data)

        print("\n✅ Content copied successfully! 🎉💫")

    except FileNotFoundError:
        print("❌ Source File not Found! Make sure the file exists.")
    except Exception as e:
        print(f"⚠️ Unexpected Error: {e}")
    
    print("\n🙏 Thank you for using this Tool 😌💫")

# 🚀 Function call with sample file names
copy_file_contents("data.txt", "copy.txt")

