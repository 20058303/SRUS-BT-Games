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
    def LeftNode(self, node):
        self.__leftNode = node

    @property
    def RightNode(self):
        return self.__rightNode

    @RightNode.setter
    def RightNode(self, node):
        self.__rightNode = node
