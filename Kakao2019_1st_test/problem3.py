'''
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
'''
key = [[0, 0, 1], [0, 0, 0], [0, 0, 0]]
lock = [[1, 1, 0], [1, 1, 1], [1, 1, 1]]
def rotate90(arr):
    new = []
    for a in range(len(arr)):
        new.append([])
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            new[i].append(arr[len(arr)-j-1][i])
    return new


def padding(arr):
    for i in range(len(arr)):
        arr[i] = [0,0] + arr[i] + [0,0]
    arr = [[0]*(len(arr)+4)]*2 + arr + [[0]*(len(arr)+4)]*2
    return arr


def check(key, lock):
    for i in range(len(key)):
        for j in range(len(key)):
            print(lock[i][j] ^ key[i-2][j-2])
            if lock[i][j] ^ key[i-2][j-2] == 0:
                return False
                break
    return True


def solution(key, lock):
    answer = True
    return answer


print(lock)
print(check(key, padding(lock)))
print(lock)