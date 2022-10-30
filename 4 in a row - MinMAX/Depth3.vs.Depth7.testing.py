



import unittest
from unittest.mock import patch
import testing_A_I_with_3_loops_vs_7
import numpy as np



''' 2 is the input where we can to select A.I, 3 is the depth of the weaker A.I and 7 is the depth of the stronger ai'''
list1 =  [2,3,7]*10000 


'''n-loops is the number of games played '''
n_loops = 1

''' This is a build in case'''
class Test(unittest.TestCase):
    '''This builints.input function helps us to put in desired input from the list1 we gave '''
    @patch('builtins.input', side_effect=(list1)) 
    def test_using_side_effect4(self, mock_input):
        global n_loops

        ''' The time each A.I takes'''
        time_weaker_Ai = 0
        time_stronger_Ai = 0

        '''We check how many times we loose or win '''
        draw_or_loose = 0
        win_for_AI = 0

        '''loop is for how many times we want to go through the same analysis, each game takes around 2 min '''
        for p in range(n_loops): 

            '''We draw the numpy array because it is suggested to be faster than lists '''
            board3 = np.zeros((6,7)) 

            ''' We initiate the function of the minmax '''
            a3 = testing_A_I_with_3_loops_vs_7.main(board3)

            '''The result whether AI won == True or lost (or even draw) == False '''
            calling_3 = a3[0]

            ''' If calling3 == Stronger AI wins it increases the won value by one and if the it is loosing or draw then it increases that '''
            if calling_3 ==  True:
                win_for_AI += 1
            else:
                draw_or_loose +=1

            '''This returns the time from each ai '''
            time_weaker_Ai += (a3[1])
            time_stronger_Ai += (a3[2])

            '''Self assert is true is the unittest own command where it checks a certain output whether is true or false '''
            self.assertTrue(calling_3 == True or calling_3 == False )

        '''We want to print out the number of moves made and how many times each of the AI won '''

        print("Number of games drawn or won by the weaker A.i ", draw_or_loose,time_weaker_Ai/n_loops, "Number of games won by the best A.I ", win_for_AI ,time_stronger_Ai/n_loops )


""" This is just to initiate the main function and can be also used via command shell"""
if __name__ == '__main__': 
    unittest.main()