'''
2
5 6
0 0 1 0

3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1
'''
n = int(input())
array = list(map(int, input().split()))
plus, minus, multiply, divide = map(int, input().split())
result = []

def dfs(total, pointer):
    global plus, minus, multiply, divide
    if pointer == n:
        print('asdf',total)
        result.append(total)
    else:
        if plus > 0:
            plus -= 1
            dfs(total + array[pointer], pointer + 1)
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(total - array[pointer], pointer + 1)
            minus += 1
        if multiply > 0:
            multiply -= 1
            dfs(total * array[pointer], pointer + 1)
            multiply += 1
        if divide > 0:
            divide -= 1
            dfs(int(total / array[pointer]), pointer + 1)
            divide += 1

print(dfs(array[0],1))
result.sort()
print(result[0], result[-1])