




import Board
import random
import minmax
import math
import time
import bad_algorithm
x_axis = Board.x_axis # determine the length of the rows
y_axis  = Board.y_axis # determine the length of the columns
 





def main(board):    

    ''' From here we see how many turns it takes for each A.I - each loop is 1 turn ''' 
    how_many_turns = 0

    '''This print the empty board '''
    Board.print_board(board)

    ''' We have to end the game if the loop stops'''
    end_of_the_game = True
    turn = 0
    Time_list = []
    another_algorithm_tofight_against_AI = int(input("Please select player(1) or a bot against the A.I (2) or bad algorithm (3) "))

    first_ai_level = 5
    second_ai_level = 5
    if another_algorithm_tofight_against_AI != 1 and another_algorithm_tofight_against_AI != 3 :
        first_ai_level= int(input("Select level of the first A.I - from 1-9:  "))
        second_ai_level= int(input("Select level of the second A.I - from 1-9:  "))
    while end_of_the_game: #If we reach to either a winning or a loosing position, we are going to put end_of_the_game as false
        if minmax.end_state(board):
            return (True,how_many_turns)
        how_many_turns += 1
        if turn == 0:
            if another_algorithm_tofight_against_AI == 1:
                move = int(input("Player 1, Make your Selection(0-6):  "))                
                if Board.is_valid(board,move): #Is_valid move checks if the move can be played or not (if is it over the select column or not which is 6)
                    row = Board.get_next_open_row(board,move) #We will fetch the desired row where we can to insert our coin - since the number of the row will change everytime
                    Board.move(board,row,move,1) #We insert the wanted move
            #      Board.print_board(board)
                    if minmax.win(board, 1): #We check if it is a winning game!
                                return (False,how_many_turns)   # We return false if and only if the player 1 wins (A.I has to either win or get a draw), we need to modify something if the test comes out as negative!

            if another_algorithm_tofight_against_AI == 2:
                    
                    moves = [0,1,2,3,4,5,6]
                    move = random.choice(moves)
                    if Board.is_valid(board,move) == False:
                        continue
                    start = time.time()
                    move2 = minmax.minimax(board, first_ai_level, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
                    end = time.time()
                # print(move2) #- we can check the moves if we have bug....
                    Time_list.append([(how_many_turns/2),(move2),(end-start)])
                    move = move2[0]
                    row = Board.get_next_open_row(board,move)
                    Board.move(board,row,move,1)
                    if minmax.win(board, 1):
                        Board.print_board(board)
                        print("Player 2 wins!")
                        end_of_the_game = False
                        print(Time_list)
                        return (True,how_many_turns) #we want our test to get a true answer!
            if another_algorithm_tofight_against_AI == 3:
                moves = [0,1,2,3,4,5,6]
                move2 = random.choice(moves)
                a = bad_algorithm.players_next_move(board)

                if a == -10:
                    move = move2

                
                if Board.is_valid(board,move): #Is_valid move checks if the move can be played or not (if is it over the select column or not which is 6)
                    row = Board.get_next_open_row(board,move) #We will fetch the desired row where we can to insert our coin - since the number of the row will change everytime
                    Board.move(board,row,move,1) #We insert the wanted move

                    if minmax.win(board, 1): #We check if it is a winning game!
                            return (False,how_many_turns)
                                

                
            Board.print_board(board) 

            ''' This is an easy way to keep track on whos turn is it, if turn 2, we degrade it to 0, and if 0, then 1 '''
            turn += 1
            turn = turn % 2
        
          
                

            

        else: #The A.I (sort of)
            moves = [0,1,2,3,4,5,6]
            move = random.choice(moves)
            if Board.is_valid(board,move) == False:
                continue
            start = time.time()
            move2 = minmax.minimax(board, second_ai_level, -math.inf, math.inf, True,move) #Get the best move using MINIMAX algorithm!
            end = time.time()
           # print(move2) #- we can check the moves if we have bug....
            Time_list.append([(how_many_turns/2),(move2),(end-start)])
            move = move2[0]
            eval = move2[1]
            row = Board.get_next_open_row(board,move)
            Board.move(board,row,move,2)
            if math.isinf(eval):
                if minmax.win(board, 2):
                    Board.print_board(board)
                    print("Player 2 wins!")
                    end_of_the_game = False
                    print(Time_list)
                    return (True,how_many_turns) #we want our test to get a true answer!
                
            Board.print_board(board)
            

         
                
            turn += 1
            turn = turn % 2




    

        
