import unittest
from app.player_list import PlayerList, PlayerNode, Player


class PlayerListTestCase(unittest.TestCase):
    """
    Tests insertion and deletion of a double linked list.
    """
    def setUp(self):
        self.testList = PlayerList()
        self.testNode = PlayerNode(Player("001", "Test"))

    def test_a_isEmpty(self):
        self.assertEqual(self.testList.isEmpty(), True, "Should return True")

    def test_b_InsertStart(self):
        self.testList.InsertAtStart("001", "Test")
        self.assertEqual(self.testList.first, self.testNode)

    def test_c_DeleteStart(self):
        self.testList.DeleteAtStart()
        self.assertIsNone(self.testList.first)

    def test_d_InsertEnd(self):
        self.testList.InsertAtEnd("001", "Test")
        self.assertEqual(self.testList.last, self.testNode)

    def test_e_DeleteEnd(self):
        self.testList.DeleteAtEnd()
        self.assertIsNone(self.testList.last)


if __name__ == '__main__':
    unittest.main()
