citations = [3,0,6,1,5]


def solution(citations):
    dic = {}
    for k, v in enumerate(citations):
        dic[k] = v
    h = 0
    while h != len(citations):
        cnt = 0
        for d in dic:
            if dic[d] >= h:
                cnt += 1
        if h == cnt:
            break
        h += 1
    return h

print("FINAL", solution(citations))