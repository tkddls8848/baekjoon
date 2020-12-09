N = input()
list = list(N)
point = 1
answer = []


def dfs(list, point, result):
    if point == len(list):
        answer.append(result)
        return result
    dfs(list, point+1, int(result)+int(list[point]))
    dfs(list, point+1, int(result)*int(list[point]))


dfs(list,point,list[0])
print(sorted(answer)[-1])