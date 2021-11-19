import unittest
from app.player import Player
from argon2 import PasswordHasher

ph = PasswordHasher()


class PlayerTestCase(unittest.TestCase):
    def setUp(self):
        self.testClass1 = Player("001", "Test Name")
        self.testClass2 = Player("002", "Another Name")
        self.testClass3 = Player("003", "Third Name")
        self.testClass4 = Player("004", "Fourth Name")
        self.testHash = ph.hash("TestPassword")

    def test_a_UID(self):
        test_uid = "001"
        self.assertEqual(self.testClass1.uid, test_uid, f"Should Read {test_uid}")

    def test_b_Name(self):
        test_name = "Test Name"
        self.assertEqual(self.testClass1.name, test_name, f"Should Read {test_name}")

    def test_c_addPassword(self):
        self.testClass1.add_password("TestPassword")
        self.assertTrue(self.testClass1.verify_password("TestPassword"))

    def test_d_verifyPassword(self):
        self.testClass1.add_password("TestPassword")
        self.assertTrue(self.testClass1.verify_password("TestPassword"))
        self.assertFalse(self.testClass1.verify_password("IncorrectPassword"))

    def test_e_comparison(self):
        self.testClass1.score = 4
        self.testClass2.score = 2
        self.assertTrue(self.testClass1 > self.testClass2)

    def test_f_insertionSort(self):
        self.testClass1.score = 4
        self.testClass2.score = 2
        self.testClass3.score = 3
        self.testClass4.score = 1

        test_list = [self.testClass1, self.testClass2, self.testClass3, self.testClass4]
        Player.InsertionSorting(test_list)
        self.assertEqual(test_list[0].score, 4)  # Checks if first listed player has the highest score
        self.assertLessEqual(test_list[3], test_list[0])  # Checks if last player in list has lower score than the first


if __name__ == '__main__':
    unittest.main()
