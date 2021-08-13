# Filename      :   player_list.py
# Location      :  ./app
# Project       :   SRUS-BT-Games
# Author        :   Bradley Torpy <200583083@tafe.wa.edu.au>
# Created       :   13/08/2021
# Version       :   0.1
# Description   :
#   This is a description for the file, and I am lazy.
#

from app.player import Player
from app.player_node import PlayerNode

class PlayerList:
    def __init__(self):
        self.first = None
        self.last = None

    def InsertAtStart(self, id, name):
        tempNode = PlayerNode(Player(id, name))
        if self.isEmpty():
            self.first = tempNode
            self.last = tempNode
        else:
            tempNode.next = self.first
            self.first.previous = tempNode
            self.first = tempNode

    def InsertAtEnd(self, id, name):
        tempNode = PlayerNode(Player(id, name))
        if self.isEmpty():
            self.first = tempNode
            self.last = tempNode
        else:
            tempNode.previous = self.last
            self.last.next = tempNode
            self.last = tempNode

    def DeleteAtStart(self):
        if not self.isEmpty():
            self.first = self.first.next
            self.first.previous = None

    def DeleteAtEnd(self):
        if not self.isEmpty():
            self.last = self.last.previous
            self.last.next = None

    def isEmpty(self):
        if self.first is None:
            return True
        return False
