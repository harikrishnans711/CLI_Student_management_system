#imports
from banner import banner_print

#banner
banner_print()

#main menu
def main_menu():
    print("Welcome to CLI Student management system!\n")
    print("Choose one of the following options:\n")
    print("[1] View list of all existing student profiles")
    print("[2] Create new student profile")
    print("[3] Browse particular profile")
    print("[4] Edit existing profile")
    print("[5] Delete existing profile\n")
    choice=int(input("Your option - "))


