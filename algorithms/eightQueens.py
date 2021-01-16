QUEEN_MARKER = 'X'

def printBoard(board):
    for i in range(len(board)):
        print(board[i])

def depthOneCopy(board):
    nextboard = []
    for i in range(len(board)):
        row = board[i]
        nextboard.append(row.copy())
    return nextboard

def checkDiagLeft(board, row, col):
    # check up and left
    while row > 0 and col > 0:
        if board[row-1][col-1] == QUEEN_MARKER:
            return False
        row -= 1
        col -= 1

    return True

def checkDiagRight(board, row, col):
    # check up and right
    while row > 0 and col < len(board) - 1:
        if board[row-1][col+1] == QUEEN_MARKER:
            return False
        row -= 1
        col += 1
    return True

def checkVert(board, row, col):
    # for each row from i to row
    for i in range(row+1):
        if board[i][col] == QUEEN_MARKER:
            return False
    return True

def canPlaceQueen(board, row, col):
    return checkVert(board, row, col) and checkDiagLeft(board, row, col) and checkDiagRight(board, row, col)

def queens(board = [], row = 0, depth = 0):
    if not board:
        for i in range(8):
            board.append([])
            for j in range(8):
                board[i].append('o')

    if row == 7:
        for col in range(len(board)):
            if canPlaceQueen(board, row, col):
                print('')
                printBoard(board)
                return 1
        return 0

    total = 0
    # for each col recursive operation
    for col in range(0, len(board)):
        if canPlaceQueen(board, row, col):
            nextboard = depthOneCopy(board)
            nextboard[row][col] = QUEEN_MARKER
            total += queens(nextboard, row+1, depth+1)

    return total

print(f'total is: {queens()}')