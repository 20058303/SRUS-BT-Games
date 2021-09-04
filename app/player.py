# Filename      :   player.py
# Location      :  ./app
# Project       :   SRUS-BT-Games
# Author        :   Bradley Torpy <200583083@tafe.wa.edu.au>
# Created       :   13/08/2021
# Version       :   0.1
# Description   :
#   A class file for the player object.
#
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
        self.__score = value

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
