import datetime as dt
from utils import *
from register import *
# registration

login_menu = ["Register", "Sign in", "Exit"]

auth_menu = ["List All Projects", "Create Project",
             "Edit Project", "Delete Project","Logout" ]

# project model
project = {
    "owner": "",
    "title": "",
    "details": "",
    "target": 0,
    "start": dt.datetime.now(),
    "end": dt.datetime.now()
}




def sign_in_menu():
    print_title("Sign in")
    while True:
        email = input("Enter you email : ")
        password = input("Enter you password : ")
        user = find_user(email)
        if user != {}:
            print(f"{user}")
            if user["password"]== password :
                home_menu(user) 
                break
            else:
                print_title("Wrong Password try again")           
                continue
        else :
            print_title("Email not register !")
            continue
    
       

def home_menu(user:dict):
    fname = user["fname"]
    lname = user["lname"]
    # phone = user["phone"]
    # email = user["email"]

    print_title(f"Welcome {fname} {lname}")
  
    # 4 -> logout
    while True:

        create_menu(auth_menu, ps1=PS1)

        input_data = input(PS1)
        if input_data.isdigit():
            option = input_data
        else:
            option = "5" #just a number above 4
            print("Invalid option !!")
            continue


        option = int(option)
        if option == 0:
            # Todo: List projects
            print(f"{auth_menu[0]}")
        elif option == 1:
            # Todo: Create  project
            print(f"{auth_menu[1]}")
        elif option == 2:
            # Todo: Edit Project
            print(f"{auth_menu[2]}")
        elif option == 3:
            # Todo: Delete Project 
            print(f"{auth_menu[3]}")
        elif option == 4:
            break  # logout
        else:
            print_title("Invalid option!")



# -------------------------------------------------
#                       start point
# -------------------------------------------------

if __name__ == "__main__":
    option = None
    print_title("Welcome To MO Starter Console")
    while option != 2:

        create_menu(login_menu, ps1=PS1)

        input_data = input(PS1)
        if input_data.isdigit():
            option = input_data
        else:
            option = "3"
            print_title("Invalid option!")
            continue

        option = int(option)
        if option == 0:
            register_menu()
        elif option == 1:
            sign_in_menu()
        elif option == 2:
            break
        else:
            print_title("Invalid option!")
