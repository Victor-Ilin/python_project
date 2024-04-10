from diceware_generator.Die import *
from hashlib import sha512


class GeneratorPass:
    """
    Class which generates and encrypting password for user's account
    """

    @staticmethod
    def create_number(die: Die, throws_amount: int) -> str:
        """
        Method create number with toss die method
        :param die: The die object
        :param throws_amount: amount of throws that build a number
        :return: String
        """
        number = ""
        for i in range(throws_amount):
            number += die.toss_die(1, 6)

        return number

    def get_diceware_dict(AccDict) -> None:
        """
        Method converting getted file to dictionary format
        :param diceware_file: Address where file locate
        :raises: FileNotFoundError: If file not found
        :return: None
        """
        # dictionary = {}
        try:
            f = open("diceware.txt", "r")
            for row in f:
                key, value = row.split()
                AccDict[key] = value
            f.close()
        except FileNotFoundError:
            raise FileNotFoundError("File not exist")


def create_password(words_amount: int) -> str:
    """
    Method generating, encrypting and returning password
    :param words_amount: amount of words in password
    :return: String
    """
    password = ""
    accDict = {}
    print("1")
    GeneratorPass.get_diceware_dict(accDict)

    for i in range(words_amount):

        number_to_check = GeneratorPass.create_number(Die(1, 6), 5)

        if number_to_check in accDict:

            password += accDict.get(number_to_check)
        else:
            password += ""
    password_encrypted = sha512(password.encode()).hexdigest()
    return password_encrypted
