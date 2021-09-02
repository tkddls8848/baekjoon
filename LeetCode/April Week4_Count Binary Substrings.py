s = '00110011'
'''
def countBinarySubstrings(s: str) -> int:
    answer = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            if subString_Check(str(s[i:j])):
                answer += 1
                print(i,j,s[i:j],subString_Check(s[i:j]))
    return answer


def subString_Check(s):
    tmp = s[0]
    cnt = 0
    num0, num1 = s.count('0'), s.count('1')
    if not num0 == num1:
        return False
    for i in range(1, len(s)):
        if tmp == s[i]:
            continue
        else:
            cnt += 1
            tmp = s[i]
    if cnt == 1:
        return True
    else:
        return False
'''
def countBinarySubstrings(s: str) -> int:
    ans, prev, cur = 0, 0, 1
    for i in range(1, len(s)):
        if s[i-1] != s[i]:
            ans += min(prev, cur)
            prev, cur = cur, 1
            print("not", ans, prev, cur)
        else:
            cur += 1
            print("ot", ans, prev, cur)
    return ans + min(prev, cur)

print('FINAL',countBinarySubstrings(s))