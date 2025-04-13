#Create student class that take name & marks of 3 subjects as arguments in constructor.
try:
  class Student: 
    def welcome():
        return "💫🎉 Welcome STUDENT"
    
    def __init__(self, fullname, mark1, mark2, mark3):
        self.name = fullname
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3
        avg = (mark1 + mark2 + mark3)/3
       
        print(Student.welcome())

        print(f"\n🎓 FULLNAME: {self.name}")
        print(f"➗ AVERAGE of marks : {avg}")
        print("-----------------\n")
except Exception as e:
   print(f"⚠️ Error: {e}")
try:
    s1 = Student("Sakshi Kumari", 98.7, 89.7, 78.6)
    s2 = Student("Keshav Sharma", 89.9, 98.5, 92.6)
    s3 = Student("Govind Ji",88.4,78.5,87)
except Exception as e:
   print(f"Error: {e}")     
#by using loop we can solve this question take marks in form of list
try:
  class STUDENT:
    def welcome():
       return("🎉📚 Welcome Dear...")
    
    def __init__(self, fullname, marks): #marks = [33,44,65,43] ab marks kitna bhi subjects ka le skte hai
        self.name = fullname
        self.marks = marks
        
        count = 0
        sum = 0 
        for val in self.marks: 
           sum += val
           count += 1

        print(f"{STUDENT.welcome()}, {self.name}")
        print(f"\nYour➗📚 Avg Score is {sum/count}")
        print("----------------------\n")

except Exception as e:
   print(f"Error: {e}")

s4 = STUDENT("Sakshi Sharma", [89.9, 67.7, 78.9, 98.6, 89.8])
s5 = STUDENT("Keshav Sharma", [90,87.8,97.8,67.9,54.7,89.7,78.9])

#create Account class with 2 attributes - balance & acc no.
# create methods for debit, credit & printing the balance
try:
   class Account:
      
      def __init__(self, balance, account_number):
         self.Balance =  balance
         self.Account_number = account_number
         print(f"\n🔖 Your Account Number is --> {self.Account_number}")
         print(f"Your original Balance is -> Rs.{self.Balance}")
    #debit method
      def debit_money(self, ammount):
         self.Balance -= ammount
         print(f"\nYour Final Balance after 💸 debited Rs.{ammount} money -> Rs.{self.get_balance()} ")
    #credit method
      def credit_money(self, ammount):
         self.Balance += ammount
         print(f"\nYour Final Balance after 💸 credited Rs.{ammount} money -> Rs.{self.get_balance()} ")
        
      def get_balance(self):
         return self.Balance
except Exception as e:
   print(f"Error: {e}")   

A1 = Account(76000, 7878787878)
A1.debit_money(6000)
A1.credit_money(10000)

A2 = Account(10000, 12345678)
A2.credit_money(61000)
A2.debit_money(1000)
