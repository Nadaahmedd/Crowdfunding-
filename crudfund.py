import datetime
import time


def generate_id():
    return round(time.time())

def askforstring(message):
    while True:
        instr = input(message)
        if instr.isalpha():
            return instr
        print("try again b alah 3lek")

def askforint(message):
    while True:
        innum = input(message)
        if innum.isdigit():
            return innum
        print("try again b alah 3lek")

def find_project_by_id(project_id):
    projects = get_all_projects()
    for project in projects:

        print(project)
        project_details = project.strip('\n').split(" ")  
        if project_details[0]==str(project_id):
            return project
    else:
        return False
    
def save_projects_to_file(listofprojects):
    try:
        fileobj =open("projects.txt", 'w')
    except Exception as e:
        print(e)
        return False
    else:
        fileobj.writelines(listofprojects)
        fileobj.close()
        return True


    
def delete_project_from_file(project):
    projects= get_all_projects()
    projects.remove(project)  
    removed = save_projects_to_file(projects)
    return removed


# Function to validate date format
def is_valid_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d %H:%M:%S')
        return True
    except ValueError:
        return False

def get_all_projects():
    try:
        fileobj =open("projects.txt", 'r')
    except Exception as e:
        print(e)
        return False
    else:
        users = fileobj.readlines()
        return users


    

def create_project():
    title = input("Enter the title of your project: ")
    details = input("Enter the details of your project: ")
    target = input("Enter the total target for your project (in EGP): ")
    email = input("Enter your email ")
    while not target.isdigit():
        target = input("Invalid target amount. Please enter a valid amount (in EGP): ")
    start_time = input("Enter the start time for your project (YYYY-MM-DD HH:MM:SS): ")
    while not is_valid_date(start_time):
        start_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
    end_time = input("Enter the end time for your project (YYYY-MM-DD HH:MM:SS): ")
    while not is_valid_date(end_time):
        end_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
    id = generate_id()
    with open("projects.txt", "a") as file:
        file.write("{} {} {} {} {} {} {}\n".format(id , title, details, target, start_time, end_time, email ))
    print("Project created successfully.")


def display_all_project():
    projects = get_all_projects()
    if projects:
        for project in projects:
            print(project)
    else:
        print(' Error happened please try again ')

            
def edit_project():
    project_id = askforint("Please enter the id of the project you want to edit: ") # int
    email=input("enter your email ")
    found = find_project_by_id(project_id)
    test = str(found).split() 
    if found :
        print( "found" )
        print(test)
        if test[8]== str(email):
            removed=delete_project_from_file(found)
            title = input("Enter the title of your project: ")
            details = input("Enter the details of your project: ")
            target = input("Enter the total target for your project (in EGP): ")
            email = input("Enter your email ")
            while not target.isdigit():
                target = input("Invalid target amount. Please enter a valid amount (in EGP): ")
            start_time = input("Enter the start time for your project (YYYY-MM-DD HH:MM:SS): ")
            while not is_valid_date(start_time):
                start_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
            end_time = input("Enter the end time for your project (YYYY-MM-DD HH:MM:SS): ")
            while not is_valid_date(end_time):
                end_time = input("Invalid date format. Please enter a valid date (YYYY-MM-DD HH:MM:SS): ")
            id = generate_id()
            with open("projects.txt", "a") as file:
                file.write("{} {} {} {} {} {} {}\n".format(id , title, details, target, start_time, end_time, email ))
            print("Project edited successfully.")
        else:
            print("this project is not yours you can't edit it ")



def delete_project():
    project_id = askforint("Please enter the id of the project you want to delete: ") # int
    email=input("enter your email ")
    found = find_project_by_id(project_id)
    test = str(found).split() 
    if found :
        print( "found" )
        if test[8]== str(email):
            removed=delete_project_from_file(found)
            if removed:
                print('project deleted successfully')
            else:
                print(" problem happened while deleting the project ")
        else:
            print("this project is not yours to delete ")
            return
    else:
        print("project not found, please try again with valid id ")

