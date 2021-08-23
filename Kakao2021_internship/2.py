from collections import deque

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
          ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
          ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]


def bfs(pos, place):
    visited = [[False] * len(place) for _ in range(len(place))]
    move = [[1,0],[0,1],[-1,0],[0,-1]]

    q = deque([pos + [0]])
    visited[pos[0]][pos[1]] = True

    while q:
        x, y, cnt = q.popleft()
        for _ in move:
            nx, ny, ncnt = x+_[0], y+_[1], cnt+1
            if 0 <= nx < len(place) and 0 <= ny < len(place) and not visited[nx][ny]:
                visited[nx][ny] = True
                if place[nx][ny] == "P":
                    if ncnt <= 2:
                        return False
                elif place[nx][ny] == "O":
                    if ncnt <= 1:
                        q.append([nx,ny,ncnt])
    return True

def solution(places):
    answer = []
    for _ in places:
        result = 1
        for i in range(len(places)):
            for j in range(len(places)):
                if _[i][j] == "P":
                    if not bfs([i,j],_):
                        result = 0
                        break
        answer.append(result)
    return answer

print(solution(places))