import re


PS1 = "Select option number : "
USERS_DB="users"
PROJECTS_DB="projects"
EMAIL_REG = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

PHONE_REG=re.compile(r'^01[0-2,5]{1}[0-9]{8}$')

def is_valid_email(email):
    """
    is_valid_email(email) => True if valid 
    is_valid_email(email) => False if not valid 
    
    """
    if re.fullmatch(EMAIL_REG, email):
      return True
    else:
      return False

def is_valid_phone(phone):
    """
    """
    if re.fullmatch(PHONE_REG,phone):
        return True
    else :
        return False


def print_title(title: str):
    print_dashed_line(len(title))
    print(f"------------------------- {title} -------------------------")
    print_dashed_line(len(title))


def print_dashed_line(number):
    print("------------------------- ", end="")
    for i in range(number):
        print("-", end="")
    print(" -------------------------")


def create_menu(items: list, ps1: str):
    for i in range(len(items)):
        print(f"{i} ) {items[i]}")
