s = "(()())()"

'''
1. 입력이 빈 문자열인 경우, 빈 문자열을 반환합니다. 
2. 문자열 w를 두 "균형잡힌 괄호 문자열" u, v로 분리합니다. 단, u는 "균형잡힌 괄호 문자열"로 더 이상 분리할 수 없어야 하며, v는 빈 문자열이 될 수 있습니다. 
3. 문자열 u가 "올바른 괄호 문자열" 이라면 문자열 v에 대해 1단계부터 다시 수행합니다. 
  3-1. 수행한 결과 문자열을 u에 이어 붙인 후 반환합니다. 
4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
  4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
  4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
  4-3. ')'를 다시 붙입니다. 
  4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
  4-5. 생성된 문자열을 반환합니다.
  '''


def isEmpty(arr):
    if len(arr) == 0:
        return True


def divide(arr):
    left, right = 0,0
    pointer = 0
    for _ in arr:
        if _ == '(':
            left += 1
        else:
            right += 1
        pointer += 1
        if left == right:
            ## print('균형',arr[:pointer], arr[pointer:])
            return pointer
            break
    return pointer


def isCorrect(arr):
    left, right = 0,0
    pointer = 0
    for _ in arr:
        if _ == '(':
            left += 1
        else:
            right += 1
        pointer += 1
        if left < right:
            ## print('올바르지 않음',arr[:pointer], arr[pointer:])
            return False
            break
        elif pointer == len(arr):
            ## print('올바름')
            return True


def solution(arr):
    if isEmpty(arr):
        return ''
    pointer = divide(arr)
    u,v = arr[:pointer], arr[pointer:]

    if isCorrect(u):
        ## print('3-1')
        tmp = solution(v)
        ## print(u)
        return u + str(tmp)
    elif not isCorrect(u):
        '''
        4. 문자열 u가 "올바른 괄호 문자열"이 아니라면 아래 과정을 수행합니다. 
            4-1. 빈 문자열에 첫 번째 문자로 '('를 붙입니다. 
            4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙입니다. 
            4-3. ')'를 다시 붙입니다. 
            4-4. u의 첫 번째와 마지막 문자를 제거하고, 나머지 문자열의 괄호 방향을 뒤집어서 뒤에 붙입니다. 
            4-5. 생성된 문자열을 반환합니다.
        '''
        ## print('4')
        tmp = ''
        tmp1 = u[1:len(u)-1]
        tmp = '(' + solution(v) + ')' +''.join(list(map(lambda x:'(' if x==')' else ')',tmp1)))
        ## print('tmp'+tmp)
        return tmp

print('answer', solution(s))