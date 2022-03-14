n = 437674
k = 3 ## result 3
n = 110011
k = 10 ## result 2
import math

def ginsu(n, k):
    result = []
    while n != 0:
        div, res = divmod(n, k)
        result.append(res)
        n = div
    result = result[::-1]
    return "".join(list(map(str, result)))

def is_prime(n):
    print(n)
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    jinsu_string = ginsu(n, k)
    for _ in jinsu_string.split('0'):
        if _ == '':
            continue
        else:
            if is_prime(int(_)):
                answer += 1
    return answer


print("FINAL", solution(n, k))