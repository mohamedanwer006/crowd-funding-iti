from utils import *
from userservices import *

# user model
user = {
    "fname": "",
    "lname": "",
    "email": "",
    "password": "",
    "phone": ""
}

def register_menu():
    done = False
    print_title("Add New Account")
    while done == False:
        fname = input("Enter you first name : ")
        lname = input("Enter you last name : ")

        while True:
            email = input("Enter you email : ")
            if is_valid_email(email):
                break
            else :
                print_title("Enter a valid email")
        
        while True:
            phone = input("Enter you phone : ")

            if is_valid_phone(phone):
                break
            else :
                print_title("Enter a valid EG phone number")

        while True:
            password = input("Enter your password : ")
            re_password = input("Confirm password: ")
            if password == re_password:
                user["fname"] = fname
                user["lname"] = lname
                user["phone"] = phone
                user["email"] = email
                user["password"] = password
                break
            else:
                print_title("Wrong Password")

        # Add user to db
        add_user(user)
        print_title("Account Add Successfully")
        done = True
