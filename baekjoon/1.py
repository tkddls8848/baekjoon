
lottos= [44, 1, 0, 0, 31, 25]
win_nums= 	[31, 10, 45, 1, 6, 19]
def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero_cnt = 0
    for l in lottos:
        if l in win_nums:
            cnt += 1
        if l == 0:
            zero_cnt += 1
    if cnt == 0:
        if zero_cnt == 0:
            answer.append(6)
            answer.append(6)
        else:
            answer.append(7 - (cnt + zero_cnt))
            answer.append(6)
    else:
        answer.append(7 - (cnt + zero_cnt))
        answer.append(7 - cnt)

    print(answer)
    return answer

solution(lottos, win_nums)