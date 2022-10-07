

def evaluate(row, piece):
    evualuation = 0  #not sure if it correct or not....
    if piece == 2:
        opponent = 1
    else:
        opponent = 2

    if row.count(opponent) == 3 and row.count(0) == 1:
        evualuation -= 4
    if row.count(piece) == 2 and row.count(0) == 2:
        evualuation += 2
    if row.count(piece) == 3 and row.count(0) == 1:
        evualuation += 5
    if row.count(piece) == 4:
        evualuation += 100
    return evualuation

def score(board, piece):
    score = 0

  
    center_array = [int(j) for j in list(board[:, 7//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    
    for r in range(6):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(4):
            row = row_array[c:c+4]
            score += evaluate(row, piece)
    for c in range(7):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(3):
            row = col_array[r:r+4]
            score += evaluate(row, piece)
    for r in range(3):
        for c in range(4):
            row = [board[r+i][c+i] for i in range(4)]
            score += evaluate(row, piece)
    for r in range(3):
        for c in range(4):
            row = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate(row, piece)

    return score