from itertools import permutations
import re

expression = "100-200*300-500+20"

def solution(expression):
    operands = set(re.findall('\D', expression))
    result = []
    for _ in permutations(operands):
        array = re.compile('(\D)').split(expression)
        for i in range(len(_)):
            while _[i] in array:
                idx = array.index(_[i])
                array = array[:idx-1] + [str(eval(''.join(array[idx-1:idx+2])))] + array[idx+2:]
                print(array)
        result.append(abs(int(array[0])))
    return max(result)


print(solution(expression))






