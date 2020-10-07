from collections import deque

graph = [
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0]
]

visited = [[False]*7 for _ in range(0,7)]

move = [[-1,0], [1,0], [0,1], [0,-1]]
cnt = 0
q = deque()

for i in visited:
    print(i)

def dfs(y,x, graph):
    if graph[x][y] == 1:
        graph[x][y] = 0
        visited[x][y] = True
        for i in move:
            after_x, after_y = x + i[0], y + i[1]
            print(i[0], i[1])
            if 0 <= after_x <= 6 and 0 <= after_y <= 6:
                if not visited[after_x][after_y] and graph[after_x][after_y] == 1:
                    print(after_y, after_x)
                    visited[after_x][after_y] = True
                    dfs(after_y, after_x, graph)
                    graph[after_x][after_y] = 0
                    print()


                    return 1
    return 0

dfs(1,4,graph)
#for i in range(0,7):
#    for j in range(0,7):
#        cnt += dfs(i, j)

for i in visited:
    print(i)

print('cnt', cnt)