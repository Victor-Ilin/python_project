
from diceware_generator.password_generator import *
from user_actions.user_activity import *
from user_actions.ui_handler import *

if __name__ == "__main__":
    options_menu = ["Add new user", "Checking user exist", "Display all users", "Exit"]
    q = QueryHandler("localhost", "exercise_diceware", "root", "")
    u = UserActivity()

    while True:
         try:
            UIHandler.show_menu(options_menu)
            choice = input("")

            if choice == "1":  # Adding an user
                user_name = input("Enter name for new user")

                password = create_password(6)
                account = Account(user_name, password, u.create_registration_date(q))
                print(f"Save your password: {account.password}")
                u.add_user(account, q)
            elif choice == "2":  # Checking if user exist
                user_name = input("Enter the username")
                password = input("Enter the password")
                if u.is_user_exist(user_name, password, q):
                    print("Username with inputed password is exist")
                else:
                    print("Username with inputed password don't exist")
            elif choice == "3":  # Displaying all users
                u.all_accounts(q)
            elif choice == "4":  # Exiting the program
                print("Thank you for using our program. Exiting...")
                break
            else:  # If the choice is incorrect, asking for another one
                print(f"Wrong choice. your choice must be between 1 and {len(options_menu)}")


         except BaseException as b:
             print(b)
