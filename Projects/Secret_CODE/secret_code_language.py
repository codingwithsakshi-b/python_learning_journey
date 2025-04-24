#secret code language
import random
import string
from colorama import Fore, Style
from datetime import datetime

def save_encoding_history(text):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("encoding_history.txt", "a") as f:
        f.write(f"[{time_stamp}] {text}\n")

def save_decoding_history(text):
    time_stamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("decoding_history.txt", "a") as f:
        f.write(f"[{time_stamp}] {text}\n")

def generate_secret_code():

    code = input(Fore.LIGHTYELLOW_EX + "ENTER A STRING: " + Style.BRIGHT).strip().lower()
    code = code.replace(" ", "")
    if len(code) < 3:
        reverse = code[::-1]
        print(Fore.GREEN + f"Secret code: {reverse}" + Style.BRIGHT)
        
        save_encoding_history(f"{code}:{reverse}")
    
    else:
        original_code = code
        code1 =  code[1:] + code[0]
        random_letters =  ''.join(random.choices(string.ascii_letters, k=6))
        code =  random_letters[:3] + code1 + random_letters[3:]
        print(Fore.GREEN + f"Secret code: {code}" + Style.BRIGHT)        

        save_encoding_history(f"{original_code}:{code}")

def decode_secret_code():
    secret_code = input(Fore.LIGHTYELLOW_EX + "Enter the secret code: " + Style.BRIGHT).strip().lower()
    try:
        if len(secret_code) < 3:
            decoded_code = secret_code[::-1]
            print(Fore.GREEN + f"Decoded code: {decoded_code}" + Style.BRIGHT)

            save_decoding_history(f"{secret_code}:{decoded_code}")

        else:
            core_code = secret_code[3:-3]
            decoded_code = core_code[-1] + core_code[:-1]
            print(Fore.GREEN + f"Decoded code: {decoded_code}" + Style.BRIGHT)

            save_decoding_history(F"{secret_code}:{decoded_code}")

    except IndexError:
        print(Fore.RED + "❌ Invalid secret code format! Make sure the code has at least 7 characters after encoding.\nTry again! 🌟" + Style.BRIGHT)

def show_encoded_codes():
    print(Fore.LIGHTBLUE_EX + "\n--- All Encoded Codes ---" + Style.BRIGHT)
    try:
        with open("encoding_history.txt", "r") as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + "⚠️ No history found yet." + Style.BRIGHT)

def show_all_decoded_codes():
    print(Fore.LIGHTBLUE_EX + "\n--- All Decoded Codes ---" + Style.BRIGHT)
    try:
        with open("decoding_history.txt", "r") as f:
            data = f.read()
            print(data)
    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + "⚠️ No history found yet." + Style.BRIGHT)

def main():
    print(Fore.MAGENTA + "===----WELCOME TO SECRET CODE MENU----===" + Style.BRIGHT)

    while True:
        print(Fore.CYAN + "\n1.👨‍💻 Generate Secret Code..🥷 ")
        print("2.📟 Decode Secret code..💫 ")
        print("3. All Encoded codes---->")
        print("4. All Decoded codes--->")
        print("5. Exit👋..." + Style.BRIGHT)

        choice = input(Fore.YELLOW + "👉 Enter a Choice (1-5): " + Style.BRIGHT)

        if choice == "1":
            generate_secret_code()

        elif choice == "2":
            decode_secret_code()

        elif choice == "3":
            show_encoded_codes()

        elif choice == "4":
            show_all_decoded_codes()

        elif choice == "5":
            print(Fore.RED + "Thank You for using this Secret Code generator and decoder🙏 ...")
            print("👋 EXITING...." + Style.BRIGHT)
            break

        else:
            print(Fore.LIGHTRED_EX + "❌ Invalid Input. Enter a valid input (1-3)" + Style.BRIGHT)
main()