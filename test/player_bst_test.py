import unittest
from app.player_bst import PlayerBST, PlayerBNode, Player

testTree = PlayerBST()
testP50 = Player("050", "50")
testP25 = Player("025", "25")
testP56 = Player("056", "56")


class MyTestCase(unittest.TestCase):
    """
    Completely outdated test cases - will correct later.
    """
    def setUp(self):
        self.testTree = PlayerBST()
        self.testTree.insert(Player("050", "50"))
        self.testTree.insert(Player("025", "25"))
        self.testTree.insert(Player("056", "56"))

    def test_correct_insertion(self):
        self.assertEqual(self.testTree.root_node.player.name, "50")
        self.assertEqual(self.testTree.root_node.left_node.player.name, "25")
        self.assertEqual(self.testTree.root_node.right_node.player.name, "56")

    def test_search(self):
        self.assertEqual(self.testTree.root_node, self.testTree.search('50'))
        self.assertEqual(self.testTree.root_node.left_node, self.testTree.search('25'))

    def test_display(self):
        print(self.testTree)


if __name__ == '__main__':
    unittest.main()
