# main.py
import view_all
from banner import banner_print
from tabulate import tabulate
from exit_req import exit_request
import createprofile

# banner
banner_print()

# main menu
def main_menu():
    print("Welcome to CLI Student management system!\n")
    print("Choose one of the following options:\n")
    print("[1] View list of all existing student profiles")
    print("[2] Create new student profile")
    print("[3] Browse particular profile")
    print("[4] Edit existing profile")
    print("[5] Delete existing profile\n")
    choice = int(input("Your option - "))

    if choice == 1: #view full list
        headers = ["Registration Number", "Name", "Grade", "Section", "Phone Number", "Email Address", "Test Scores"]
        print(tabulate(view_all.data, headers=headers, tablefmt="grid"))
        exit_request()
    elif choice == 2: #create new profile
        createprofile.create_profile()
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    else:
        print("Invalid option selected. Please try again.\n")

main_menu()