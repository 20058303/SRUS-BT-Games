from app.player import Player


class PlayerBNode:
    def __init__(self, player):
        self.__player = player
        self.__left_node = None
        self.__right_node = None

    @property
    def player(self):
        return self.__player

    @property
    def left_node(self):
        return self.__left_node

    @left_node.setter
    def left_node(self, node):
        self.__left_node = node

    @property
    def right_node(self):
        return self.__right_node

    @right_node.setter
    def right_node(self, node):
        self.__right_node = node
