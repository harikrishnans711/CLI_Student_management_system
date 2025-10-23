import view_all
from closemenu import exit_request

def delete_profile():
    reg_no = int(input("Enter the registration number of the profile to delete: "))
    profile_found = False
    for profile in view_all.data:
        if profile[0] == reg_no:
            profile_found = True
            confirm = input(f"Are you sure you want to delete profile {profile[1]} (y/n)? ").lower()
            if confirm == 'y':
                view_all.data.remove(profile)
                print(f"Profile with registration number {reg_no} is deleted!")
            else:
                print("Deletion cancelled.")
            exit_request()  
            break

    if not profile_found:
        print("Profile not found.")
        exit_request()
