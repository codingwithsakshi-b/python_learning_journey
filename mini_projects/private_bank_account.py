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

        print("Account created successfully!✅")
        print(f"\n✅ Welcome {self.name}, your Account Number: {self.__account_number} has been created.🏦💵")
        print(f"Initial Balance: {self.__balance} Rs/\n")
    
    def __verify_pin(self):
      entered_pin = input("🔒 Enter your PIN: ")
      if entered_pin == self.__pin:
        return True
      else:
        print("❌ Incorrect PIN! Access denied.\n")
        return False


    def change_pin(self):
       if self.__verify_pin(): 
          while True:

            new_pin = input("Enter New PIN 🔒:")
            if new_pin == self.__pin:
              print("⚠️ New PIN cannot be the same as the old one. Please choose a different PIN.")
              
            else:
               confirm_pin = input("Confirm 🔒 PIN by re-entering:")
               if confirm_pin != new_pin:
                  print("❌ The new PIN and confirmation PIN do not match. Please try again.")
               else:
                  print("PIN changed successfully! ✅")
                  self.__pin = new_pin
                  break
                                
    def get_balance(self):
       if self.__verify_pin():
        print(f"💰 Your Total Balance is: {self.__balance} Rs/ only!\n")

    def deposit(self, amount):
        
        if self.__verify_pin():
         self.__balance += amount
         print(f"💵 {amount} Rs/ deposited successfully! 🎉\n")
         self.__transactions.append(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} ➜ Deposited {amount} Rs.")
         self.__log_to_file(f"Deposited {amount} Rs/ only.")
    
    def withdraw(self, amount):
       if self.__verify_pin():

        if amount > self.__balance:
            print("⚠️ Insufficient Balance! Transaction Failed.\n")
            self.__transactions.append(f"{datetime.now().strftime('%d-%m-%Y %H:%M:%S')} ➜ withdrawn {amount} Rs. failed due to insufficient balance ")
            self.__log_to_file(f"Transaction Failed!⚠️ Due to insufficient Balance.")       
        else:
            self.__balance -= amount
            print(f"💸 {amount} Rs/ withdrawn from your account!\n")
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
       print("6. ❌ Exit")
       
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
          print("👋 Thank you for using Private Bank CLI! Stay Safe & Secure. 🛡️")
          break
       else:
          print("❌ Invalid choice. Please select a valid option.")

if __name__ == "__main__":
   main()
          
