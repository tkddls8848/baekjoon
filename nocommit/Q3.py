from itertools import combinations

width = 2
height = 2
diagonals = [[1,1], [2,2]]	#result12

width = 51
height = 37
diagonals = [[17,19]]	#result12

import copy

def two_dot_distance(arr1, arr2):
    cnt = 0
    test = []
    tmp1 = abs(arr1[0] - arr2[0])
    tmp2 = abs(arr1[1] - arr2[1])
    for h in range(tmp1):
        test.append("H")
    for v in range(tmp2):
        test.append("V")
    for c in combinations(test, tmp1):
        cnt += 1
    return cnt

def solution(width, height, diagonals):
    DP = [[0] * width] * height

    #0 0 => 대각 => 끝
    for diagonal in diagonals:
        tmp1 = copy.deepcopy(diagonal)
        tmp1[0] -= 1
        pivot1 = tmp1
        print(diagonal, pivot1)
        print(two_dot_distance([0,0], pivot1))
        print(two_dot_distance(pivot1, [width, 0]))
        return ((two_dot_distance([0,0], pivot1) * two_dot_distance(pivot1, [width, 0])) * 2 * len(diagonals)) % 10000019
    return 0

print("FINAL", solution(width, height, diagonals))