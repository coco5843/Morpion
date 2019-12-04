

def is_winner(board, symbol):
    # Columns
    size = len(board)
    for x in range(0, size):
        count = 0
        for y in range(0, size):
            if board[y][x] == symbol:
                count += 1
                if count >= size:
                    return True
            else:
                break
    # Rows
    for y in range(0, size):
        count = 0
        for x in range(0, size):
            if board[y][x] == symbol:
                count += 1
                if count >= size:
                    return True
            else:
                break

    # Reversed diagonal
    count = 0
    for i in range(0, size):
        if board[i][size - 1 - i] == symbol:
            count += 1
            if count >= size:
                return True
        else:
            break
    # Diagonal
    count = 0
    for i in range(0, size):
        if board[i][i] == symbol:
            count += 1
            if count >= size:
                return True
        else:
            break



