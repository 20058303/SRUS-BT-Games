"""
File:           player.py
Author:         Bradley Torpy <20058303@Tafe.wa.edu.au>

Description:    Player class used for storing player information, such as ID, Names, Scores and hashed passwords.
"""
import argon2.exceptions
from argon2 import PasswordHasher

ph = PasswordHasher()


class Player:
    def __init__(self, id, name):
        """
        The player object.
        :param id: Unique Identifier for the player.
        :param name: The name of the player.
        """
        self.uid = id
        self.name = name
        self.__score = 0
        self.__password = None

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value=0):
        if value > -1:
            self.__score = value
        else:
            self.__score = 0

    def add_password(self, _string):
        """
        Adds a hashed password to the player class
        :param _string: Password wanting to be set.
        :return: hashed password
        """
        self.__password = ph.hash(_string)

    def verify_password(self, _string):
        """
        Verifies a string with a stored password
        :param _string: string to compare
        :return: True or False
        """
        try:
            if ph.verify(self.__password, _string):
                return True
        except argon2.exceptions.VerifyMismatchError:
            return False

    def __ge__(self, other):
        if self.score >= other.score:
            return True
        return False

    def __lt__(self, other):
        if self.score < other.score:
            return True
        return False

    def __str__(self):
        return f"{self.uid}: {self.name}"

    @staticmethod
    def InsertionSorting(_list):
        try:
            if len(_list) == 0:
                return None
            else:
                for i in range(1, len(_list)):
                    _val = _list[i]
                    _pos = i

                    while _pos > 0 and _list[_pos - 1] < _val:
                        _list[_pos] = _list[_pos - 1]
                        _pos = _pos - 1
                    _list[_pos] = _val
        except ValueError:
            return "Item is not a list!"
