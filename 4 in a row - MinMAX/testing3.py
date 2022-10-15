



import unittest
from unittest.mock import patch
import testing_A_I_with_3_loops_vs_7
import Board
import time
import numpy as np

#Testing 3 idea is to see whether increasing the numbers of loops (how deep the minimax goes) and can it win a minimax with only 3 loops...


list1 =  [2]*10000 #This list is for the first testing code for the random input by the user (test_using_side_effect)



n_loops = 20

class Test(unittest.TestCase):
    @patch('builtins.input', side_effect=(list1)) #This plays against A.I himself, but forsome reason it never ends up in a draw...
    def test_using_side_effect4(self, mock_input):
        global n_loops
        time_weaker_Ai = 0
        time_stronger_Ai = 0
        draw_or_loose = 0
        win_for_AI = 0
        for p in range(n_loops): 
            board3 = Board.board()
            a3 = testing_A_I_with_3_loops_vs_7.main(board3)
            calling_3 = a3[0]
            if calling_3 ==  True:
                win_for_AI += 1
            else:
                draw_or_loose +=1
            print(a3)
            time_weaker_Ai += (a3[1])
            time_stronger_Ai += (a3[2])
            self.assertTrue(calling_3 == True or calling_3 == False )
        print("Number of games drawn or won by the weaker A.i ", draw_or_loose,time_weaker_Ai/n_loops, "Number of games won by the best A.I ", win_for_AI ,time_stronger_Ai/n_loops )
if __name__ == '__main__': #we can use  - python testing.py - so it works
    unittest.main()