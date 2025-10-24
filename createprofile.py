from view_all import data
from closemenu import exit_request

def create_profile():
    print("Creating a new student profile...\n")
    try:
        reg_no = int(input("Enter Registration Number[integer only]: "))
        regnos = list(i[0] for i in data)
        if reg_no in regnos:
            print("Registration Number already exists! TRY AGAIN...")
            create_profile()
        else:
            pass
        name = input("Enter Name: ")
        grade = input("Enter Grade: ")
        section = input("Enter Section: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email Address: ")
        test_scores = input("Enter Test Scores (comma separated): ")
        new_profile = [reg_no, name, grade, section, phone, email, test_scores]
        data.append(new_profile)
        print("Profile created successfully!")
    except:
        print("Invalid Input")
    exit_request()
create_profile()
