import unittest
import main


class TestCalc(unittest.TestCase):

    def test_add(self):
        result = main()
        self.assertEqual(result,"Player 2 wins!")


