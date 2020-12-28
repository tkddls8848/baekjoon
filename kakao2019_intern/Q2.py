'''
1.수식의 연산자 계산 우선순위 순열
2.우선순위에 따른 계산
3.절대값 가장 큰것
'''
from itertools import permutations
import re

expression = "100-200*300-500+20"


def solution(expression):
    answer = []
    calc = set(re.findall('\D', expression))

    for _ in permutations(calc):
        calculation = re.compile('(\D)').split(expression)
        for i in range(len(_)):
            while _[i] in calculation:
                idx = calculation.index(_[i])
                calculation = calculation[:idx-1] + [str(eval(''.join((calculation[idx-1:idx+2]))))] + calculation[idx+2:]
        answer.append(abs(int(calculation[0])))

    return max(answer)

print(solution(expression))

