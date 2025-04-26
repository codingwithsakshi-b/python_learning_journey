from colorama import Style, Fore
from datetime import datetime
import time
import random
import pyfiglet
from termcolor import colored
from fpdf import FPDF

shift = random.randint(1, 10)

def zigzag_encode():
    code = input(Fore.BLUE + "Enter a word or sentence you want to encode: ").strip().lower()
    code = code.replace(" ", "")

    even_chars = [char for index, char in enumerate(code) if index % 2 == 0]
    odd_chars = [char for index, char in enumerate(code) if index % 2 != 0]
    combined = odd_chars + even_chars

    shift = random.randint(1, 10)

    shifted_char = []

    for char in combined:
        if 'a' <= char <= 'z':
            shifted = chr((ord(char) - ord('a') + shift) % 26 + ord('a') )
            shifted_char.append(shifted)

        else:
            shifted_char.append(char)

    encoded_string = ''.join(shifted_char)

    print(Fore.MAGENTA + "⏳ Encoding in Progress..." + Style.BRIGHT)
    time.sleep(1.5)

    print(Fore.GREEN + f"🍁 Encoded String: {encoded_string}" + Style.BRIGHT)
    save_encoding_history(code, encoded_string, shift)

def save_encoding_history(original, encoding, shift):
    time_stamp = datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    with open("encoding_history.txt", "a") as file:
        file.write(f"[{time_stamp}] {original} --> {encoding} of shift: {shift}\n")

def show_encoding_history():
    try:
        with open("encoding_history.txt", "r") as file:
            data = file.read()
            print(Fore.LIGHTYELLOW_EX + "\n👇 Encoded History Loading... " + Style.BRIGHT)
            time.sleep(1.5)
            print(Fore.LIGHTCYAN_EX + data + Style.BRIGHT)

    except FileNotFoundError:
        print(Fore.RED + "⚠️ No encoding history found. Tip: Encode something first!" + Style.BRIGHT)

def zigzag_decode():
    code = input(Fore.YELLOW + "Enter a word or sentence you want to decode: " + Style.BRIGHT).strip().lower()
    try:
        shift = int(input(Fore.LIGHTYELLOW_EX + "Enter that Shift Use during Encoding: "))

        decoded_shifted_string = []

        for char in code:
            if 'a' <= char <= 'z':
                shifted = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                decoded_shifted_string.append(shifted)
            
            else:
                decoded_shifted_string.append(char)

        shifted_string = ''.join(decoded_shifted_string)

        mid = len(shifted_string) // 2

        odd_chars = shifted_string[:mid]
        even_chars = shifted_string[mid:]

        original_chars = []

        for i in range(len(even_chars)):
            if i < len(even_chars):
                original_chars.append(even_chars[i])

            if i < len(odd_chars):
                original_chars.append(odd_chars[i])

        decoded_string = ''.join(original_chars)

        print(Fore.MAGENTA + "⏳ Decoding in Progress..." + Style.BRIGHT)
        time.sleep(1.5)

        print(Fore.GREEN + f"Decoded string is: {decoded_string}" + Style.BRIGHT)

        save_decoding_history(code, decoded_string, shift)

    except Exception as e:
        print(Fore.RED + f"⚠️ Enter A Integer Value: {e}" + Style.BRIGHT)

def save_decoding_history(original, decoding, shift):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("decoding_history.txt", "a") as file:
        file.write(f"[{time_stamp}] {original} --> {decoding} of shift: {shift}\n")

def show_decoding_history():
    try:
        with open("decoding_history.txt", "r") as file:
            data = file.read()

            print(Fore.LIGHTYELLOW_EX + "\n👇 Encoded History Loading... " + Style.BRIGHT)
            time.sleep(1.5)

            print(Fore.LIGHTCYAN_EX + data + Style.BRIGHT)

    except FileNotFoundError:
        print(Fore.RED + "	⚠️ No decoding history found. Tip: Decode something first!" + Style.BRIGHT)

def clear_encoding_history():
    with open("encoding_history.txt", "w") as file:
        file.write("")
    print(Fore.LIGHTRED_EX + "🧹 Clearing encoding history..." + Style.BRIGHT)
    time.sleep(1)
    print(Fore.GREEN + "✔️ Encoding History cleared!" + Style.BRIGHT) 

