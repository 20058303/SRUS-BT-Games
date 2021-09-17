import unittest
from app.player_bst import PlayerBST, PlayerBNode, Player

testTree = PlayerBST()
testP50 = Player("050", "50")
testP25 = Player("025", "25")
testP56 = Player("056", "56")


class MyTestCase(unittest.TestCase):
    def test_insertion(self):
        testTree.Insert(testP50)
        self.assertEqual(testTree.RootNode.player.name, testP50.name)

    def test_leftInsertion(self):
        testTree.Insert(testP25)
        self.assertEqual(testTree.RootNode.leftNode.player.name, testP25.name)

    def test_rightInsertion(self):
        testTree.Insert(testP56)
        self.assertEqual(testTree.RootNode.rightNode.player.name, testP56.name)

    def test_search(self):
        testTree.Insert(testP50)
        testTree.Insert(testP25)
        testTree.Insert(testP56)
        self.assertEqual(testTree.Search("56").player, testP56)



if __name__ == '__main__':
    unittest.main()
