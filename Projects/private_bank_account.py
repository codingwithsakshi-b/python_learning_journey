from getpass import getpass
from colorama import Fore, Style #pip install colorama
from datetime import datetime
import random

class BankAccount:
    def __init__(self, name, email, balance, pin,):
        self.name = name
        self.email = email
        self.__account_number = random.randint(10**9, 10**10-1)
        self.__balance = balance
        self.__pin = str(pin)
        self.__transactions = []

        print(Fore.GREEN + "Account created successfully!✅" + Style.RESET_ALL)
        print(Fore.BLUE + f"\n✅ Welcome {self.name}, your Account Number: {self.__account_number} has been created.🏦💵" + Style.RESET_ALL)
        print(Fore.BLUE + f"Initial Balance: {self.__balance} Rs/\n" + Style.RESET_ALL)
    
    def __verify_pin(self):
      entered_pin = getpass(Fore.YELLOW + "🔒 Enter your PIN:" + Style.RESET_ALL)
      if entered_pin == self.__pin:
        return True
      else:
        print(Fore.RED + "❌ Incorrect PIN! Access denied.\n" + Style.RESET_ALL)
        return False


    def change_pin(self):
       if self.__verify_pin(): 
          while True:

            new_pin = input("Enter New PIN 🔒:")
            if new_pin == self.__pin:
              print(Fore.RED + "⚠️ New PIN cannot be the same as the old one. Please choose a different PIN." + Style.RESET_ALL)
              
            else:
               confirm_pin = input(Fore.YELLOW + "Confirm New PIN 🔒:" + Style.RESET_ALL)
               if confirm_pin != new_pin:
                  print(Fore.RED + "❌ The new PIN and confirmation PIN do not match. Please try again." + Style.RESET_ALL)
               else:
                  print(Fore.GREEN + "PIN changed successfully! ✅" + Style.RESET_ALL)
                  self.__pin = new_pin
                  break
                                
    def get_balance(self):
       if self.__verify_pin():
        print(Fore.GREEN + f"💰 Your Total Balance is: {self.__balance} Rs/ only!\n" + Style.RESET_ALL)

    def deposit(self, amount):
         if amount <= 0:
             print(Fore.RED + "⚠️ Deposit amount must be greater than zero.\n" + Style.RESET_ALL)
             return

         if self.__verify_pin():
             self.__balance += amount
            
             print(Fore.BLUE + f"💵 {amount} Rs/ deposited successfully! 🎉\n" + Style.RESET_ALL)
         
             self.__transactions.append(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} ➜ Deposited {amount} Rs.")
             self.__log_to_file(f"Deposited {amount} Rs/ only.")
    
    def withdraw(self, amount):
         if amount <= 0:
             print(Fore.RED + "⚠️ Deposit amount must be greater than zero.\n" + Style.RESET_ALL)
             return

         if self.__verify_pin():

          if amount > self.__balance:
            print(Fore.RED + "⚠️ Insufficient Balance! Transaction Failed.\n" + Style.RESET_ALL)
            self.__transactions.append(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} ➜ withdrawn {amount} Rs. failed due to insufficient balance ")
            self.__log_to_file(f"Transaction Failed!⚠️ Due to insufficient Balance.")       
          else:
            self.__balance -= amount
            print(Fore.GREEN + f"💸 {amount} Rs/ withdrawn from your account!\n" + Style.RESET_AL)
            self.__transactions.append(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} ➜ withdrawn {amount} Rs.")
            self.__log_to_file(f"withdrawl {amount} Rs/ only.")

    def show_transactions(self):
     if self.__verify_pin():
        print("\n📜 Transaction History:")
        if not self.__transactions:
           print("No transactions yet.")
        else:
          for t in self.__transactions:
            print(f"• {t}\n")
    
    def __log_to_file(self, message):
       with open("transaction_log.txt", "a") as f:
          f.write(f"[{datetime.now().strftime('%d-%m-%Y %H:%M:%S')}] {message}\n")

    def calculate_interest(self, rate):
        if self.__verify_pin():
            interest = self.__balance * (rate / 100)
            self.__balance += interest
            print(Fore.GREEN + f"💰 Interest of {interest} Rs/ added to your balance!\n" + Style.RESET_ALL)
            self.__transactions.append(
                f"{datetime.now().strftime('%d-%m_%Y %H:%M:%S')} ➜ Interest of {interest} Rs/ added.")
            self.__log_to_file(f"Interest of {interest} Rs/ added.")

    def account_summary(self):
        if self.__verify_pin():
            print(Fore.CYAN + "\n🔍 Account Summary:")
            print(f"Nmae: {self.name}")
            print(f"Email: {self.email}")
            print(f"Account Number: {self.__account_number}")
            print(f"Current Balance: {self.__balance} Rs/")
            print("📜 Transactions:")
            for t in self.__transactions:
                print(f"•  {t}")
            print(Style.RESET_ALL)
            
#-----------------------CLI Interface------------------------

def main():
   print("🏦 Welcome to Private Bank CLI 💻\n")
   name = input("Enter Your Name: ")
   email = input("Enter Your Email: ")
   balance = float(input("Enter initial deposit amount (Rs):"))
   pin = input("Set a 4-digit PIN: ")

   user = BankAccount(name, email, balance, pin)

   while True:
       print("\n📋 Choose an option:")
       print("1. 🧾 Check Balance")
       print("2. 💵 Deposit Money")
       print("3. 💸 Withdraw Money")
       print("4. 🔐 Change PIN")
       print("5. 🧾 Show Transactions")
       print("6. 🧮 Calculate Interest")
       print("7. 📜 Summary of Account:")
       print("8. ❌ EXIT")
       
       choice = input("\n Enter Your Choice (1-6):")

       if choice == "1":
          user.get_balance()

       elif choice == "2":
             amount = float(input("Enter amount to deposit: "))
             user.deposit(amount)             
          
       elif choice == "3":
             try:
              amount = float(input("Enter amount to withdraw: "))             
              user.withdraw(amount)
             except ValueError:
                print("❌ invalid amount.")

       elif choice == "4":
          user.change_pin()

       elif choice == "5":
          user.show_transactions()

       elif choice == "6":
           rate = float(input(Fore.YELLOW + "Enter the Interest Rate" + Style.RESET_ALL))
           user.calculate_interest(rate)

       elif choice == "7":
           user.account_summary()

       elif choice == "8":
          print("👋 Thank you for using Private Bank CLI! Stay Safe & Secure. 🛡️")
          break
       else:
          print("❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
   main()
          
