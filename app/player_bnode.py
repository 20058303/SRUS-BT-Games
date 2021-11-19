from app.player import Player


class PlayerBNode:
    def __init__(self, player):
        self.__player = player
        self.__left_node = None
        self.__right_node = None

    def insert(self, player):
        """
        Inserts Player object within the Binary Tree.
        :param player: Player Object to be added.
        :return: None
        """
        if player.name < self.player.name:
            if self.left_node is not None:
                self.left_node.insert(player)
            else:
                self.left_node = PlayerBNode(player)
        elif player.name > self.player.name:
            if self.right_node is not None:
                self.right_node.insert(player)
            else:
                self.right_node = PlayerBNode(player)
        else:
            self.player = player

    def search(self, string):
        """
        Searches the Binary Tree for a player containing the name of the provided string.
        :param string: The Name to Search for
        :return: player object with relevant name if found, otherwise returns false.
        """
        if string < self.player.name:
            if self.left_node is not None:
                return self.left_node.search(string)
        elif string > self.player.name:
            if self.right_node is not None:
                return self.right_node.search(string)
        elif self.player.name == string:
            return self
        else:
            return None

    def b_sort(self, current_list=None):
        """
        :param current_list:
        :return:
        """

        if not current_list:
            return None

        middle_value = int(len(current_list) / 2)

        try:
            if current_list[middle_value-1]:
                self.left_node = current_list[middle_value-1]
                self.left_node.b_sort(current_list[:middle_value-1])
            if current_list[middle_value+1]:
                self.right_node = current_list[middle_value+1]
                self.right_node.b_sort(current_list[middle_value+1:])
        except IndexError:
            return None

    @property
    def player(self):
        return self.__player

    @player.setter
    def player(self, p):
        self.__player = p

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

    def __ge__(self, other):
        return self.player.name >= other.player.name

    def __lt__(self, other):
        return self.player.name < other.player.name

    def __str__(self):
        return f"{self.player.name}"
