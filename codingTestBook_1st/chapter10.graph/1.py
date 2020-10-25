def find_setNum(setNums, x):
    if not setNums[x] == x:
        return find_setNum(setNums, setNums[x])
    return x

def union_setNum(setNums, a, b):
    n, m = find_setNum(setNums, a), find_setNum(setNums, b)
    setNums[n], setNums[m] = min(n, m), min(n, m)

'''
6 4
1 4
2 3
2 4
5 6
'''
v, e = map(int, input().split())
setNums = []
for i in range(v+1):
    setNums.append(i)

for i in range(e):
    a,b = map(int, input().split())
    union_setNum(setNums, a ,b)

for _ in setNums:
    print(find_setNum(setNums,_), end=' ')

print(setNums)