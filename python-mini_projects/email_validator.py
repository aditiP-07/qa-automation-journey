'''
Email validator:
Write a function that takes a string and returns True if it's a valid email, False if not. A valid email must have exactly one @, at least one . after the @, and no spaces.
'''

def validate_email(email):
    if email.count("@") != 1:
        return False
    if " " in email:
        return False
    parts = email.split("@")
    if "." not in parts[1]:
        return False
    return True

email = input("Enter your email address: ")

print(validate_email(email))