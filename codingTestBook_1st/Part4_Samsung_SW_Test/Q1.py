'''
3
0 0 0
0 0 0
0 9 0

3
0 0 1
0 0 0
0 9 0

4
4 3 2 1
0 0 0 0
0 0 9 0
1 2 3 4

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
n = int(input())
graph = []
shark_pos = [0, 0]
shark_size = 2
shark_fish_cnt = 0
for i in range(n):
    graph.append(list(map(int, input().split())))
for j in range(n):
    for k in range(n):
        if graph[j][k] == 9:
            shark_pos = [j, k]
            print(shark_pos)
            break
move = [[0, 1], [1, 0], [-1, 0], [0, -1]]

