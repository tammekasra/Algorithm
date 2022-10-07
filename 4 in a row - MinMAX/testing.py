

import unittest
from unittest.mock import patch
import main
import random


list1 =  [0]*100

class Test(unittest.TestCase):

    @patch('builtins.input', side_effect=(list1))
    def test_using_side_effect(self, mock_input):
        for p in range(100):
            for i in range(100):
                list1[i] = random.choice(['0','1', '2', '3', '4', '5', '6'])
            calling_1 = main.main()
            self.assertTrue(calling_1 == True)

#class TestCalc(unittest.TestCase): # pythong -m unittest testing.py
   # @mock.patch('main.get_input', create=random.choice(variables))
#    def test_add(self):
#        with input(create=random.choice(variables)):
#            self.assertEqual(main.main(),True)


if __name__ == '__main__': #we can use  - python testing.py - so it works
    unittest.main()