def clear_decoding_history():
    with open("decoding_history.txt", "w") as file:
        file.write("")
    print(Fore.LIGHTRED_EX + "🧹 Clearing decoding history..." + Style.BRIGHT)
    time.sleep(1)
    print(Fore.GREEN + "✔️ Decoding History cleared!" + Style.BRIGHT) 

def export_data_to_pdf():
    print(Fore.YELLOW + "\n📤 Export Menu (Stylish PDF)")
    print(Fore.CYAN + "1. Export Encoded History to PDF")
    print(Fore.CYAN + "2. Export Decoded History to PDF")

    choice = input(Fore.YELLOW + "👉 Enter Your Choice (1-2): " + Style.BRIGHT)

    if choice == "1":
        filename = "encoded_export.pdf"
        source_file = "encoding_history.txt"
        title = "ZigZag Encoded History"
    elif choice == "2":
        filename = "decoded_export.pdf"
        source_file = "decoding_history.txt"
        title = "ZigZag Decoded History"
    else:
        print(Fore.RED + "⚠️ Invalid choice, please select 1 or 2!" + Style.BRIGHT)
        return

    try:
        with open(source_file, "r") as file:
            data = file.read()

        if not data.strip():
            print(Fore.RED + "⚠️ History is empty. Nothing to export!" + Style.BRIGHT)
            return

        pdf = FPDF()
        pdf.add_page()

        # Title style
        pdf.set_font("Arial", 'B', 20)  # Bold, size 20
        pdf.set_text_color(0, 102, 204)  # Blue color
        pdf.cell(0, 10, txt=title, ln=True, align="C")
        pdf.ln(10)  # Line break after title

        # Body style
        pdf.set_font("Arial", size=12)
        pdf.set_text_color(0, 0, 0)  # Black color

        lines = data.split('\n')
        for line in lines:
            pdf.cell(0, 10, txt=line, ln=True)

        pdf.output(filename)

        print(Fore.GREEN + f"✔️ Stylish history exported successfully to '{filename}'!" + Style.BRIGHT)

    except FileNotFoundError:
        print(Fore.RED + f"⚠️ No history file found ({source_file}) to export!" + Style.BRIGHT)



def exit_program():
    print(Fore.CYAN + "\n♥️  Exiting", end="" )
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="")

    print(Fore.RED + "\n🌟 Thank you for using ZigZag Coder! See you next time. 👋" + Style.BRIGHT)

    banner = pyfiglet.figlet_format("Thank You", font="bubble")  # You can change text here
    color_banner = colored(banner, color="red")
    print(color_banner)
    time_stamps = datetime.now().strftime("%d-%m-%Y  %H:%M:%S")
    print(colored(time_stamps, color="light_green"))


def main():
    banner = pyfiglet.figlet_format("ZigZag Coder", font="digital")
    colored_banner = colored(banner, color="blue")
    print(colored_banner)

    while True:
        print(colored("\n💻 Connection Established. Ready to encode or decode your secrets?", color="yellow"))
        print(Fore.CYAN + "1.📟 Encode Something" + Style.BRIGHT)
        print(Fore.CYAN + "2.🌿 Decode Something" + Style.BRIGHT)
        print(Fore.CYAN + "3.🌱 Show Encoding History" + Style.BRIGHT)
        print(Fore.CYAN + "4.💀 Show Decoding History" + Style.BRIGHT)
        print(Fore.CYAN + "5.🧹 Clear Encoding History" + Style.BRIGHT)
        print(Fore.CYAN + "6.🪶 Clear Decoding History" + Style.BRIGHT)
        print(Fore.CYAN + "7. Export File as PDF" + Style.BRIGHT)
        print(Fore.CYAN + "8.❕Exit" + Style.BRIGHT)

        choice = input(Fore.YELLOW + "👉 Enter Your Choice (1-8): " + Style.BRIGHT)

        if choice == "1":
            zigzag_encode()

        elif choice == "2":
            zigzag_decode()

        elif choice == "3":
            show_encoding_history()

        elif choice == "4":
            show_decoding_history()

        elif choice == "5":
            clear_encoding_history()

        elif choice == "6":
            clear_decoding_history()

        elif choice == "7":
            export_data_to_pdf()

        elif choice == "8":
            exit_program()
            break

        else:
            print(Fore.RED + "⚠️ Please Enter a Valid Input!" + Style.BRIGHT)

if __name__ == "__main__":
    main()

            
            