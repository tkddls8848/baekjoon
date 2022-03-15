arr = []
mul = []
for _ in input():
    if _ == 'c':
        if arr != []:
            if arr[-1] == 'c':
                mul.append(25)
            else:
                mul.append(26)
        else:
            mul.append(26)
    else:
        if arr != []:
            if arr[-1] == 'd':
                mul.append(9)
            else:
                mul.append(10)
        else:
            mul.append(10)
    arr.append(_)
total = 1
for _ in mul:
    total *= _
print(total)

