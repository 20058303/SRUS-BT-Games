# Filename      :   player.py
# Location      :  ./app
# Project       :   SRUS-BT-Games
# Author        :   Bradley Torpy <200583083@tafe.wa.edu.au>
# Created       :   13/08/2021
# Version       :   0.1
# Description   :
#   A class file for the player object.
#


class Player:
    def __init__(self, id, name):
        """
        The player object.
        :param id: Unique Identifier for the player.
        :param name: The name of the player.
        """
        self.uid = id
        self.name = name

    def __str__(self):
        return f"{self.uid}: {self.name}"
