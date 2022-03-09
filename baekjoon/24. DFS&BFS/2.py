'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
from collections import deque

n = int(input())
lines = int(input())
connection = []
visited = [False for i in range(n+1)]
for i in range(lines):
    connection.append(sorted(list(map(int, input().split(" ")))))
q = deque()
for line in connection:
    if 1 in line:
        q.append(line[1])
        visited[1] = True
        connection.remove(line)

cnt = 1

while q:
    pos = q.popleft()
    for _ in connection:
        if pos in _:
            if visited[_[1]] == False:
                q.append(_[1])
                visited[_[1]] = True
                connection.remove(_)
                cnt += 1

print(cnt)