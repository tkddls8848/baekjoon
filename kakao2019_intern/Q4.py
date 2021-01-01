from collections import deque
board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]

def solution(board):
    length = len(board)
    cost = [[10 ** 9] * length for _ in range(length)]
    move = [[1, 0, 'U'], [0, 1, 'R'], [-1, 0, 'D'], [0, -1, 'L']]

    q = deque()
    q.append([0,0,'START',0])
    cost[0][0] = 0
    while q:
        y, x, t, c = q.popleft()
        for _ in move:
            ay, ax, at = y + _[0], x + _[1], _[2]
            if 0 <= ay < length and 0 <= ax < length and not board[ay][ax]:
                if t == at or t == 'START':
                    if cost[ay][ax] >= c + 100:
                        cost[ay][ax] = c + 100
                        q.append([ay, ax, at, c + 100])
                elif not t == at:
                    if cost[ay][ax] >= c + 600:
                        cost[ay][ax] = c + 600
                        q.append([ay, ax, at, c + 600])
    return cost[length-1][length-1]


print(solution(board))
