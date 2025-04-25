from colorama import Fore, Style, init
import time
import random
import pygame
import threading

pygame.init()
pygame.mixer.init()
init(autoreset=True)

# 🎵 Background & Sound Functions
def play_background_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(0.3)
    pygame.mixer.music.play(-1)

def stop_background_music():
    pygame.mixer.music.stop()

def play_sound(sound_file):
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# ⏱ Timer-based Input Class
class TimedInput:
    def __init__(self):
        self.user_input = None

    def get_input(self):
        self.user_input = input(Fore.MAGENTA + "Your answer (A/B/C/D) or '5050' or 'exit': ")

    def input_with_timeout(self, timeout=15):
        input_thread = threading.Thread(target=self.get_input)
        input_thread.daemon = True
        input_thread.start()
        input_thread.join(timeout)

        if input_thread.is_alive():
            print(Fore.RED + f"\n⏰ Time's up! You took more than {timeout} seconds.")
            return None
        else:
            return self.user_input.strip().upper()

# 🧠 Questions
questions_list = [Fore.LIGHTYELLOW_EX +
    "Q1: Which of the following is the correct way to declare a variable in Python?" + Fore.CYAN +
    "\nA) int x = 10\nB) x := 10\nC) x = 10\nD) var = 10",
    
    Fore.LIGHTYELLOW_EX + "Q2: What is the output of print(3 + 2 * 2) in Python?\n"
    + Fore.CYAN + "A) 10\nB) 7\nC) 8\nD) 5",

    Fore.LIGHTYELLOW_EX + "Q3: Which of the following is a mutable data type in Python?\n"
      + Fore.CYAN + "A) str\nB) tuple\nC) list\nD) int",

    Fore.LIGHTYELLOW_EX + "Q4: What is the keyword used to define a function in Python?\n"
      + Fore.CYAN + "A) function\nB) def\nC) func\nD) define",

    Fore.LIGHTYELLOW_EX + "Q5: Which of the following is not a valid Python data type?\n"
      + Fore.CYAN + "A) list\nB) dict\nC) set\nD) array",

    Fore.LIGHTYELLOW_EX + "Q6: What is the output of print(type(5)) in Python?\n"
      + Fore.CYAN + "A) <class 'int'>\nB) <type 'int'>\nC) int\nD) 5",

    Fore.LIGHTYELLOW_EX + "Q7: Which of the following is used to create a comment in Python?\n"
      + Fore.CYAN + "A) //\nB) #\nC) /* */\nD) <!-- -->",

    Fore.LIGHTYELLOW_EX + "Q8: What is the output of print(bool('False')) in Python?\n"
     + Fore.CYAN + "A) True\nB) False\nC) None\nD) Error",

    Fore.LIGHTYELLOW_EX + "Q9: Which of the following is a built-in function in Python?\n"
      + Fore.CYAN + "A) print()\nB) echo()\nC) write()\nD) display()",

    Fore.LIGHTYELLOW_EX + "Q10: What is the correct way to create a list in Python?\n"
      + Fore.CYAN + "A) list = [1, 2, 3]\nB) list = (1, 2, 3)\nC) list = {1, 2, 3}\nD) list = <1, 2, 3>",

    Fore.LIGHTYELLOW_EX + "Q11: Which of the following is not a valid way to import a module in Python?\n"
      + Fore.CYAN + "A) import math\nB) from math import *\nC) import math as m\nD) include math",

    Fore.LIGHTYELLOW_EX + "Q12: What is the output of print(2 ** 3) in Python?\n"
      + Fore.CYAN + "A) 6\nB) 8\nC) 9\nD) 5",

    Fore.LIGHTYELLOW_EX + "Q13: Which of the following is a valid way to open a file in Python?\n"
      + Fore.CYAN + "A) open('file.txt', 'r')\nB) open('file.txt', 'w')\nC) open('file.txt', 'a')\nD) All of the above",

    Fore.LIGHTYELLOW_EX + "Q14: What is the output of print('Hello' + 'World') in Python?\n"
      + Fore.CYAN + "A) HelloWorld\nB) Hello World\nC) Hello+World\nD) Error",

    Fore.LIGHTYELLOW_EX + "Q15: Which of the following is not a valid way to create a dictionary in Python?\n"
      + Fore.CYAN + "A) dict = {}\nB) dict = []\nC) dict = {'key': 'value'}\nD) dict = dict()"
    + Style.RESET_ALL
]

