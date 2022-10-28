


''' This just evalutes the position if we dont win nor loose, so we just give a score how much are we winning or loosing'''
def evaluate(row, piece):
    evualuation = 0  #not sure if it correct or not.... but the idea is that we evaluate how many free slots are in each row, column and diagonal
    if piece == 2:
        opponent = 1
    else:
        opponent = 2


    '''if our opponent has a winning slot, we need to stop it, so the position is -4 '''
    if row.count(opponent) == 3 and row.count(0) == 1: 
        evualuation -= 4

    ''' if we have two slots free, we increase the value a little bit by 2 '''
    if row.count(piece) == 2 and row.count(0) == 2: 
        evualuation += 2

    '''if there 3 in a row and 1 free slot, we choose it and give it a score of 5 '''
    if row.count(piece) == 3 and row.count(0) == 1: 
        evualuation += 5

    ''' If we obvisouly have 4 in a row, then we have won! So maximum score  '''
    if row.count(piece) == 4: 
        evualuation += 100

    return evualuation

def score(board, column):
    

    points = 0
    middle = [int(j) for j in list(board[:, 7//2])]
    amount = middle.count(column)
    points += amount * 3

    
    for r in range(6):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(4):
            row = row_array[c:c+4] #we get the whole column of 4 so we can evaluate it in evaluate function!
            points += evaluate(row, column)
    for c in range(7):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(3):
            row = col_array[r:r+4] #we get the whole row of 4 so we can evaluate it in evaluate function!
            points += evaluate(row, column)
    for r in range(3):
        for c in range(4):
            row = [board[r+i][c+i] for i in range(4)] #we get the whole vertical to the right of 4 so we can evaluate it in evaluate function!
            points += evaluate(row, column)
    for r in range(3):
        for c in range(4):
            row = [board[r+3-i][c+i] for i in range(4)] #we get the whole vertical to the left of 4 so we can evaluate it in evaluate function!
            points += evaluate(row, column)
    return points