

import unittest
from unittest.mock import patch
import main
import random
import numpy as np

'''This select random moves '''
list1 =  [1]*200 

''' This picks to fight against the bad algorithm (the one who only blocks the winning moves)'''
list2 =  [2,5,5]*200 

''' This picks to fight himself! '''
list3 = [3,5,5]*200


''' We check how many turns it took to win one or either!'''
how_many_turns_random = 0
how_many_turns_bad_algorithm = 0
how_many_turn_against_ai = 0

#[[0. 0. 0. 2. 0. 0. 2.],[0. 1. 0. 1. 0. 1. 1.],[0. 1. 0. 2. 0. 2. 1.],[1. 2. 1. 2. 0. 2. 1.],[2. 1. 2. 2. 0. 1. 2.],[1. 2. 1. 1. 0. 2. 2.]]
#position1 = [[0.,0., 0., 1., 0., 0., 0.],[0., 0., 0., 2., 0., 0., 0.],[0., 2., 0., 1., 0., 0., 0.],[0., 1., 0., 2., 0., 0., 0.],[0., 2., 0., 1., 0., 2., 0.],[1., 1., 2., 2., 2., 1., 1.]]



n_loops = 1 #How many times we are testing the same game over again!



class Test(unittest.TestCase):

    '''This plays someone who plays completely randomly! '''

    @patch('builtins.input', side_effect=(list1)) 
    def test_using_side_effect(self, mock_input):
        global n_loops

        ''' We '''
        for p in range(n_loops): 
            board1 = np.zeros((6,7)) 
            for i in range(200):
                if i > 0:
                    list1[i] = random.choice(['0','1', '2', '3', '4', '5', '6'])
            '''We go through the minmax using random varaibles '''

            a = main.main(board1)

            '''How many turns it took! '''
            calling_1 = a[0]
            global how_many_turns_random 
            how_many_turns_random += a[1]

            ''' To see if it comes back as either won or drawn!'''
            self.assertTrue(calling_1 == True)
    
    @patch('builtins.input', side_effect=(list3)) 
    def test_using_side_effect2(self, mock_input):
        global n_loops
        for p in range(n_loops): 
            board2 =  np.zeros((6,7)) 
            for i in range(100):
                if i > 2:
                    list2[i] = random.choice(['0','1', '2', '3', '4', '5', '6'])

            ''' Number of moves against the bad algorithm!! '''
            a2 = main.main(board2)
            calling_2 = a2[0] 
            global how_many_turns_bad_algorithm
            how_many_turns_bad_algorithm += a2[1]


            ''' To see if it comes back as either won or drawn!'''
            self.assertTrue(calling_2 == True)
    @patch('builtins.input', side_effect=(list2)) 
    def test_using_side_effect3(self, mock_input):
        global n_loops
        for p in range(n_loops): 
            board3 =  np.zeros((6,7)) 
            for i in range(5):
                if i > 2:
                    list2[i] = random.choice(['0','1', '2', '3', '4', '5', '6'])
            a3 = main.main(board3)
            calling_3 = a3[0]
            global how_many_turn_against_ai
            how_many_turn_against_ai += a3[1]
            
            ''' To see if it comes back as either won or drawn!'''
            self.assertTrue(calling_3 == True)
        print("Against random inputs, takes turns on average = ", how_many_turns_random/n_loops)
        print("Against the bad algorithm, takes turns on average = ",how_many_turns_bad_algorithm/n_loops )
        print("Against the AI, takes turns on average= ",how_many_turn_against_ai/n_loops )
    



if __name__ == '__main__': 
    unittest.main()