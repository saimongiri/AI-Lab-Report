def heuristic(board, player):
    opponent = 'O' if player == 'X' else 'X'
    
    lines = []

    # rows
    for row in board:
        lines.append(row)

    # columns
    for col in range(3):
        lines.append([board[row][col] for row in range(3)])

    # diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2-i] for i in range(3)])

    p_open = 0
    o_open = 0

    for line in lines:
        if opponent not in line:
            p_open += 1
        if player not in line:
            o_open += 1

    return p_open - o_open


board = [
    ['X',' ',' '],
    [' ','O',' '],
    [' ',' ','X']
]

print("Heuristic value:", heuristic(board, 'X'))