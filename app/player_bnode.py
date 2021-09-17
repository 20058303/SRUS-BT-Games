from app.player import Player


class PlayerBNode:
    def __init__(self, player):
        self.__player = player
        self.__leftNode = None
        self.__rightNode = None

    @property
    def player(self):
        return self.__player

    @property
    def leftNode(self):
        return self.__leftNode

    @leftNode.setter
    def leftNode(self, node):
        self.__leftNode = node

    @property
    def rightNode(self):
        return self.__rightNode

    @rightNode.setter
    def rightNode(self, node):
        self.__rightNode = node
