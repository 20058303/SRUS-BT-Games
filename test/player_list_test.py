import unittest
from app.player_list import PlayerList, PlayerNode, Player


class PlayerListTestCase(unittest.TestCase):
    def test_isEmpty(self):
        testList = PlayerList()
        self.assertEqual(testList.isEmpty(), True, "Should return True")
        testList.InsertAtStart("001", "Test")
        self.assertEqual(testList.isEmpty(), False, "Should return False")

    def test_InsertStart(self):
        testNode = PlayerNode(Player("001", "Test"))
        testList = PlayerList()
        testList.InsertAtStart("001", "Test")
        self.assertEqual(testList.first.key, testNode.key)

    def test_InsertEnd(self):
        testNode = PlayerNode(Player("001", "Test"))
        testList = PlayerList()
        testList.InsertAtEnd("001", "Test")
        self.assertEqual(testList.last.key, testNode.key)

    def test_DeleteStart(self):
        testList = PlayerList()
        testList.InsertAtStart("001", "Test1")
        testList.DeleteAtStart()
        self.assertIsNone(testList.first)

    def test_DeleteEnd(self):
        testList = PlayerList()
        testList.InsertAtStart("001", "Test1")
        testList.DeleteAtEnd()
        self.assertIsNone(testList.last)


if __name__ == '__main__':
    unittest.main()
