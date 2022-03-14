n = 5
info = [2,1,1,1,0,0,0,0,0,0,0]

n = 1
info = [1,0,0,0,0,0,0,0,0,0,0]

n = 9
info = [0,0,1,2,0,1,1,1,1,1,1]

n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]

from itertools import combinations_with_replacement

def solution(n, info):
    answer = []
    test = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    info.reverse()
    score_showdown_result = {}
    appeach_result = {}
    lion_result = {}

    for _ in combinations_with_replacement(test, n):
        appeach_final_score = 0
        lion_final_score = 0
        lion_info = _
        for k, v in enumerate(info):
            appeach_result[k] = v
            lion_result[k] = 0
            score_showdown_result[k] = ''
        ##for i in range(len(lion_info)):
        ##    lion_result[i] += lion_info[i]
        for _ in lion_info:
            print(_)
            lion_result[_] += 1
        print("appeach_result", appeach_result)
        print("lion_result", lion_result)
        for i in range(len(info)):
            if appeach_result[i] == 0 and lion_result[i] == 0:
                score_showdown_result[i] = 'nothing'
            else:
                if appeach_result[i] >= lion_result[i]:
                    score_showdown_result[i] = 'appeach'
                else:
                    score_showdown_result[i] = 'lion'
        print("score_showdown_result", score_showdown_result)
        for _ in score_showdown_result:
            if score_showdown_result[_] == "appeach":
                appeach_final_score += _
            elif score_showdown_result[_] == "lion":
                lion_final_score += _
        print("final score difference", lion_final_score, appeach_final_score, lion_final_score - appeach_final_score)
        if lion_final_score - appeach_final_score > 0:
            answer.append([lion_final_score - appeach_final_score, lion_info])
    if len(answer) != 0:
        answer.sort(key=lambda x:x[0], reverse=True)
        print(list(answer[0][1]))
        last = [0] * len(info)
        for _ in list(answer[0][1]):
            last[_] += 1
        print(last)
        return sorted(last, reverse=True)
    else:
        return [-1]

print("FINAL", solution(n, info))