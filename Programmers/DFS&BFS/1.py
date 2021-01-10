numbers	= [1, 1, 1, 1, 1]
target = 3
answer = 0

def dfs(number, depth):
    global answer
#    print(number, depth)
    if depth == len(numbers):
        if number == target:
            answer += 1
            print("answer", answer)
    if depth < len(numbers):
        dfs(number + 1, depth + 1)
        dfs(number - 1, depth + 1)

dfs(0,0)