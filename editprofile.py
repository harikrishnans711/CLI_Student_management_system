import view_all
from closemenu import exit_request
def edit_profile():
    reg_no = int(input("Enter Registration number of profile to edit: "))
    profile_found = False
    for profile in view_all.data:
        if profile[0] == reg_no:
            print("Profile found")
            profile_found = True
            print("Current profile details:")
            print(f"[1]: Name: {profile[1]}")
            print(f"[2]: Grade: {profile[2]}")
            print(f"[3]: Section: {profile[3]}")
            print(f"[4]: Phone: {profile[4]}")
            print(f"[5]: Email: {profile[5]}")
            while True:
               edit_field = int(input("Enter the number of the field to edit: "))
               if edit_field == 1:
                   edit_name = input("Enter new name for the profile: ")
                   profile[edit_field] = edit_name
                   print("Name updated successfully!")
                   break
               elif edit_field == 2:
                   edit_grade = input("Enter new grade for the profile: ")
                   profile[edit_field] = edit_grade
                   print("Grade updated successfully!")
                   break
               elif edit_field == 3:
                   edit_section = input("Enter new section for the profile: ")
                   profile[edit_field] = edit_section
                   print("Section updated successfully!")
                   break
               elif edit_field == 4:
                   edit_phone_number = input("Enter new phone number for the profile: ")
                   profile[edit_field] = edit_phone_number
                   print("Phone number updated successfully!")
                   break
               elif edit_field == 5:
                   edit_email = input("Enter new email address for the profile: ")
                   profile[edit_field] = edit_email
                   print("Email address updated successfully!")
                   break
               else:
                   print("Invalid input. Please enter any of the given field numbers.")

    if not profile_found:
        print("Profile not found")
        edit_profile()
    exit_request()



