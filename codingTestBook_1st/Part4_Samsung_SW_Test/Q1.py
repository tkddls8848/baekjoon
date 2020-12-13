'''
3
0 5 0
5 9 5
0 5 0

3
0 0 1
0 1 0
0 9 0

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4
answer14

6
5 4 3 2 3 4
4 3 2 3 4 5
3 2 9 5 6 6
2 1 2 3 4 5
3 2 1 6 5 4
6 6 6 6 6 6
answer60

6
6 0 6 0 6 1
0 0 0 0 0 2
2 3 4 5 6 6
0 0 0 0 0 2
0 2 0 0 0 0
3 9 3 0 0 1
answer48

6
1 1 1 1 1 1
2 2 6 2 2 3
2 2 5 2 2 3
2 2 2 4 6 3
0 0 0 0 0 6
0 0 0 0 0 9
answer39
'''
from collections import deque

n = int(input())
shark_pos = [0, 0]
shark_size = 2
shark_fish_cnt = 0
fish = []
for i in range(n):
    fish.append(list(map(int, input().split())))
for j in range(n):
    for k in range(n):
        if fish[j][k] == 9:
            shark_pos = [j, k]
            print('shark',shark_pos)
            break
move = [[-1, 0], [0, -1], [1, 0], [0, 1]]
distance = 0


##탐색함수
def search(start, shark_size):
    x, y = start[0], start[1]
    q = deque()
    q.append([x, y, 0])
    visited = [[False] * n for _ in range(n)]
    visited[x][y] = True
    target = []
    while q:
        pos = q.popleft()
        for _ in move:
            ax, ay = pos[0] + _[0], pos[1] + _[1]
            if 0 <= ax < n and 0 <= ay < n:
                if not visited[ax][ay] and not fish[ax][ay] > shark_size:
                    fish_size = fish[ax][ay]
                    q.append([ax, ay])
                    visited[ax][ay] = True
                    if not fish[ax][ay] == 0 and judge_fish(shark_size, fish_size):
                        t = move_destination([x,y],[ax,ay])
                        target.append([ax, ay, t])
                        visited[ax][ay] = True
    if len(target) == 0:
        return target
    elif len(target) == 1:
        return target[0]
    else:
        result = sorted(target, key=lambda x: (x[2], x[0], x[1]))[0]
        return result


##물고기 먹을수 있는가?
def judge_fish(shark_size, fish_size):
    if shark_size > fish_size:
        return True
    else:
        return False


##이동
def move_destination(pos, destination):
    time = abs(int(pos[0])-int(destination[0]))+abs(int(pos[1])-int(destination[1]))
    fish[pos[0]][pos[1]] = 0
    return time


##물고기 먹기
def eat_fish(pos, shark_size, shark_fish_cnt):
    shark_fish_cnt += 1
    x, y = pos[0], pos[1]
    fish[x][y] = 9
    if shark_size == shark_fish_cnt:
        return [shark_size + 1, 0]
    else:
        return [shark_size, shark_fish_cnt]



def solve(shark_pos, shark_size, shark_fish_cnt):
    pos = shark_pos
    size = shark_size
    fish_cnt = shark_fish_cnt
    time = 0
    target_pos = search(pos, size)
    if len(target_pos) == 0:
        return time
    time += move_destination(pos, target_pos)
    pos = target_pos
    [size, fish_cnt] = eat_fish(pos, size, fish_cnt)
    while True:
        target_pos = search(pos, size)
        if len(target_pos) == 0:
            break
        time += move_destination(pos, target_pos)
        pos = target_pos[0:2]
        [size, fish_cnt] = eat_fish(pos, size, fish_cnt)
    return time


print('FINAL ANSWER', solve(shark_pos,2,0))