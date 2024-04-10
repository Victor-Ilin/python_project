from Account import Account
from db.query_handler import *
from datetime import datetime

class UserActivity:
    """
    Class contains operation related to the user's account
    """

    @staticmethod
    def add_user(account: Account, query: QueryHandler) -> None:
        """
        Method adding new user account to database
        :param Account: The account object to insert
        :param query: The query object
        :return: None
        """
        query.execute_non_fetch("INSERT INTO accounts (user_name, password, registration_date) VALUES (%s, %s, %s)",
                                (account.username, account.password, account.date_registration))

    @staticmethod
    def is_user_exist(name: str, password: str, query: QueryHandler) -> bool:
        """
        Method checks if a user available in the database
        :param name: User's name
        :param password: User's password
        :param query: The query object
        :return: True if user exist and false otherwise
        """
        if not isinstance(name, str) or not isinstance(password, str):
            raise ValueError("Incorrect name or password")
        if query.execute_fetch("SELECT * FROM accounts WHERE user_name=%s and password=%s", (name, password)):
            return True
        else:
            return False

    @staticmethod
    def all_accounts(query: QueryHandler) -> None:
        """
        Method displays all accounts
        :param query: The query object
        :return: None
        """
        accounts = query.execute_fetch(
            "SELECT user_id,user_name,DATE_FORMAT(registration_date,%s) as 'registration date' FROM accounts", ('%d/%m/%y',))
        if not accounts:
            print("No accounts to display", end="\n\n")
        else:
            for account in accounts:
                for field_name, info in account.items():
                    print(field_name, ":", info)
                print("-----------------------------------------------------------------------")

    @staticmethod
    def create_registration_date(query: QueryHandler) -> str:
        """
        Method create and returns a data of registration date of account.
        :param query: The query object
        :return: String that contains registration date
        """
        return str(datetime.now())