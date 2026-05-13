'''
Login validator:
Write a function that takes a username and password. Valid if: username is at least 4 characters, password is at least 8 characters and contains at least one number. Return "Login valid" or "Login invalid".
'''

def login_validation(username, password):
    if len(username) >= 4 and len(password) >= 8 and any(char.isdigit() for char in password) :
        return "Login valid"
    else:
        return "Login invalid"
    
username = input("Enter your username: ")
password = input("Enter your password: ")

print(login_validation(username, password))