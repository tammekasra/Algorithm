

import unittest
from unittest.mock import patch
import main
import random
import Board
import copy
import numpy as np
list1 =  [1]*10000
list2 =  [2]*10000


#[[0. 0. 0. 2. 0. 0. 2.],[0. 1. 0. 1. 0. 1. 1.],[0. 1. 0. 2. 0. 2. 1.],[1. 2. 1. 2. 0. 2. 1.],[2. 1. 2. 2. 0. 1. 2.],[1. 2. 1. 1. 0. 2. 2.]]
position1 = [[0.,0., 0., 1., 0., 0., 0.],[0., 0., 0., 2., 0., 0., 0.],[0., 2., 0., 1., 0., 0., 0.],[0., 1., 0., 2., 0., 0., 0.],[0., 2., 0., 1., 0., 2., 0.],[1., 1., 2., 2., 2., 1., 1.]]

class Test(unittest.TestCase):

    @patch('builtins.input', side_effect=(list1))
    def test_using_side_effect(self, mock_input):
        for p in range(1): # We go through the game from the beginning 100 times!
            board1 = Board.board() # This is an empty board to analyze (starting board)
            for i in range(10000):
                if i > 0:
                    list1[i] = random.choice(['0','1', '2', '3', '4', '5', '6'])
            calling_4 = main.main(np.flip(position1,0)) # This a middle game position to check.
            calling_3 = main.main(board1) #This plays is when A.I plays against A.I and it should be a draw.... (but it isnt...)
            position1.clear()
            
            #calling_2 = main.main(position1)
            self.assertTrue(calling_3 == True and calling_4 == True)
    
    @patch('builtins.input', side_effect=(list2))
    def test_using_side_effect2(self, mock_input):
        for p in range(100): 
            board2 = Board.board()
            board3 = Board.board()
            for i in range(10000):
                if i > 0:
                    list2[i] = random.choice(['0','1', '2', '3', '4', '5', '6'])
            calling_3 = main.main(board3) #This plays is when A.I plays against A.I and it should be a draw.... (but it isnt...)
            calling_2 = main.main(board2) 
            position1.clear()
            
            #calling_2 = main.main(position1)
            self.assertTrue(calling_2 == True and calling_3 == True)
            

#class TestCalc(unittest.TestCase): # pythong -m unittest testing.py
   # @mock.patch('main.get_input', create=random.choice(variables))
#    def test_add(self):
#        with input(create=random.choice(variables)):
#            self.assertEqual(main.main(),True)


if __name__ == '__main__': #we can use  - python testing.py - so it works
    unittest.main()