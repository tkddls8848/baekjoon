'''
1.왼손* 오른손#
2.1,4,7에서 시작 3,6,9에서 시작
3.가운데는 가장 가까운거
'''

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"
array = ['1', '2', '3', '4', '5', '6', '7', '8', '9','*', '0', '#']

def distance(str1, str2):
    pos1 = array.index(str1)
    pos2 = array.index(str2)
    pos1_row = pos1 // 3
    pos1_col = pos1 % 3
    pos2_row = pos2 // 3
    pos2_col = pos2 % 3
    return abs(pos1_col-pos2_col)+abs(pos1_row-pos2_row)

def solution(numbers, hand):
    answer = ''
    left_pos = '*'
    right_pos = '#'
    numb = list(map(str, numbers))
    for _ in numb:
        if _ == '1' or _ == '4' or _ == '7':
            left_pos = _
            answer += 'L'
        elif _ == '3' or _ == '6' or _ == '9':
            right_pos = _
            answer += 'R'
        elif _ == '2' or _ == '5' or _ == '8' or _ == '0':
            left_dis = distance(left_pos, _)
            right_dis = distance(right_pos, _)
            if left_dis < right_dis:
                left_pos = _
                answer += 'L'
            elif left_dis > right_dis:
                right_pos = _
                answer += 'R'
            else:
                if hand == 'right':
                    right_pos = _
                    answer += 'R'
                else:
                    left_pos = _
                    answer += 'L'
    return answer


print(solution(numbers,hand))