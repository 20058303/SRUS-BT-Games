# Filename      :   player_node.py
# Location      :  ./app
# Project       :   SRUS-BT-Games
# Author        :   Bradley Torpy <200583083@tafe.wa.edu.au>
# Created       :   13/08/2021
# Version       :   0.1
# Description   :
#   This is a description for the file, and I am lazy.
#


class PlayerNode:
    def __init__(self, player):
        self.player = player
        self.key = self.player.uid
        self.next = None
        self.previous = None

    @property
    def player(self):
        return self.player

    @player.setter
    def player(self, value):
        self.player = value

    @property
    def key(self):
        return self.player.uid

    @property
    def next(self):
        return self.next

    @next.setter
    def next(self, value):
        self.next = value

    @property
    def previous(self):
        return self.previous

    @previous.setter
    def previous(self, value):
        self.previous = value

    def __str__(self):
        return f"Contains {self.key}: {self.player.name}"
