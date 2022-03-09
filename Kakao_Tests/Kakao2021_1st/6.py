'''
14
'''

board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
from collections import deque

def moves(board, row, column):
    m = [[0, 1],[1, 0],[-1, 0],[0, -1]]
    move = []

    for _ in m:
        nr, nc = row + _[0], column + _[1]
        if (nr < 0 or nr > 3) or (nc < 0 or nc > 3):
            continue
        else:
            move.append([nr, nc])
    print("row, column", row, column)
    lr = board[row]
    ud = []
    for _ in board:
        ud.append(_[column])
    print(lr, ud)
    tmp_left , tmp_right, tmp_up, tmp_down = column, column, row, row
    while not tmp_left == 0:
        tmp = board[row][tmp_left]
        if not tmp == 0:
            break
        tmp_left -= 1
    print("tmp_left", tmp_left)
    move.append([row, tmp_left])
    while not tmp_right == 3:
        tmp = board[row][tmp_right]
        if not tmp == 0:
            break
        tmp_right += 1
    print("tmp_right", tmp_right)
    move.append([row, tmp_right])
    while not tmp_up == 0:
        tmp = board[tmp_up][column]
        if not tmp == 0:
            break
        tmp_up -= 1
    print("tmp_up", tmp_up)
    move.append([tmp_up, column])
    while not tmp_down == 3:
        tmp = board[tmp_down][column]
        if not tmp == 0:
            break
        tmp_down += 1
    print("tmp_down", tmp_down)
    move.append([tmp_down, column])
    print(move)
    return move

def DP(board, target):
    pos = []
    DP = [["N"]*4 for i in range(4)]
    for r in range(len(board)):
        if target in board[r]:
            for c in range(len(board[r])):
                if board[r][c] == target:
                    ##print("position", r,c)
                    pos.append([r, c])
    pos.sort()
    INF = pow(10, 10)
    x, y = abs(pos[0][0]-pos[1][0]), abs(pos[0][1]-pos[1][1])
    for i in range(pos[0][0], pos[1][0]+1):
        for j in range(pos[0][1], pos[1][1]+1):
           DP[i][j] = INF
    DP[pos[0][0]][pos[0][1]] = 0
    q = deque()

    print("move",moves(board, pos[0][0],pos[0][1]))
    for move in (moves(board, pos[0][0],pos[0][1])):
        nx, ny = move[0], move[1]
        if DP[nx][ny] == "N":
            continue
        elif DP[nx][ny] > DP[pos[0][0]][pos[0][1]]+1:
            DP[nx][ny] = DP[pos[0][0]][pos[0][1]]+1
            q.append([nx,ny])
            print([nx,ny], q)
    while q:
        x, y = q.pop()
        for move in (moves(board, x, y)):
            nx, ny = move[0], move[1]
            if DP[nx][ny] == "N":
                continue
            elif DP[nx][ny] > DP[x][y] + 1:
                DP[nx][ny] = DP[x][y] + 1
                q.append([nx, ny])
                print([nx, ny], q)

    for _ in DP:
        print("pppp", _)

    return 0


def solution(board, r, c):
    answer = 0
    moves(board, 0, 0)


    return answer

solution(board, r, c)