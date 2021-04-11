'''
board = [[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
r = 0
c = 1
'''
from collections import deque
board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[0,0,1,0]]
r = 3
c = 0
card_pairing = deque()

def flop_card(board, r, c):
    if not len(card_pairing) == 2:
        card_pairing.append([r, c])
        board[r][c] = 0
    else:
        card_pairing.clear()
        card_pairing.append([r, c])
        board[r][c] = 0
    print(card_pairing)

def out_board(board, r, c):
    if 0<=r<=len(board) and 0<=c<=len(board):
        result = False
    else:
        result = True
    return result

def move(r, c):
    m = [[0,1],[1,0],[-1,0],[0,-1]]
    move = []
    for _ in m:
        move.append([r + _[0], c + _[1]])
    return move

def ctrl_move(board, r, c, direction):
    nr, nc = r+direction[0], c+direction[1]
    while True:
        if out_board(board,nr,nc):
            break
        if not board[nr][nc] == 0:
            break
        nr, nc = nr + direction[0], nc + direction[1]
    print([nr,nc])
    return [nr,nc]

def solution(board, r, c):
    answer = 0
    ctrl_move(board,r,c,[-1,0])
    flop_card(board,2,2)
    flop_card(board,2,3)
    flop_card(board,2,1)

    return answer

def bfs(board,r,c):
    q = deque
    visited = [[False]*len(board)]*len(board)
    move = [[0,1],[1,0],[-1,0],[0,-1]]

solution(board,r,c)