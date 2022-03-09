word = "I"
from itertools import product


def solution(word):
    alphabet = ['A', 'O', 'E', 'I', 'U']
    alphabet.sort()
    l = []
    for i in range(1, len(alphabet)+1):
        for c in product(alphabet):
            tmp = ""
            for _ in c:
                tmp += _
            l.append(tmp)
    li = sorted(l)
    print(li)
    return li.index(word)+1


print(solution(word))