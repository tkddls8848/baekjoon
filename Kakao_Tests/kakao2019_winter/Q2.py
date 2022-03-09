s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

def solution(s):
    answer = []

    str = s[2:-2].split('},{')
    strlist = []
    for _ in str:
        strlist.append(_.split(','))
    strlist.sort(key=lambda x: len(x))
    print(strlist)
    tmp = set('')
    for _ in strlist:
        target = set(_)
        answer.append(int(list(target - tmp)[0]))
        tmp = target
    print(answer)
    return answer

solution(s)