'''
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

4
S S S T
X X X X
X X X X
T T T X

3
S S X
X X X
X X T
'''
from itertools import combinations


n = int(input())
graph = []
teacherPos = []
studentPos = []
space = []

for i in range(n):
    li = list(input().split())
    graph.append(li)
    for j in range(n):
        if graph[i][j] == 'T':
            teacherPos.append([i,j])
        elif graph[i][j] == 'S':
            studentPos.append([i,j])
        else:
            space.append([i,j])
print('t', teacherPos, 's', studentPos)


def teacher(y,x):
    listX = graph[x]
    listY = []
    for i in range(n):
        listY.append(graph[i][y])
    for _ in listX:
        if _ == 'O':
            return False
            break
        elif _ == 'S':
            return True
    for _ in listY:
        if _ == 'O':
            return False
            break
        elif _ == 'S':
            return True
    return False


def search():##학생이 보이면 TRUE 아니면 FALSE
    result = False
    for _ in teacherPos:
        result = result or teacher(_[0], _[1])
    return result


def obstacle():
    covered = False
    for combi in combinations(space,3):
        print(combi)
        for _ in combi:
            x, y = _[0], _[1]
            graph[x][y] = 'O'
            for _ in graph:
                print(_)
            print()
            if not search():
                covered = True
        for _ in combi:
            x, y = _[0], _[1]
            graph[x][y] = 'X'
    if not covered:
        print('NO')
    else:
        print('YES')


obstacle()