def browse():
    import view_all
    regno=int(input("Enter the registration number of the desired profile to be browsed - "))
    yeah=0
    for profile in view_all.data:
        if profile[0] == regno:
            headers = ["Registration Number", "Name", "Grade", "Section", "Phone Number", "Email Address",
                       "Test Scores"]
            import tabulate
            print(tabulate.tabulate([profile], headers=headers, tablefmt="grid"))
            yeah=1
        else:
            continue
    if yeah==0:
        print("Profile not found")
    else:
        pass
    from closemenu import exit_request
    exit_request()
browse()


