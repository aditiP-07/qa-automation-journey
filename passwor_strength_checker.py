'''
Password strength checker:
Write a function that takes a password string and returns "weak", "medium", or "strong". Your own rules — but define at least 3 criteria (length, numbers, special characters, whatever you decide).
'''

import string 

def passwordStrengthTest(password):
    if (
        len(password) >= 7 
        and any(char.isdigit() for char in password) 
        and any(char in string.punctuation for char in password) 
        and any(char.isupper() for char in password)
    ):
        return("Strong password! ᕙ(⇀‸↼‶)ᕗ ")
    else:
        return("I could hack into your systems if you're not careful enough... (｡- .•)")

password = input("Enter the password: ")
print("You are disclosing your password, you innocent creature (˵¬ᴗ¬˵)")
print("But since you trusted me with it, I will check it for you! (⸝⸝> ᴗ•⸝⸝)")
print(passwordStrengthTest(password))