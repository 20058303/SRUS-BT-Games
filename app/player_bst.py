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
            current_node = self.root_node
            while True:
                if player.name < current_node.player.name:
                    if current_node.left_node is not None:
                        current_node = current_node.left_node
                    else:
                        current_node.left_node = PlayerBNode(player)
                        break
                elif player.name > current_node.player.name:
                    if current_node.right_node is not None:
                        current_node = current_node.right_node
                    else:
                        current_node.right_node = PlayerBNode(player)
                        break
                elif player.name == current_node.player.name:
                    current_node.player = player
                    break

    def search(self, string):
        """
        Searches the Binary Tree for a player containing the name of the provided string.
        :param string: The Name to Search for
        :return: player object with relevant name if found, otherwise returns false.
        """
        if self.root_node is None:
            return False

        elif self.root_node.player.name == string:
            return self.root_node

        else:
            current_node = self.root_node
            while True:
                if current_node.player.name == string:
                    return current_node

                elif string < current_node.player.name:
                    if current_node.left_node is not None:
                        current_node = current_node.left_node
                    else:
                        return False

                elif string > current_node.player.name:
                    if current_node.right_node is not None:
                        current_node = current_node.right_node
                    else:
                        return False
