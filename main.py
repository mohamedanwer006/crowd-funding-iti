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



def list_projects():
    data = PServices.get_projects()
    print("title\t\towner\t\ttarget\tstart-date\tend-date\t\tdetails")
    for i in data:
        print(i)

def delete_project(user):
    title = input("Enter project name to delete : ")
    if PServices.del_project(title,user['email']):
        print_title("Deleted")
    else :
        print_title("you don't has project with this name")


def update_project(user):
    title = input("Enter project title to update : ")
    oldproject= PServices.get_project(title=title,owner=user["email"])
    if oldproject == None :
        print_title("you don't has project with this name")
    else :
        while True:
            print("Press enter for defaults value")
            title = input(f"Project title ({oldproject.title}) : ")
            target = input(f"Project target ({oldproject.target}) : ")
            start = input(f"Start date yyyy-mm-dd ({oldproject.start}) : ")
            end = input(f"End date yyyy-mm-dd ({oldproject.end}) : ")
            details = input(f"Project details ({oldproject.details}): ")
            if title == "":
                title=oldproject.title
            if target =="":
                target=oldproject.target
            if start =="":
                start=oldproject.start
            if end =="":
                end=oldproject.end
            if details =="":
                details=oldproject.details
            
            project = Project(owner=user["email"], title=title, target=target,
                                start=start, end=end, details=details)

            PServices.update_project(project,oldproject,user["email"])
            break


def home_menu(user: dict):
    print_title(f"Welcome {user['fname']} {user['lname']}")

    while True:

        create_menu(auth_menu)
        input_data = input(PS1)

        if input_data.isdigit():
            option = input_data
        else:
            option = "5"  # just a number above 4
            print("Invalid option !!")
            continue
        option = int(option)


        if option == 0:
            list_projects()
        elif option == 1:
            create_project_menu(user)
        elif option == 2:
           update_project(user)

        elif option == 3:
            delete_project(user=user)
        elif option == 4:
            break  # logout
        else:
            print_title("Invalid option!")


# -------------------------------------------------
#                       start point
# -------------------------------------------------
if __name__ == "__main__":
    option = None
    
    print_title("Welcome To MO Console")
    
    while option != 2:

        create_menu(login_menu)

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
