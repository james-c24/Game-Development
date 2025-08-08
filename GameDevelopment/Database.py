database = {}
while True:
    print("1. Insert Country and Capital")
    print("2. Display All Countries")
    print("3. Display All Capitals")
    print("4. Get Capital")
    print("5. Delete \n")
    choice = input("Which function would you like to use? \n")
    if choice == "1":
        new_country = input("What country would you like to add? \n")
        new_capital = input("What is the capital of that country? \n")
        database[new_country] = new_capital
        print("Your country has been inserted into the database.\n")
    elif choice == "2":
        print()
        for key in database.keys():
            print(key)
        print()
    elif choice == "3":
        print()
        for value in database.values():
            print(value)
        print()
    elif choice == "4":
        while True:
            select_country = input("What country would you like to find the capital of? Type BACK to return to list.\n")
            if select_country in database:
                print(database[select_country])
                print()
                break
            elif select_country == "BACK":
                print()
                break
            else:
                print("Sorry, please try that again.")
    elif choice == "5":
        while True:
            delete_country = input("What country would you like to delete from the database? Type BACK to return to list.\n")
            if delete_country in database:
                del database[delete_country]
                print("{} has been deleted from the database.\n").format(delete_country)
                break
            elif delete_country == "BACK":
                print()
                break
            else:
                print("Sorry, please try that again.")
    else:
        print("Sorry, please type the number of the function you would like to use again.\n")