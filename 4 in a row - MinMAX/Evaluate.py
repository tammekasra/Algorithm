

def evaluate(window, piece):
    score = 0
    if piece == 2:
        oppponent = 1
    else:
        opponent = 2
    

    if window.count(piece) == 4:
        score += 100
    elif window.count(piece) == 3 and window.count(0) == 1:
        score += 5
    elif window.count(piece) == 2 and window.count(0) == 2:
        score += 2

    if window.count(opponent) == 3 and window.count(0) == 1:
        score -= 4

    return score

def score(board, piece):
    score = 0

    ## Score center column
    center_array = [int(i) for i in list(board[:, 7//2])]
    center_count = center_array.count(piece)
    score += center_count * 3

    ## Score Horizontal
    for r in range(6):
        row_array = [int(i) for i in list(board[r,:])]
        for c in range(7-3):
            window = row_array[c:c+4]
            score += evaluate(window, piece)

    ## Score Vertical
    for c in range(7):
        col_array = [int(i) for i in list(board[:,c])]
        for r in range(3):
            window = col_array[r:r+4]
            score += evaluate(window, piece)

    ## Score posiive sloped diagonal
    for r in range(3):
        for c in range(4):
            window = [board[r+i][c+i] for i in range(4)]
            score += evaluate(window, piece)

    for r in range(3):
        for c in range(4):
            window = [board[r+3-i][c+i] for i in range(4)]
            score += evaluate(window, piece)

    return score