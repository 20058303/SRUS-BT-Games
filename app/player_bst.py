from app.player_bnode import PlayerBNode
from app.player import Player


class PlayerBST:
    def __init__(self):
        self.root_node = None

    def insert(self, player):
        """
        Inserts Player object within the Binary Tree.
        :param player: Player Object to be added.
        :return: None
        """
        if self.root_node is None:
            self.root_node = PlayerBNode(player)
        else:
            self.root_node.insert(player)

    def search(self, string):
        """
        Searches the Binary Tree for a player containing the name of the provided string.
        :param string: The Name to Search for
        :return: player object with relevant name if found, otherwise returns false.
        """
        if self.root_node is None:
            return None
        elif self.root_node.player.name == string:
            return self.root_node
        else:
            return self.root_node.search(string)

    def to_list(self, current_node=None, current_list=None):
        """
        Displays the Tree's players as a stringed list.
        :return: string
        """

        return_list = []

        if current_list is not None:
            return_list = current_list

        if self.root_node is None:
            return "Empty BST"

        else:
            if current_node is None:
                current_node = self.root_node

            if current_node.left_node is not None:
                self.to_list(current_node.left_node, return_list)
            return_list.append(current_node)

            if current_node.right_node is not None:
                self.to_list(current_node.right_node, return_list)

            return_list.sort()
            return return_list

    def b_sort(self, current_list=None):
        """
        :param current_list:
        :return:
        """

        if not current_list:
            return None

        middle_value = int(len(current_list) / 2)

        current_node = current_list[middle_value]

        if current_list[middle_value-1]:
            current_node.left_node = current_list[middle_value-1]
            current_node.left_node.b_sort(current_list[:middle_value-1])
        if current_list[middle_value+1]:
            current_node.right_node = current_list[middle_value+1]
            current_node.right_node.b_sort(current_list[middle_value+1:])

        self.root_node = current_node


if __name__ == "__main__":
    testTree = PlayerBST()
    testTree.insert(Player("5", "5"))
    testTree.insert(Player("2", "2"))
    testTree.insert(Player("6", "6"))
    testTree.insert(Player("3", "3"))
    testTree.insert(Player("7", "7"))
    testTree.insert(Player("13", "13"))
    testTree.insert(Player("11", "11"))
    testTree.insert(Player("18", "18"))
    testTree.insert(Player("10", "10"))

    for i in testTree.to_list():
        print(i)

    testTree.b_sort(testTree.to_list())

