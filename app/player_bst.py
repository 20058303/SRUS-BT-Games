"""
File:           player_bst.py
Author:         Bradley Torpy <20058303@Tafe.wa.edu.au>

Description:    This file acts as the main controller or parental class to the player binary nodes,
                or PlayerBNode class. It is able to insert, search, and balance itself.
                I understand this isn't my nicest work, so I do apologize.
"""

from app.player_bnode import PlayerBNode
from app.player import Player


class PlayerBST:
    def __init__(self):
        """
        The Parent Object or Controller for the Binary Search Tree
        as per documented requirements.
        """
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

    def to_list(self, current_node=None, current_list=None, bool_sort=True):
        """
        Converts the Binary Search Tree to an ordered list through recursive traversal.
        :param current_node: Used only for recursion. Default: None
        :param current_list: Used for recursion and persistence. Default: None
        :param bool_sort: If True, will sort the end result by it's comparison operators. Default: True
        :return: array containing PlayerBNode items.
        """

        return_list = []

        if current_list is not None:
            return_list = current_list

        if self.root_node is None:
            return None

        else:
            if current_node is None:
                current_node = self.root_node

            if current_node.left_node is not None:
                self.to_list(current_node.left_node, return_list)
            return_list.append(current_node)

            if current_node.right_node is not None:
                self.to_list(current_node.right_node, return_list)

            if bool_sort:
                return_list.sort()
            return return_list

    def balanced_sort(self, current_list=None, first_pass=True):
        """
        Balances the Binary Search Tree by using a sorted array of PlayerBNodes, and recursively
        assigning the middle of the halved list to the current node.
        :param first_pass: Used to assign the root_node of this BST class on it's first iteration.
        :param current_list: The list of PlayerBNode objects that gets passed down the recursion
        :return: the PlayerBNode that will be assigned to the object one recursion higher.
        """

        if not current_list:
            return None

        middle_value = len(current_list) // 2
        set_node = current_list[middle_value]

        set_node.left_node = self.balanced_sort(current_list[:middle_value], False)
        set_node.right_node = self.balanced_sort(current_list[middle_value+1:], False)

        if first_pass:
            self.root_node = set_node

        return set_node
