'''
5
1,0,0,1
1,1,1,1
2,1,0,1
2,2,1,1
5,0,0,1
5,1,0,1
4,2,1,1
3,2,1,1
'''

n = int(input())
bo_setup = [[False]*(n+1) for i in range(n+1)]
pillar_setup = [[False]*(n+1) for j in range(n+1)]
build_frame = []
for i in range(n+1):
    build_frame.append(list(map(int, input().split(','))))

for _ in build_frame:
    pos_x, pos_y = _[0], _[1]
    category = _[2]
    doing = _[3]


def build_bo(x, y):
    print(x,y,check_pillar(x,y),check_bo(x,y))
    if x == n:
        return False
    if check_pillar(x,y) or check_pillar(x+1, y):
        bo_setup[y][x+1] = True
        return True
    else:
        if check_bo(x+1, y) and check_bo(x+2, y):
            bo_setup[y][x] = True
            print('build bo', x, y)
            return True
        else:
            return False


def delete_bo(x, y):
    bo_setup[y][x+1] = False
    print('d',x,y,check_bo(x+1,y),check_bo(x+2,y))
    if check_bo(x+1, y):
        bo_setup[y][x] = False
        print('delete bo', x, y)
        return True
    else:
        bo_setup[y][x+1] = True
        print('not delete bo')
        return False


def build_pillar(x, y):
    print(x,y,check_pillar(x,y),check_bo(x,y))
    if check_pillar(x, y):
        pillar_setup[y+1][x] = True
        print('build pillar', x, y)
        return True
    else:
        return False


def delete_pillar(x, y):
    p_y = y + 1
    print('de', check_bo(x - 1, p_y), check_bo(x + 1, p_y), check_bo(x, p_y), x, p_y)
    if (check_bo(x-1, p_y) and check_bo(x, p_y)) or (check_bo(x + 1, p_y) and check_bo(x, p_y)):
        pillar_setup[p_y][x] = False
        print('delete pillar', x, p_y)
        return True
    else:
        return False


def check_bo(x, y):
    if x < n-1 and y < n-1:
        print('x',x,y)
        if (pillar_setup[y][x] or pillar_setup[y][x+1]) or (bo_setup[y][x] and bo_setup[y][x+1]):
            return True
        else:
            return False
    elif x == n or y == n:
        print('x over limit')
        return False


def check_pillar(x,y):
    if y == 0 or bo_setup[y][x] or pillar_setup[y][x]:
        return True
    else:
        return False

'''
build_pillar(1,0)
build_bo(1,1)
build_pillar(2,1)
build_bo(2,2)
build_pillar(5,0)
build_pillar(5,1)
build_bo(4,2)
build_bo(3,2)
'''
build_pillar(0,0)
build_pillar(2,0)
build_pillar(4,0)
build_bo(0,1)
build_bo(1,1)
build_bo(2,1)
build_bo(3,1)
delete_pillar(2,0)
delete_bo(1,1)
build_pillar(2,2)

for _ in bo_setup:
    print('bo : ', _)
for _ in pillar_setup:
    print('pillar : ', _)