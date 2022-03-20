'''
1
(((()())()
'''
n = int(input())

for i in range(n):
    stack = list(input())
    bracket = []
    for s in stack:
        if s == ")" and bracket and bracket[-1] == "(":
            bracket.pop()
        else:
            bracket.append(s)
    if bracket:
        print("NO")
    else:
        print("YES")
