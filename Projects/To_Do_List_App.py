from colorama import Fore, Style
import json
import pygame
pygame.init()          
pygame.mixer.init()
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import threading
import time
from plyer import notification


def play_background_music(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.set_volume(0.3)  # Adjust volume (0.0 to 1.0)
    pygame.mixer.music.play(-1)         # -1 means loop forever

def stop_background_music():
    pygame.mixer.music.stop()


def background_reminder(user):
    while True:
        time.sleep(60)  # Check every 60 seconds
        user.show_reminders()

class ToDoApp:
    def __init__(self):
            self.task_list = []
            self.load_data()

    def add_task(self):
        task = input(Fore.LIGHTYELLOW_EX + "📝 Enter a task: " + Style.BRIGHT).lower()
        priority = input(Fore.YELLOW + "⚡ Set Priority (Low / Medium / High): ").capitalize()
        
        while True:
            Due_date = input(Fore.GREEN + "📅 Enter Due Date (YYYY-MM-DD) or leave Blank: ")
            
            if Due_date.strip() == "":
                due_date = datetime.today().strftime("%Y-%m-%d")
                print(Fore.CYAN + f"📅 Default due date set to: {due_date}" + Style.BRIGHT)
                break

            try:
                valid_date = datetime.strptime(Due_date, "%Y-%m-%d")
                due_date = valid_date.strftime("%Y-%m-%d")
                break
            except ValueError:
                print(Fore.RED + " ❌ Invalid date format! Please use YYYY-MM-DD." + Style.BRIGHT)
        
        
        task_dict = {
            "title": task,
            "completed": False,
            "Priority": priority,
            "Due Date": Due_date
        }
        print(Fore.GREEN + "Task Added Successfully ✅ ")
        self.task_list.append(task_dict)
        self.save_data()
        self.show_reminders()

    def view_task(self):

        if len(self.task_list) == 0:
            print(Fore.RED + "🚫 No Tasks Found. Add a Task 📝." + Style.BRIGHT)
        else:
            # Priority order: High > Medium > Low
            priority_order = {"High": 1, "Medium": 2, "Low": 3}

            # Sort tasks based on priority
            sorted_tasks = sorted(
                self.task_list,
                key=lambda x: priority_order.get(x["Priority"], 4)
            )

            for index, task in enumerate(sorted_tasks, start=1):
                status = "Done✅" if task["completed"] else "Not Done❌"
                print(
                    (Fore.LIGHTGREEN_EX if task["completed"] else Fore.RED)
                    + f"{index}. {task['title']} | {status} | Priority: {task['Priority']} | Due Date: {task['Due Date']}"
                    + Style.BRIGHT
                )

            
    def mark_task_done(self):
        
        if len(self.task_list) == 0:
            print(Fore.RED + "⛔ No Task Found. Add a Task 📜." + Style.BRIGHT)
            return
            
        self.view_task()
        try:    
            task_num = int(input(Fore.CYAN + "Enter Task Number You Want to Mark as DONE ✅: " + Style.BRIGHT))
            task_index = task_num - 1
            
            if 0 <= task_index <len(self.task_list):
                self.task_list[task_index]["completed"] = True
                print(Fore.GREEN + f"✅ Task {self.task_list[task_index]['title']} mark as completed." + Style.BRIGHT)
                self.save_data()

            else:
                print(Fore.RED + f"⚠️ Invalid Task Number. Please Enter a valid t.no!")

        except ValueError:
            print(Fore.RED + "Enter a valid Numeric input..." + Style.BRIGHT)
        

    def delete_task(self):
       
        if len(self.task_list) == 0 :
            print(Fore.LIGHTRED_EX + "⚠️ No Task Found." + Style.BRIGHT)
            return
        
        self.view_task()

        try:
            task_num = int(input(Fore.YELLOW + "📜 Enter the Task Number YOU Want to Delete: " + Style.BRIGHT))
            task_index = task_num - 1

            if 0 <= task_index < len(self.task_list):            
                final_choice = input(
                    Fore.LIGHTYELLOW_EX + "✨ Are You Sure Want To Delete this Task? (yes/no)" + Style.BRIGHT
                    ).lower()
                
                if final_choice == "yes":
                    deleted_task = self.task_list[task_index]['title']
                    del self.task_list[task_index]
                    print(Fore.RED + f"🚮 Task {deleted_task} deleted Successfully ✅." + Style.BRIGHT)
                    self.save_data()
                
                elif final_choice == "no":
                    print(Fore.GREEN + "Yayy You Saved your task From Deletion..🥳" + Style.BRIGHT)    
                
                else:
                    print(Fore.RED + "Please Enter 'yes' or 'no' in input..." + Style.BRIGHT)
            else:
                print(Fore.RED + "Please Enter A Valid Input!...." + Style.BRIGHT)

        except ValueError:
            print(Fore.RED + "Please Enter a Valid Input..." + Style.BRIGHT)
        
    def save_data(self):
        with open("tasks.json", "w") as f:
            json.dump(self.task_list, f, indent=4)
 
    def load_data(self):
        try:
            with open("tasks.json", "r") as f:
                self.task_list = json.load(f)
            print(Fore.GREEN + "📂 Tasks Loaded Successfully ✅" + Style.BRIGHT)
        
        except FileNotFoundError:
            self.task_list = []
            print(Fore.YELLOW + "⚠️  No existing task file found. Starting fresh!" + Style.BRIGHT)
        except json.JSONDecodeError:
            self.task_list = []
            print(Fore.RED + "⚠️ Task file is corrupted or empty. Starting with empty list." + Style.BRIGHT)
        except Exception as e:
            print(Fore.RED + f"⚠️ Error Loading Tasks: {e}" + Style.BRIGHT)

    def search_task(self):
        search_keyword = input(Fore.CYAN + "🔍Enter a Keyword to search i task title: " + Style.BRIGHT)
        found = False

        for index, task in enumerate(self.task_list, start=1):
            if search_keyword in task['title'].lower():
                status = "Done✅" if task["completed"] else "Not Done❌"
                print(Fore.GREEN + f"{index}. {task['title']} | {status} | Priority: {task['Priority']} | Due Date: {task['Due Date']}")
                found = True

        if not found:
            print(Fore.RED + "❌ No Matching Task Found!" + Style.BRIGHT)
    

    def clear_all_tasks(self):
        confirm = input("⚠️ Are You Sure You want to delete ALL Tasks? (yes/no)").lower()

        if confirm == "yes":
            self.task_list.clear()
            with open("tasks.json", "w") as f:
                json.dump([], f, indent=4)
            print(Fore.RED + "🧹 All Tasks have been Cleared!" + Style.BRIGHT)

        elif confirm == "no":
            print(Fore.GREEN + "✅ All Tasks Were kept Safe!" + Style.BRIGHT)

        else:
            print(Fore.LIGHTRED_EX + "Please Enter Yes/No in input!" + Style.BRIGHT)

    def export_to_csv(self):
        if len(self.task_list) == 0:
            print(Fore.LIGHTRED_EX + "🚫 No Tasks Found!" + Style.BRIGHT)
            return
        
        file_name = input(Fore.YELLOW + "🗃️ Enter File Name To export(eg. tasks.csv) --> " + Style.BRIGHT)
        try:
            with open(file_name , mode='w', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=["title", "completed", "Priority", "Due Date"])
                writer.writeheader()
                writer.writerows(self.task_list)

            print(Fore.GREEN + f"✅ Tasks exported Successfully to {file_name}!" + Style.BRIGHT)

        except Exception as e:
            print(Fore.RED + f"⚠️ Error exporting to CSV: {e}" + Style.BRIGHT)

    def export_to_pdf(self):
        if len(self.task_list) == 0:
            print(Fore.LIGHTRED_EX + "🚫 No Tasks Found!" + Style.BRIGHT)
            return
        
        file_name = input(Fore.YELLOW + "🗃️ Enter File Name To export(eg. tasks.pdf) --> " + Style.BRIGHT)
        try:
            c = canvas.Canvas(file_name, pagesize=letter)
            width, height = letter

            c.setFont("Helvetica", 12)
            c.drawString(30, height - 40, "To-Do List Tasks:")
            y_position = height - 60

            for task in self.task_list:
                status = "Done✅" if task["completed"] else "Not Done❌"
                task_text = f"Task: {task['title']} | Status: {status} | Priority: {task['Priority']} | Due Date: {task['Due Date']}"
                c.drawString(30, y_position, task_text)
                y_position -= 20

                if y_position < 40:
                    c.showPage()
                    c.setFont("Helvetica", 12)
                    y_position = height - 40

            c.save()

            print(Fore.GREEN + f"✅ Tasks exported successfully to {file_name}!" + Style.BRIGHT)
        except Exception as e:
            print(Fore.RED + f"⚠️ Error exporting to PDF: {e}" + Style.BRIGHT)

    from datetime import datetime

    def show_reminders(self):
        today = datetime.today().date()
        reminders = []

        for task in self.task_list:
            try:
                due_date = datetime.strptime(task["Due Date"], "%Y-%m-%d").date()
                if not task["completed"] and due_date <= today:
                    reminders.append(task)
            except ValueError:
                continue  # Skip tasks with invalid dates

        if reminders:
            print(Fore.LIGHTMAGENTA_EX + "\n🔔 Reminder: These tasks are due today or overdue!")
            for task in reminders:
                print(Fore.MAGENTA + f"👉 {task['title']} | Priority: {task['Priority']} | Due Date: {task['Due Date']}")
            
            # 📢 Popup Notification
            notification.notify(
                title="🔔 Task Reminder!",
                message=f"You have {len(reminders)} task(s) due today or overdue!",
                timeout=10  # seconds
            )

            # 🔊 Sound alert
            try:
                pygame.mixer.Sound("reminder.wav").play()
            except Exception as e:
                print(Fore.YELLOW + "🔇 Reminder sound could not be played.")
        else:
            print(Fore.CYAN + "\n✅ No due or overdue tasks today!" + Style.RESET_ALL)

    def edit_task(self):
        if len(self.task_list) == 0:
            print(Fore.RED + "⚠️ No Tasks Found to Edit." + Style.BRIGHT)
            return

        self.view_task()

        try:
            task_num = int(input(Fore.CYAN + "\n✏️ Enter Task Number to Edit: " + Style.BRIGHT))
            index = task_num - 1

            if 0 <= index < len(self.task_list):
                task = self.task_list[index]
                print(Fore.YELLOW + f"\nEditing Task: {task['title']}" + Style.BRIGHT)

                print("\n1. ✍️ Edit Title")
                print("2. ⚡ Edit Priority")
                print("3. 📅 Edit Due Date")
                print("4. ✅ Mark as Completed / ❌ Not Completed")
                print("5. 🔙 Cancel")

                choice = input(Fore.CYAN + "👉 What would you like to edit? (1-5): " + Style.BRIGHT)

                if choice == "1":
                    new_title = input("Enter new title: ").strip()
                    if new_title:
                        task['title'] = new_title.lower()
                        print(Fore.GREEN + "✅ Title updated.")

                elif choice == "2":
                    new_priority = input("Enter new priority (Low / Medium / High): ").capitalize()
                    if new_priority in ["Low", "Medium", "High"]:
                        task['Priority'] = new_priority
                        print(Fore.GREEN + "✅ Priority updated.")
                    else:
                        print(Fore.RED + "❌ Invalid priority.")

                elif choice == "3":
                    new_due_date = input("Enter new due date (YYYY-MM-DD): ")
                    try:
                        valid_date = datetime.strptime(new_due_date, "%Y-%m-%d")
                        task['Due Date'] = valid_date.strftime("%Y-%m-%d")
                        print(Fore.GREEN + "✅ Due Date updated.")
                    except ValueError:
                        print(Fore.RED + "❌ Invalid date format.")

                elif choice == "4":
                    toggle = input("Mark as completed? (yes/no): ").lower()
                    if toggle == "yes":
                        task["completed"] = True
                        print(Fore.GREEN + "✅ Task marked as completed.")
                    elif toggle == "no":
                        task["completed"] = False
                        print(Fore.YELLOW + "⏳ Task marked as not completed.")
                    else:
                        print(Fore.RED + "❌ Invalid input.")

                elif choice == "5":
                    print(Fore.BLUE + "🔙 Cancelled editing." + Style.BRIGHT)
                    return

                else:
                    print(Fore.RED + "❌ Invalid option.")

                self.save_data()

            else:
                print(Fore.RED + "❌ Invalid task number.")
        except ValueError:
            print(Fore.RED + "❌ Please enter a valid numeric input.")


def main():
    play_background_music("bg_music.mp3")
    print(Fore.CYAN + "===== Welcome to To-Do-List Main Menu =====-" + Style.BRIGHT)
    user = ToDoApp()
    user.show_reminders()
    # Start background reminder thread
    reminder_thread = threading.Thread(target=background_reminder, args=(user,), daemon=True)
    reminder_thread.start()

    while True:
        print(Fore.LIGHTBLUE_EX + "\n1. 📝 Add a Task"  + Style.BRIGHT)
        print(Fore.LIGHTBLUE_EX + "2. View Task" + Style.BRIGHT)
        print(Fore.LIGHTBLUE_EX + "3. Mark Task As Done✅ " + Style.BRIGHT)
        print(Fore.LIGHTBLUE_EX + "4. Delete a Task🔕 " + Style.BRIGHT)
        print(Fore.LIGHTBLUE_EX + "5. Clear ALL Tasks🧹 " + Style.BRIGHT)
        print(Fore.BLUE + "6. 🔍 Search a Task.." + Style.BRIGHT)
        print(Fore.BLUE + "7. 📂 Export as .CSV file" + Style.BRIGHT)
        print(Fore.BLUE + "8. 🗄️ Export as .PDF file (recommended)" + Style.BRIGHT)
        print(Fore.BLUE + "9. 🖊️ Edit a Task" + Style.BRIGHT)
        print(Fore.LIGHTRED_EX + "10. Exit🚪 " + Style.BRIGHT + Style.BRIGHT)


        choice = input(Fore.YELLOW + "👉 Enter a Choice (1-9): \n" + Style.BRIGHT)

        if choice == "1":
            user.add_task()

        elif choice == "2":
            user.view_task()

        elif choice == "3":
            user.mark_task_done()

        elif choice == "4":
            user.delete_task()

        elif choice == "5":
            user.clear_all_tasks()

        elif choice == "6":
            user.search_task()

        elif choice == "7":
            user.export_to_csv()

        elif choice == "8":
            user.export_to_pdf()

        elif choice == "9":
            user.edit_task()

        elif choice == "10":
            print(Fore.GREEN + "\n👋 Thank You For Using To-Do-List App..." + Style.BRIGHT)
            stop_background_music()
            break

        else:
            print(Fore.RED + "⚠️ Please Enter A Valid Choice between 1-6..." + Style.BRIGHT)

if __name__ == "__main__":
    main()