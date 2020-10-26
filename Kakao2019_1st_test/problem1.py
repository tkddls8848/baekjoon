s = "abcabcdede"


def solution(s):
    answer = 1001
    length = len(s)//2+1
    list = []
    for i in range(1, length+1):
        for j in range(0, len(s)):
            if not s[i*j:i*(j+1)] == '':
                list.append(s[i*j:i*(j+1)])
        count = 1
        tmp = ""
        finalStr = ""
        for a in list:
            if not tmp == a:
                if count != 1:
                    finalStr += str(count)
                finalStr += str(tmp)
                tmp = a
                count = 1
            else:
                count += 1
        if count != 1:
            finalStr += str(count)
        finalStr += str(tmp)
        print(finalStr)
        if answer > len(finalStr):
            answer = len(finalStr)
        list.clear()
    return answer


print(solution(s))