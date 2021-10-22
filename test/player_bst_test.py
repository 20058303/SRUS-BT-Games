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
    def test_insertion(self):
        testTree.insert(testP50)
        self.assertEqual(testTree.root_node.player.name, testP50.name)

    def test_leftInsertion(self):
        testTree.insert(testP25)
        self.assertEqual(testTree.root_node.left_node.player.name, testP25.name)

    def test_rightInsertion(self):
        testTree.insert(testP56)
        self.assertEqual(testTree.root_node.right_node.player.name, testP56.name)

    def test_search(self):
        testTree.insert(testP50)
        testTree.insert(testP25)
        testTree.insert(testP56)
        self.assertEqual(testTree.search("56").player, testP56)


if __name__ == '__main__':
    unittest.main()
