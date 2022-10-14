



import unittest
from unittest.mock import patch
import main_testing
import random
import Board
import copy
import numpy as np


list1 =  [1]*10000 #This list is for the first testing code for the random input by the user (test_using_side_effect)



n_loops = 1

class Test(unittest.TestCase):
    @patch('builtins.input', side_effect=(list1)) #This plays against A.I himself, but forsome reason it never ends up in a draw...
    def test_using_side_effect4(self, mock_input):
        global n_loops
        for p in range(n_loops): 
            board3 = Board.board()
            a3 = main_testing.main(board3)
            calling_3 = a3[0]
            global how_many_turn_against_ai
            how_many_turn_against_ai += a3[1]
            self.assertTrue(calling_3 == True)
if __name__ == '__main__': #we can use  - python testing.py - so it works
    unittest.main()