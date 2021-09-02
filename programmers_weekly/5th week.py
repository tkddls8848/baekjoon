word = "AAAAE"

def recursive(alphabet, depth, string):

    if depth == len(alphabet):
        return string

    for _ in alphabet:
        string += _
        depth += 1
        recursive(alphabet, depth, string)

def solution(word):
    alphabet = ['A', 'E', 'I', 'O', 'U']
    string = ""
    l = []
    for _ in alphabet:
        tmp1 = string.join(_)
        print(string+tmp1,"tmp1")
        l.append(string + tmp1)
        for _ in alphabet:
            tmp2 = string.join(_)
            print(string+tmp1+tmp2, "tmp2")
            l.append(string+tmp1+tmp2)
            for _ in alphabet:
                tmp3 = string.join(_)
                print(string + tmp1 + tmp2 + tmp3, "tmp3")
                l.append(string + tmp1 + tmp2 + tmp3)
                for _ in alphabet:
                    tmp4 = string.join(_)
                    print(string + tmp1 + tmp2 + tmp3 + tmp4, "tmp4")
                    l.append(string + tmp1 + tmp2 + tmp3 + tmp4)
                    for _ in alphabet:
                        tmp5 = string.join(_)
                        print(string + tmp1 + tmp2 + tmp3 + tmp4 + tmp5, "tmp5")
                        l.append(string + tmp1 + tmp2 + tmp3 + tmp4 + tmp5)
    print(l)
    return l.index(word) + 1

print(solution(word))