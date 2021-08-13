import unittest
from app.player import Player

testClass = Player("001", "Test Name")


class PlayerTestCase(unittest.TestCase):
    def testUID(self):
        test_UID = "001"
        self.assertEqual(testClass.uid, test_UID, f"Should Read {test_UID}")

    def testName(self):
        test_name = "Test Name"
        self.assertEqual(testClass.name, test_name, f"Should Read {test_name}")


if __name__ == '__main__':
    unittest.main()
