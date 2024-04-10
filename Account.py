

class Account:
    def __init__(self, username: str, password: str, date_registration: str) -> None:
        """
        Constructor that initializes user account
        :param username: User's account name
        :param password: Password for entrance
        :param date_registration: Date and time of account's registration
        """

        self.username = username
        self.password = password
        self.date_registration = date_registration

    # GETTERS
    @property
    def username(self) -> str:
        """
        Getter return the name of user's account
        :return: username
        """
        return self.__username

    @property
    def password(self) -> str:
        """
        Getter return the password of user's account
        :return: password
        """
        return self.__password

    @property
    def date_registration(self) -> str:
        """
        Getter return the registration date of account
        :return: date_registration
        """
        return self.__date_registration

    # SETTERS

    @username.setter
    def username(self, username: str) -> None:
        """
        Setter sets a name of account
        :param username: a name of account
        :raises ValueError - if the given name format is invalid. Must be a string
        :return: None
        """
        if not isinstance(username, str):
            raise ValueError("Incorrect name")

        self.__username = username

    @password.setter
    def password(self, password: str) -> None:
        """
        Setter sets a password of account
        :param password: a password of account
        :raises ValueError - if the given password format is invalid. Must be a string
        :return: None
        """
        if not isinstance(password, str):
            raise ValueError("Incorrect password")

        self.__password = password

    @date_registration.setter
    def date_registration(self, date_registration: str) -> None:
        """
        Setter sets a date of user's registration
        :param date_registration:
        :raises ValueError - if the given date_registration format is invalid. Must be a string
        :return: None
        """
        if not isinstance(date_registration, str):
            raise ValueError("Incorrect password")

        self.__date_registration = date_registration