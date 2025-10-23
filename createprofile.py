import view_all
from closemenu import exit_request

def create_profile():
    print("Creating a new student profile...\n")
    reg_no = input("Enter Registration Number: ")
    name = input("Enter Name: ")
    grade = input("Enter Grade: ")
    section = input("Enter Section: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email Address: ")
    test_scores = input("Enter Test Scores (comma separated): ")

    new_profile= [reg_no, name, grade, section, phone, email, test_scores]
    view_all.data.append(new_profile)

    print("\nNew student profile created successfully!\n")
    exit_request()
