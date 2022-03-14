n = 5
clockwise = True	##[[1,2,3,4,1],[4,5,6,5,2],[3,6,7,6,3],[2,5,6,5,4],[1,4,3,2,1]]

import copy
def rotate(mat):
    new_mat = [[0,0,0],[0,0,0],[0,0,0]]
    length = len(mat)
    for r in range(len(mat)):
        for c in range(len(mat)):
            new_mat[c][length-r-1] = mat[r][c]
    print(new_mat)


def solution(n, clockwise):
    tmp_matrix = [[1,2,3],[4,5,6],[7,8,9]]
    rotate(tmp_matrix)
    start_pos = [0, 0]


        ##뱡향 돌림
        ##startpos 바꿈
    return 0

print("FINAL", solution(n, clockwise))