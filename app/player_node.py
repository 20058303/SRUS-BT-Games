"""
File:           player_node.py
Author:         Bradley Torpy <20058303@Tafe.wa.edu.au>

Description:    Player Node class to be used with double linked list, containing the player class object within.
"""

from app.player import Player


class PlayerNode:
    def __init__(self, player):
        """
        Creates a node for a doubly linked list, containing a player object.
        :param player: Player object to be contained within this node.
        """
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

    def __eq__(self, other):
        if self.player.name == other.player.name and \
                self.player.uid == other.player.uid:
            return True

    def __str__(self):
        return f"Contains {self.key}: {self.__player.name}"
