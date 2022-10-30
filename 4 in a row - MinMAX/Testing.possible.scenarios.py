

import unittest
from unittest.mock import patch
import main
import numpy as np

''' To check if it blocks opponents winning move '''
block_in_1 = np.flip([[0,0,0,0,0,0,0],  
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0]],0)
block_in_2 = np.flip([[0,0,0,0,0,0,0],  
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,1,1,0,0,0,0]],0)
block_in_3 = np.flip([[0,0,0,0,0,0,0],  
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,1,0,0,0],
                  [2,2,2,1,2,2,2],
                  [2,2,2,1,2,2,2]],0)


''' This check if the algorithm can find a win in 2 moves'''
win2turns2 = np.flip([[0,1,2,0,0,0,0],
                    [0,0,2,1,0,0,0],
                    [0,0,2,2,0,0,0],
                    [0,0,2,1,0,2,1],
                    [1,2,1,2,2,1,2],
                    [1,1,2,1,1,1,2]],0)

''' Check if it blocks the winning move or wins straighforward'''
win_in_1_turns_1 = np.flip([[0,0,0,0,0,0,0], 
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,0,0,0,0,0,2],
                  [1,0,0,0,0,0,2],
                  [1,0,0,0,0,0,2]],0)

''' Checks if it wins vertically and diagonally!!'''
win_in_1_turns_2 = np.flip([[0,0,0,0,0,0,0],  
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0],
                  [1,0,0,0,0,0,0],
                  [1,0,0,0,2,2,2]],0)
win_in_1_turns_3 = np.flip([[0,0,0,0,0,0,0], 
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,0,0,1,2,0,0],
                  [1,0,0,1,2,2,0],
                  [1,0,0,1,1,1,2]],0)
win_in_1_turns_4 = np.flip([[0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,0,2,1,1,0,0],
                  [1,2,1,1,2,2,0],
                  [2,1,2,1,1,1,2]],0)
                
win_in_1_turns_5 = np.flip([[0,0,0,0,0,0,0],  #
                  [0,0,0,0,0,0,0],
                  [0,0,0,0,0,0,0],
                  [1,1,1,0,0,0,0],
                  [1,1,1,0,0,0,0],
                  [1,1,1,0,2,2,2]],0)

''' Checks if the position is drawn!'''
draw_in_1_turns_1 = np.flip([[0,0,2,1,2,1,1],
                            [1,2,2,2,1,1,2],
                            [2,2,1,1,2,2,1],
                            [1,1,2,2,1,1,2],
                            [2,1,2,1,2,2,1],
                            [1,1,2,2,1,2,1]],0)


''' Checks the win in 2'''
win_in_2_turns_1 = np.flip([[0,0,0,0,0,0,0], 
                            [0,0,0,0,0,0,0],
                            [0,0,2,1,0,0,0],
                            [0,0,1,2,0,0,0],
                            [0,2,2,1,0,1,0],
                            [2,2,1,2,0,2,0]],0)
''' Checks the win in 5!'''
win_in_2_turns_2 = np.flip([[0,0,0,1,0,0,1], 
                            [0,2,2,2,1,1,2],
                            [0,2,1,1,2,2,1],
                            [0,1,2,2,1,1,2],
                            [2,1,2,1,2,2,1],
                            [1,1,2,2,1,2,1]],0)





''' This gives the input values 2 as in the A.I plays with the level of 5 for each!'''
list1 =  [2,5,5]*10000 



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