# Filename      :   player_node.py
# Location      :  ./app
# Project       :   SRUS-BT-Games
# Author        :   Bradley Torpy <200583083@tafe.wa.edu.au>
# Created       :   13/08/2021
# Version       :   0.1
# Description   :
#   This is a description for the file, and I am lazy.
#

from app.player import Player


class PlayerNode:
    def __init__(self, player):
        self.__player = player
        self.__next = None
        self.__previous = None

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, value):
        self.__player = value

    @property
    def key(self):
        return self.__player.uid

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, value):
        self.__next = value

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, value):
        self.__previous = value

    def __str__(self):
        return f"Contains {self.key}: {self.__player.name}"
