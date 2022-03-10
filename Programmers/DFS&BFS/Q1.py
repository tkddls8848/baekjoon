##numbers	= [1, 1, 1, 1, 1]
##target = 3
numbers	= [4, 1, 2, 1]
target = 4

def solution(numbers, target):
    if numbers == []:
        if target == 0:
            return 1
        else:
            return 0
    answer = solution(numbers[1:], target+numbers[0])+solution(numbers[1:], target-numbers[0])
    return answer


print(solution(numbers, target))