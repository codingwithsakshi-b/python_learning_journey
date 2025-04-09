#string palindrome 
word = input("enter your word:")

if(word == word[::-1]):
    print("the word is a palindrome")
else:
    print("the word is not palindrome")

#number palindrome

num = input("enter your number:")

if(num == num[::-1]):
    print("the number is palindrome")
else:
    print("number is not palindrome")