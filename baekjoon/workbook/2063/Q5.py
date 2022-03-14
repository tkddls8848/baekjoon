height, width, pos_x, pos_y, command_number = list(map(int, input().split(" ")))


roads = []
for i in range(height):
    roads.append(list(map(int, input().split(" "))))

commands = list(input().split())

print(height, width, pos_x, pos_y, command_number)
print(roads)
print(commands)
## h 1 v 1은 주사위의 중심
horizon = [0,0,0]
vertical = [0,0,0,0]

pos = [pos_x,pos_y]
##좌우 : horizon 돌고 vertical 중심 => horizon 중심으로 교체
##상하 : vertical 돌고 horizon 중심 => vertical 중심으로 교체

answer = []

def rotate_h(h, v, direction):
    new_horizon = []
    top = ''
    if direction == 'left':
        tmp = h.pop()
        new_horizon = [tmp] + h
        top = new_horizon[2]
    elif direction == 'right':
        tmp = h[0]
        h = h[1:]
        new_horizon = h + [tmp]
        top = new_horizon[0]
    v[1] = new_horizon[1]
    print("new_horizon", new_horizon, v)
    return new_horizon, v, v[1], top

def rotate_v(h, v, direction):
    new_vertical = []
    top = ''
    if direction == 'up':
        tmp = v.pop()
        new_vertical = [tmp] + v
        top = new_vertical[3]
    elif direction == 'down':
        tmp = v[0]
        v = v[1:]
        new_vertical = v + [tmp]
        top = new_vertical[3]
    h[1] = new_vertical[1]
    print("new_vertical", h, new_vertical)
    return h, new_vertical, new_vertical[1], top


for command in commands:
    print("command", command)
    ##down 위치 바닥 0
    if command == '4':
        next_x, next_y = pos[0] + 1, pos[1]
        print(pos, next_x, next_y, width, height, 0 <= next_x <= height and 0 <= next_y <= width)
        if 0 <= next_x <= height and 0 <= next_y <= width:
            horizon, vertical, bottom, top = rotate_v(horizon, vertical, 'down')
            if roads[next_x][next_y] == 0:
                roads[next_x][next_y] = bottom
                horizon[1] = 0
                vertical[1] = 0
            elif roads[next_x][next_y] != 0:
                bottom = roads[next_x][next_y]
                roads[next_x][next_y] = 0
                horizon[1] = bottom
                vertical[1] = bottom
            pos = [next_x, next_y]
            print("down", horizon, vertical, roads)
            print(bottom, top)
            answer.append(top)
    elif command == '3':
        next_x, next_y = pos[0] - 1, pos[1]
        print(pos, next_x, next_y, width, height, 0 <= next_x <= height and 0 <= next_y <= width)

        if 0 <= next_x <= height and 0 <= next_y <= width:
            horizon, vertical, bottom, top = rotate_v(horizon, vertical, 'up')
            if roads[next_x][next_y] == 0:
                roads[next_x][next_y] = bottom
                horizon[1] = 0
                vertical[1] = 0
            elif roads[next_x][next_y] != 0:
                bottom = roads[next_x][next_y]
                roads[next_x][next_y] = 0
                horizon[1] = bottom
                vertical[1] = bottom
            pos = [next_x, next_y]
            print("up", horizon, vertical, roads)
            print(bottom, top)
            answer.append(top)
    elif command == '1':
        next_x, next_y = pos[0], pos[1] + 1
        print(pos, next_x, next_y, width, height, 0 <= next_x <= height and 0 <= next_y <= width)

        if 0 <= next_x <= height and 0 <= next_y <= width:
            horizon, vertical, bottom, top = rotate_h(horizon, vertical, 'right')
            if roads[next_x][next_y] == 0:
                roads[next_x][next_y] = bottom
                horizon[1] = 0
                vertical[1] = 0
            elif roads[next_x][next_y] != 0:
                bottom = roads[next_x][next_y]
                roads[next_x][next_y] = 0
                horizon[1] = bottom
                vertical[1] = bottom
            pos = [next_x, next_y]
            print("right", horizon, vertical, roads)
            print(bottom, top)
            answer.append(top)
    elif command == '2':
        next_x, next_y = pos[0], pos[1] - 1
        print(pos, next_x, next_y, width, height, 0 <= next_x <= height and 0 <= next_y <= width)

        if 0 <= next_x <= height and 0 <= next_y <= width:
            horizon, vertical, bottom, top = rotate_h(horizon, vertical, 'left')
            if roads[next_x][next_y] == 0:
                roads[next_x][next_y] = bottom
                horizon[1] = 0
                vertical[1] = 0
            elif roads[next_x][next_y] != 0:
                bottom = roads[next_x][next_y]
                roads[next_x][next_y] = 0
                horizon[1] = bottom
                vertical[1] = bottom
            pos = [next_x, next_y]
            print("left", horizon, vertical, roads)
            print(bottom, top)
            answer.append(top)

print("FINAL", answer)