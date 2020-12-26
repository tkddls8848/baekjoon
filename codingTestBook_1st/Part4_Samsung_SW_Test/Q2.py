'''
7 6 2 3 15 6 9 8
3 1 1 8 14 7 10 1
6 1 13 6 4 3 11 4
16 1 8 7 5 2 12 2

16 7 1 4 4 3 12 8
14 7 7 6 3 4 10 2
5 2 15 2 8 3 6 4
11 8 2 4 13 5 9 4

12 6 14 5 4 5 6 7
15 1 11 7 3 7 7 5
10 3 8 3 16 6 1 1
5 8 2 7 13 6 9 2
'''

#direction 시계방향 위쪽이1 ~ 9
fish = [[0]*4 for _ in range(4)]
move = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        fish[i][j] = [data[j*2], data[j*2+1]-1]

print(fish)
'''
물고기 움직임
1.번호 순으로 움직인다
2.물고기 방향에 따라 움직인다
3.상어나 공간밖만 아니면 이동
4.서로 교환 방식으로 이동함
5.이동할 곳이 없으면 반시계 45도 회전
6.아무곳도 없으면 이동 안함

상어 움직임
1.0,0의 물고기를 먹는다
2.먹은 물고기 방향을 공유한다.
3.해당방향의 물고기 중 하나를 먹으며 이동.(중간은 안먹음)
4.상어 이동 후에는 물고기 다시 이동
4.상어 이동 불능하면 집으로 감
'''
search_fish_list = []
for i in range(4):
    for j in range(4):
        search_fish_list.append(fish[i][j]+[i,j])
fish_list = sorted(search_fish_list, key=lambda x: x[0])

def fish_move(fish_list):
    fish_num, fish_dir,fish_pos = fish[0], fish[1], [fish[2], fish[3]]

