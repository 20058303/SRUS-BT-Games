# Filename      :   player.py
# Location      :  ./app
# Project       :   SRUS-BT-Games
# Author        :   Bradley Torpy <200583083@tafe.wa.edu.au>
# Created       :   13/08/2021
# Version       :   0.1
# Description   :
#   This is a description for the file, and I am lazy.
#


class Player:
    def __init__(self, id, name):
        self.uid = id
        self.name = name

    def __str__(self):
        return f"{self.uid}: {self.name}"
