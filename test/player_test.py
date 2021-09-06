import unittest
from app.player import Player
from argon2 import PasswordHasher

ph = PasswordHasher()
testClass = Player("001", "Test Name")
testClass2 = Player("002", "Another Name")
testClass3 = Player("003", "Third Name")
testClass4 = Player("004", "Fourth Name")
testHash = ph.hash("TestPassword")


class PlayerTestCase(unittest.TestCase):
    def testUID(self):
        test_UID = "001"
        self.assertEqual(testClass.uid, test_UID, f"Should Read {test_UID}")

    def testName(self):
        test_name = "Test Name"
        self.assertEqual(testClass.name, test_name, f"Should Read {test_name}")

    def test_addPassword(self):
        testClass.add_password("TestPassword")
        self.assertTrue(testClass.verify_password("TestPassword"))

    def test_verifyPassword(self):
        self.assertTrue(testClass.verify_password("TestPassword"))
        self.assertFalse(testClass.verify_password("IncorrectPassword"))

    def test_comparison(self):
        testClass.score = 4
        testClass2.score = 2
        self.assertTrue(testClass > testClass2)

    def test_insertionSort(self):
        testClass.score = 4
        testClass2.score = 2
        testClass3.score = 3
        testClass4.score = 1

        testList = [testClass, testClass2, testClass3, testClass4]
        Player.InsertionSorting(testList)
        self.assertEqual(testList[0].score, 4)  # Checks if first listed player has the highest score
        self.assertLessEqual(testList[3], testList[0])   # Checks if last player in list has lower score than the first


if __name__ == '__main__':
    unittest.main()
