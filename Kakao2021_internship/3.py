n = 8
k = 2
cmd = ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]
# OOOOXOOO

def up(l, k):
    k = l[k][0]
    if k == "H":
        return 0
    return k


def down(l, k):
    k = l[k][1]
    if k == "T":
        return len(l)-1
    return k


def cut(l, k, s):
    pre, nex = l[k][0], l[k][1]
    s.append([[pre,nex],k])
    if pre == "H":
        tmp = l[k][1]
        l[nex][0] = "H"
        l[k] = [k, k]
        return tmp
    elif nex == "T":
        tmp = l[k][0]
        l[pre][1] = "T"
        l[k] = [k, k]
        return tmp
    l[pre][1] = l[k][1]
    l[nex][0] = l[k][0]
    tmp = down(l, k)
    l[k] = [k,k]
    return tmp


def paste(l, k, s):
    tmp = s.pop()
    pre, nex, pos = tmp[0][0], tmp[0][1], tmp[1]
    l[pos] = [pre, nex]
    if pre == "H":
        l[nex][0] = pos
    elif nex == "T":
        l[pre][1] = pos
    else:
        l[pre][1] = pos
        l[nex][0] = pos
    return k

def solution(n, k, cmd):
    linked_list = [[i - 1, i + 1] for i in range(n)]
    linked_list[0] = ["H", 1]
    linked_list[-1] = [len(linked_list) - 2, "T"]
    stack = []
    answer = []
    new_cmd = ""

    for _ in cmd:
        if not len(_) == 1:
            tmp = list(_.split(" "))
            new_cmd += str(tmp[0])*int(tmp[1])
        else:
            new_cmd += str(_)
    print(k)
    for _ in new_cmd:
        if _ == "U":
            k = up(linked_list, k)
            print("U", linked_list, k)
        elif _ == "D":
            k = down(linked_list, k)
            print("D", linked_list, k)
        elif _ == "C":
            k = cut(linked_list, k, stack)
            print("C", linked_list, k, stack, answer)
        elif _ == "Z":
            k = paste(linked_list, k, stack)
            print("Z", linked_list, k, stack, answer)
    for i in range(len(linked_list)):
        if not linked_list[i][0] == linked_list[i][1]:
            answer.append("O")
        else:
            answer.append("X")
    print(answer)
    return "".join(answer)

solution(n,k,cmd)