answers_list = ["C", "B", "C", "B", "D", "A", "B", "A", "A", "A", "D", "B", "D", "A", "B"]

options_dict = {i: ["A", "B", "C", "D"] for i in range(15)}

def ask_questions():
    play_background_music("bg_music.mp3")

    score = 0
    lifeline_used = False

    print(Fore.GREEN + "------✨ Welcome to the KBC Quiz! -------")
    username = input(Fore.LIGHTBLUE_EX + "👤 Enter your name: ")
    print(Fore.YELLOW + f"\n🎯 Hello {username}, Let's begin the game!")
    print(Fore.YELLOW + "📤 You can exit the quiz anytime by typing 'exit'")
    print(Fore.YELLOW + "🧠 Type '5050' to use a 50:50 lifeline (only once)\n")

    play_sound("start.mp3")  # Welcome Sound

    for i in range(len(questions_list)):
        play_background_music("bg_music.mp3")
        while True:
            print(Fore.YELLOW + f"🏆 Question {i+1} for ₹{(i+1)*1000}")
            print(questions_list[i])

            # 🔁 Use timed input
            timer_input = TimedInput()
            user_answer = timer_input.input_with_timeout(15)

            if user_answer is None:
                print(Fore.RED + f"❌ You didn't answer in time!")
                play_sound("wrong.mp3")
                print(Fore.LIGHTRED_EX + "-------- GAME OVER 🎯 --------")
                print(Fore.LIGHTMAGENTA_EX + f"Your total score is: ₹{score}" + Style.RESET_ALL)
                save_score(username, score)
                stop_background_music()
                return

            if user_answer == "EXIT":
                print(Fore.LIGHTRED_EX + "\n👋 Exiting the quiz.")
                print(Fore.LIGHTMAGENTA_EX + f"Your total score is: ₹{score}" + Style.RESET_ALL)
                save_score(username, score)
                stop_background_music()
                return
            
            elif user_answer == "5050":
                if not lifeline_used:
                    lifeline_used = True
                    correct_option = answers_list[i]
                    all_options = options_dict[i]
                    wrong_options = [opt for opt in all_options if opt != correct_option]
                    removed = random.sample(wrong_options, 2)
                    remaining = [opt for opt in all_options if opt not in removed]
                    print(Fore.LIGHTCYAN_EX + f"Available options: {', '.join(remaining)}")
                    continue
                else:
                    print(Fore.RED + "❌ You have already used the 50:50 lifeline!")
                    continue

            elif user_answer not in ["A", "B", "C", "D"]:
                print(Fore.RED + "❌ Invalid input. Please enter A, B, C, D, '5050' or 'exit'.")
                continue

            else:
                print(Fore.BLUE + "⏳ Checking your answer...")
                time.sleep(1.5)

                if user_answer == answers_list[i]:
                    play_sound("correct.mp3")
                    print(Fore.GREEN + f"✅ Correct! You win ₹{(i+1)*1000}.\n")
                    score += (i + 1) * 1000
                    break
                else:
                    play_sound("wrong.mp3")
                    print(Fore.RED + f"👎 Incorrect! The correct answer was: {answers_list[i]}")
                    print(Fore.LIGHTRED_EX + "-------- GAME OVER 🎯 --------")
                    print(Fore.LIGHTMAGENTA_EX + f"Your total score is: ₹{score}" + Style.RESET_ALL)
                    save_score(username, score)
                    stop_background_music()
                    return

        print(Style.RESET_ALL)

    print(Fore.GREEN + "\n🎉 Congratulations! You've completed the quiz! 🎉")
    print(Fore.LIGHTMAGENTA_EX + f"Your final score is: ₹{score}" + Style.RESET_ALL)
    save_score(username, score)


def save_score(username, score):
    with open("scores.txt", "a", encoding="utf-8") as file:
        file.write(f"{username}: ₹{score}\n")


ask_questions()
