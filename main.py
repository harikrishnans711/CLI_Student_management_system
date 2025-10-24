# main.py

#Made by S.Raghavapriyan and Harikrishnan
from banner import banner_print
from tabulate import tabulate

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
        import view_all
        headers = ["Registration Number", "Name", "Grade", "Section", "Phone Number", "Email Address", "Test Scores"]
        print(tabulate(view_all.data, headers=headers, tablefmt="grid"))
        from closemenu import exit_request
        exit_request()
    elif choice == 2: #create new profile
        import createprofile
        createprofile.create_profile()
    elif choice == 3: #browsing particular profile
        import browse_particular_profile
        browse_particular_profile.browse()
    elif choice == 4: #editing existing profile
        import editprofile
        editprofile.edit_profile()
    elif choice == 5: #deleting existing profile
        import deleteprofile
        deleteprofile.delete_profile()
    else:
        print("Invalid option selected. Please try again.\n")
        main_menu()
        exit()


main_menu()