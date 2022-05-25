from fileservices import *
from utils import USERS_DB 

def add_user(user: dict):
    fname = user["fname"]
    lname = user["lname"]
    phone = user["phone"]
    email = user["email"]
    password = user["password"]
    data = f"{email}:{password}:{fname}:{lname}:{phone}\n"
    add_data(USERS_DB, data)

def find_user(email:str):
    users = read_data(USERS_DB).splitlines()
    user={}
    for u in users :
        data = u.split(":")
        if email == data[0] :
            user["email"] = data[0]
            user["password"] = data[1]
            user["fname"] = data[2]
            user["lname"] = data[3]
            user["phone"] = data[4]
            break
        else :
            user={}

    return user
    
