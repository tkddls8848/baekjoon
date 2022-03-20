'''
([ (([( [ ] ) ( ) (( ))] )) ]).
'''
while True:
    s = input()
    ##print(s)
    if s == '.':
        break
    bracket1 = []
    bracket2 = []
    for i in s:
        if i == '(' or i == ')':
            bracket1.append(i)
        elif i == '[' or i == ']':
            bracket2.append(i)
    ##print(bracket1, bracket2)

    tmp = []
    flag = True
    for b in bracket1:
        if b == "(":
            tmp.append(b)
        elif b == ")":
            if tmp and tmp[-1] == "(":
                tmp.pop()
            else:
                tmp.append(b)
    print(tmp)
    if tmp:
        flag = False
        ##print("NO ()")
    else:
        flag = True
        ##print("YES ()")

    tmp1 = []
    flag1 = True
    for b in bracket2:
        if b == "[":
            tmp1.append(b)
        elif b == "]":
            if tmp1 and tmp1[-1] == "[":
                tmp1.pop()
            else:
                tmp1.append(b)
    ##print(tmp1)
    if tmp1:
        ##print("NO []")
        flag1 = False
    else:
        ##print("YES []")
        flag1 = True
    ##print(flag, flag1)
    if flag == True and flag1 == True:
        print('yes')
    else:
        print('no')