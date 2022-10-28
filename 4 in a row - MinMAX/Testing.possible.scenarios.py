

import unittest
from unittest.mock import patch
import main
import numpy as np


block_in_1 = np.flip([[0,0,0,0,0,0,0],  #To check if it blocks opponents winning move
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0]],0)
block_in_2 = np.flip([[0,0,0,0,0,0,0],  #To check if it blocks opponents winning move
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,1,1,0,0,0,0]],0)
block_in_3 = np.flip([[0,0,0,0,0,0,0],  #To check if it blocks opponents winning move
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,1,0,0,0],
                  [2,2,2,1,2,2,2],
                  [2,2,2,1,2,2,2]],0)

win2turns2 = np.flip([[0,1,2,0,0,0,0],
                    [0,0,2,1,0,0,0],
                    [0,0,2,2,0,0,0],
                    [0,0,2,1,0,2,1],
                    [1,2,1,2,2,1,2],
                    [1,1,2,1,1,1,2]],0)

win_in_1_turns_1 = np.flip([[0,0,0,0,0,0,0],  #This check upwards if it fins the correct move!
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,0,0,0,0,0,2],
                  [1,0,0,0,0,0,2],
                  [1,0,0,0,0,0,2]],0)
win_in_1_turns_2 = np.flip([[0,0,0,0,0,0,0],  #This check if the minimax algorithm fins winning move vertically
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0],
                  [1,0,0,0,2,2,2]],0)
win_in_1_turns_3 = np.flip([[0,0,0,0,0,0,0], #This check if the minimax algorithm fins winning move diagonally
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,0,0,1,2,0,0],
                  [1,0,0,1,2,2,0],
                  [1,0,0,1,1,1,2]],0)
win_in_1_turns_4 = np.flip([[0,0,0,0,0,0,0], ##This check if the minimax algorithm fins winning move diagonally
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,0,2,1,1,0,0],
                  [1,2,1,1,2,2,0],
                  [2,1,2,1,1,1,2]],0)
                
win_in_1_turns_5 = np.flip([[0,0,0,0,0,0,0],  #This check if the minimax algorithm fins winning move vertically
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,1,1,0,0,0,0],
                  [1,1,1,0,0,0,0],
                  [1,1,1,0,2,2,2]],0)
draw_in_1_turns_1 = np.flip([[0,0,2,1,2,1,1], # This check if the positions is drawn 
                            [1,2,2,2,1,1,2],
                            [2,2,1,1,2,2,1],
                            [1,1,2,2,1,1,2],
                            [2,1,2,1,2,2,1],
                            [1,1,2,2,1,2,1]],0)

win_in_2_turns_1 = np.flip([[0,0,0,0,0,0,0], ##This check if the minimax algorithm finds the winning move in 2
                            [0,0,0,0,0,0,0],
                            [0,0,2,1,0,0,0],
                            [0,0,1,2,0,0,0],
                            [0,2,2,1,0,1,0],
                            [2,2,1,2,0,2,0]],0)
win_in_2_turns_2 = np.flip([[0,0,0,1,0,0,1], # This checks if it find the winning move with 5
                            [0,2,2,2,1,1,2],
                            [0,2,1,1,2,2,1],
                            [0,1,2,2,1,1,2],
                            [2,1,2,1,2,2,1],
                            [1,1,2,2,1,2,1]],0)





list1 =  [2,5,5]*10000 #This list is for the first testing code for the random input by the user (test_using_side_effect)



n_loops = 1
class Test(unittest.TestCase):

    @patch('builtins.input', side_effect=(list1)) #Check if the algorithms finds all winning moves in 1!
    def test_using_side_effect(self, mock_input):
        global n_loops
        for p in range(n_loops): 
            board1 = win_in_1_turns_1[:]
            board2 = win_in_1_turns_2[:]
            board3 = win_in_1_turns_3[:]
            board4 = win_in_1_turns_4[:]
            board5 = draw_in_1_turns_1[:]
            board6 = win_in_1_turns_5[:]
            board7 = block_in_1[:]
            a = main.main(board1)
            a2 = main.main(board2)
            a3 = main.main(board3)
            a4 = main.main(board4)
            a5 = main.main(board5)
            a6 = main.main(board6)
            a7 = main.main(board7)
            calling_1 = a[0]
            calling_2 = a2[0]
            calling_3 = a3[0]
            calling_4 = a4[0]
            calling_5 = a5[0]
            calling_6 = a6[0]
            calling_7 = a7[0]
            self.assertTrue(calling_7 == True and calling_1 == True and calling_2 == True and calling_3 == True and calling_4 == True and calling_5 == True and calling_6 == True)
    @patch('builtins.input', side_effect=(list1)) #Check if the algorithms finds all winning moves in 2!
    def test_using_side_effect2(self, mock_input):
        global n_loops
        for p in range(n_loops): 
            print("-----------------------------------------------------------------")
            board1 = win_in_2_turns_1[:]
            board2 = win_in_2_turns_2[:]
            a = main.main(board1)
            a2 = main.main(board2)
            calling_1 = a[0]
            calling_2 = a2[0]
            self.assertTrue(calling_1 == True and calling_2 == True) # and calling_3 == True and calling_4 == True)


    @patch('builtins.input', side_effect=(list1)) #Check if the algorithms finds all winning moves in 5!
    def test_using_side_effect3(self, mock_input):
        global n_loops
        for p in range(n_loops): 
            print("-----------------------------------------------------------------")
            board1 = win_in_2_turns_1[:]
            board2 = win_in_2_turns_2[:]
            a = main.main(board1)
            a2 = main.main(board2)
            calling_1 = a[0]
            calling_2 = a2[0]
            self.assertTrue(calling_1 == True and calling_2 == True) # and calling_3 == True and calling_4 == True)

if __name__ == '__main__': #we can use  - python testing.py - so it works
    unittest.main()