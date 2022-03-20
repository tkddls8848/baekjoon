'''
4
3
0
4
0
'''
n = int(input())
stack = []
for i in range(n):
    command = int(input())
    if command == 0:
        stack.pop()
    else:
        stack.append(command)

print(sum(stack))