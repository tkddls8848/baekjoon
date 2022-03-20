'''
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
'''

n = int(input())
stack = []
cnt = 0
while cnt != n:
    commands = input().split(' ')
    types = commands[0]
    if types == 'push':
        num = commands[1]
        stack.append(num)
    elif types == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif types == 'size':
        print(len(stack))
    elif types == 'empty':
        if stack == []:
            print(1)
        else:
            print(0)
    elif types == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
    cnt += 1