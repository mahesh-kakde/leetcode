moves1 = [[0,0],[2,0],[1,1],[2,1],[2,2]]
moves2 = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
moves3 = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]

def sol(moves):
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    for i in range(len(moves)):
        r = moves[i][0]
        c = moves[i][1]

        if i % 2 == 0:
            board[r][c] = 1
        else:
            board[r][c] = 2

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != 0:
            if board[i][0] == 1:
                return "A"
            else:
                return "B"

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != 0:
            if board[0][i] == 1:
                return "A"
            else:
                return "B"

    if board[0][0] == board[1][1] == board[2][2] != 0:
        if board[0][0] == 1:
            return "A"
        else:
            return "B"

    if board[0][2] == board[1][1] == board[2][0] != 0:
        if board[0][2] == 1:
            return "A"
        else:
            return "B"

    if len(moves) == 9:
        return "Draw"

    return "Pending"

print(sol(moves1))
print(sol(moves2))
print(sol(moves3))