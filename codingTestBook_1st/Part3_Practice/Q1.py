N = input()
M = list(map(int, input().split()))
'''
5
2 3 1 2 2
'''
def guild(M):
    M.sort()
    cnt = 0
    while M :
        max = M[0]
        M = M[max:]
        cnt += 1
    print(cnt)


guild(M)
