import datetime as dt
from project import Project
from utils import *
from register import *
from projectservices import PServices
# registration

login_menu = ["Register", "Sign in", "Exit"]

auth_menu = ["List All Projects", "Create Project",
             "Edit Project", "Delete Project", "Logout"]


def sign_in_menu():
    print_title("Sign in")
    while True:
        email = input("Enter you email : ")
        password = input("Enter you password : ")
        user = find_user(email)
        if user != {}:
            if user["password"] == password:
                home_menu(user)
                break
            else:
                print_title("Wrong Password try again")
                continue
        else:
            print_title("Email not register !")
            continue


def create_project_menu(user: dict):

    while True:
        title = input("Project title : ")
        target = input("Project target : ")
        start = input("Start date yyyy-mm-dd  : ")
        end = input("End date yyyy-mm-dd  : ")
        details = input("Project details : ")

        project = Project(owner=user["email"], title=title, target=target,
                          start=start, end=end, details=details)

        PServices.add_project(project)
        break


def home_menu(user: dict):
    print_title(f"Welcome {user['fname']} {user['lname']}")

    # 4 -> logout
    while True:

        create_menu(auth_menu, ps1=PS1)

        input_data = input(PS1)
        if input_data.isdigit():
            option = input_data
        else:
            option = "5"  # just a number above 4
            print("Invalid option !!")
            continue

        option = int(option)

        if option == 0:
           
            data = PServices.get_projects()
            print("title\t\towner\t\ttarget\tstart-date\tend-date\t\tdetails")
            for i in data:
                print(i)

        elif option == 1:

            create_project_menu(user)

        elif option == 2:
            # Todo: Edit Project
            print(f"{auth_menu[2]}")
        elif option == 3:
            title = input("Enter project name to delete : ")
            if PServices.del_project(title,user['email']):
                print("delete")
            else :
                print("you don't has project with this name")

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
