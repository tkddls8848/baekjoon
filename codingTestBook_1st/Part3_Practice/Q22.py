'''
5
00011
00010
01011
11001
00000
'''
from collections import deque

board = []
space = " "
move = [[1, 0], [-1, 0], [0, 1], [0, -1]]

q = deque()
n = int(input())
for i in range(n):
    board.append(list(map(int, space.join(input().split()))))

pos = [[1,1],[1,2]]

def onestep(position,depth):
    nx, ny = 0, 0
    pos = position
    if depth == 2:
        return position
    else:
        for a in pos:
            for i in move:
                nx = a[0] + i[0]
                ny = a[1] + i[1]
                onestep([[nx,ny],a],depth+1)
                onestep([a,[nx,ny]],depth+1)
                print(nx,ny)

onestep(pos,0)