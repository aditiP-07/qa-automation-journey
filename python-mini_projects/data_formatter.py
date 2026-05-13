'''
Test data formatter:
Write a function that takes a first name, last name, and age, and returns a dictionary like {"full_name": "Aditi Prasad", "age": 23, "username": "aditi.prasad"}. Username is firstname.lastname, all lowercase.
'''

def dataFormatter(firstname, age, lastname):
    dic = {}
    dic["full_name"] = firstname + " " + lastname
    dic["age"] = age
    dic["username"] = (firstname + "." + lastname).lower()
    return(dic)

firstname = input("Enter your first name: ")
age = int(input("Enter your age: "))
lastname = input("Enter your last name: ")
username = ""

print(dataFormatter(firstname, age, lastname))