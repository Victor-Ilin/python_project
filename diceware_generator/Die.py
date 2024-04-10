from random import randint
from validators.global_validator import *

class Die:
    """
    Die represents a throwing die
    """

    def __init__(self, bottom_range_value: int, top_range_value: int):
        """
        Constructor which defines the upper die side by using a random value
        """
        self.toss_die(bottom_range_value, top_range_value)

    @property
    def die_upper_side(self):
        """
        Getter return the upper side's value
        :return: Die upper side
        """
        return self.__die_upper_side

    @die_upper_side.setter
    def die_upper_side(self, upper_side_value: int):
        """
        Setter which defines the die upper side
        :raise ValueError - Wrong die upper side value
        :return: None
        """
        if not isinstance(upper_side_value, int):
            raise ValueError("Wrong die upper side value")

        self.__die_upper_side = upper_side_value

    def __str__(self) -> str:
        """
        Method returns a string that displays the die upper side value in the specific format
        :return:
        """
        return f"The throwing die upper side value is {self.die_upper_side}"

    def toss_die(self, bottom_die_range: int, top_die_range: int) -> str:
        """
        Method is responsible to simulate the die throwing process
        :param bottom_die_range: bottom range value to use as an upper side value
        :param top_die_range: top range value to use as an upper side value
        :raise ValueError - when passed values don't represent top and bottom range values
        :return: String
        """
        if not GlobalValidator.validate_range(bottom_die_range, top_die_range):
            raise ValueError("Passed values don't represent top and bottom range values")

        self.die_upper_side = randint(bottom_die_range, top_die_range)

        return str(self.die_upper_side)
