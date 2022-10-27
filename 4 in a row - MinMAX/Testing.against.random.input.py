

import unittest
from unittest.mock import patch
import main
import main2
import random
import Board
list1 =  [1]*10000 #This list is for the first testing code for the random input by the user (test_using_side_effect)
list2 =  [2]*10000 #This list is for the A.I (test_using_side_effect2)


how_many_turns_random = 0
how_many_turns_bad_algorithm = 0
how_many_turn_against_ai = 0

#[[0. 0. 0. 2. 0. 0. 2.],[0. 1. 0. 1. 0. 1. 1.],[0. 1. 0. 2. 0. 2. 1.],[1. 2. 1. 2. 0. 2. 1.],[2. 1. 2. 2. 0. 1. 2.],[1. 2. 1. 1. 0. 2. 2.]]
#position1 = [[0.,0., 0., 1., 0., 0., 0.],[0., 0., 0., 2., 0., 0., 0.],[0., 2., 0., 1., 0., 0., 0.],[0., 1., 0., 2., 0., 0., 0.],[0., 2., 0., 1., 0., 2., 0.],[1., 1., 2., 2., 2., 1., 1.]]



n_loops = 1 #How many times we are testing the same game over again!



class Test(unittest.TestCase):

    @patch('builtins.input', side_effect=(list1)) #This plays against random input from the user, so the A.I should win most of the time
    def test_using_side_effect(self, mock_input):
        global n_loops
        for p in range(n_loops): 
            board1 = Board.board()
            for i in range(200):
                if i > 0:
                    list1[i] = random.choice(['0','1', '2', '3', '4', '5', '6'])
            a = main.main(board1)
            calling_1 = a[0]
            global how_many_turns_random 
            how_many_turns_random += a[1]
            self.assertTrue(calling_1 == True)
    
    @patch('builtins.input', side_effect=(list2)) #This plays against A.I, an algorithm that does not try to win, but block every 4th winning slot for the A.I
    def test_using_side_effect2(self, mock_input):
        global n_loops
        for p in range(n_loops): 
            board2 = Board.board()
            for i in range(5):
                if i > 0:
                    list2[i] = random.choice(['0','1', '2', '3', '4', '5', '6'])
            a2 = main2.main(board2)
            calling_2 = a2[0] 
            global how_many_turns_bad_algorithm
            how_many_turns_bad_algorithm += a2[1]
            #calling_2 = main.main(position1)
            self.assertTrue(calling_2 == True)
    @patch('builtins.input', side_effect=(list2)) #This plays against A.I himself, but forsome reason it never ends up in a draw...
    def test_using_side_effect3(self, mock_input):
        global n_loops
        for p in range(n_loops): 
            board3 = Board.board()
            for i in range(5):
                if i > 0:
                    list2[i] = random.choice(['0','1', '2', '3', '4', '5', '6'])
            a3 = main.main(board3)
            calling_3 = a3[0]
            global how_many_turn_against_ai
            how_many_turn_against_ai += a3[1]
            
            #calling_2 = main.main(position1)
            self.assertTrue(calling_3 == True)
        print("Against random inputs, takes turns on average = ", how_many_turns_random/n_loops)
        print("Against the bad algorithm, takes turns on average = ",how_many_turns_bad_algorithm/n_loops )
        print("Against the AI, takes turns on average= ",how_many_turn_against_ai/n_loops )
    

#class TestCalc(unittest.TestCase): # pythong -m unittest testing.py
   # @mock.patch('main.get_input', create=random.choice(variables))
#    def test_add(self):
#        with input(create=random.choice(variables)):
#            self.assertEqual(main.main(),True)


if __name__ == '__main__': #we can use  - python testing.py - so it works
    unittest.main()