N = input()


def check(n):
    l = list(n)
    result1, result2 = 0, 0
    for _ in l:
        result1 += int(_)
        result2 *= int(_)
    if result1 == 0 or result2 == 1:
        return True
    else:
        return False



def flip(num):
    l = list(num)
    count0 = 0
    count1 = 0
    if int(l[0]) == 0:
        count0 = count0 + 1
    else:
        count1 = count1 + 1
    for i in range(len(l)-1):
        if int(l[i])^int(l[i+1]) == 1:
            if int(l[i+1]) == 0:
                count0 = count0 + 1
            elif int(l[i+1])  == 1:
                count1 = count1 + 1
    return min(count0,count1)

print(flip(N))