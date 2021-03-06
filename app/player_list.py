"""
File:           player_list.py
Author:         Bradley Torpy <20058303@Tafe.wa.edu.au>

Description:    A double linked list system used for storing player data within nodes. Will be replaced with a
                balanced binary tree. Allows for insertion at both the start and end.
"""

from app.player import Player
from app.player_node import PlayerNode


class PlayerList:
    def __init__(self):
        """
        Double Linked List used to store and hold Player Information.
        """
        self.__first = None
        self.__last = None

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, value=None):
        self.__first = value

    @property
    def last(self):
        return self.__last

    @last.setter
    def last(self, value=None):
        self.__last = value

    def InsertAtStart(self, id, name):
        """
        Inserts a player object at the start of the player list.
        :param id: ID associated with the player object
        :param name: Name associated with the player object
        """

        tempNode = PlayerNode(Player(id, name))
        if self.isEmpty():
            self.first = tempNode
            self.last = tempNode
        else:
            tempNode.next = self.first
            self.first.previous = tempNode
            self.first = tempNode

    def InsertAtEnd(self, id, name):
        """
        Inserts a player object at the end of the player list.
        :param id: ID associated with the player object
        :param name: Name associated with the player object
        """

        tempNode = PlayerNode(Player(id, name))
        if self.isEmpty():
            self.first = tempNode
            self.last = tempNode
        else:
            tempNode.previous = self.last
            self.last.next = tempNode
            self.last = tempNode

    def DeleteAtStart(self):
        """
        Deletes the first player object within the player list.
        """

        if not self.isEmpty():
            if self.first.next is not None:
                self.first = self.first.next
                self.first.previous = None
            else:
                self.first = None
                self.last = None

    def DeleteAtEnd(self):
        """
        Deletes the last player object within the player list.
        """

        if not self.isEmpty():
            if self.last.previous is not None:
                self.last = self.last.previous
                self.last.next = None
            else:
                self.first = None
                self.last = None

    def DeleteWithKey(self, key):
        """
        Deletes the first instance of a player object with the key provided.
        :param key: The key you wish to search for.
        """

        if not self.isEmpty():
            currentNode = self.first
            while True:
                if currentNode.key == key:
                    if currentNode == self.first:
                        self.DeleteAtStart()
                        break

                    elif currentNode == self.last:
                        self.DeleteAtEnd()
                        break
                    else:
                        currentNode.previous.next = currentNode.next
                        currentNode.next.previous = currentNode.previous
                        break

                elif currentNode.next is not None:
                    currentNode = currentNode.next
                else:
                    print(f"No players with '{key}' found.")
                    break

    def isEmpty(self):
        """
        Checks if the player list is empty.
        """
        if self.first is None:
            return True
        return False

    def DisplayList(self, forward=True):
        """
        Displays the player list in a user-friendly format.
        :param forward: If True, will display the list from the start (Boolean)
        """

        counter = 0
        s = ""
        if not self.isEmpty():
            if forward:
                currentNode = self.first
            else:
                currentNode = self.last

            while True:
                counter += 1
                s += f"{currentNode.player}\n"
                if (forward and currentNode.next is None) or (not forward and currentNode.previous is None):
                    break
                elif forward:
                    currentNode = currentNode.next
                else:
                    currentNode = currentNode.previous
            return f"{counter} Players:\n" + s
        else:
            return "No players listed."
