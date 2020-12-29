from collections import defaultdict
gems = ["ZZZ", "ZZZ", "NNNN", "NNNN", "YYY", "NNNN", "ZZZ", "NNNN", "ZZZ"]


def solution(gems):
    answer = []
    sorted_gems = set(gems)
    start, end = 0, 1
    gems_dict = defaultdict(int)
    gems_dict[gems[start]] = 1

    while start < len(gems):
        if len(gems_dict) == len(sorted_gems):
            gems_dict[gems[start]] -= 1
            if gems_dict[gems[start]] == 0:
                del gems_dict[gems[start]]
            start += 1
            if abs(start-end)+1 >= len(sorted_gems):
                answer.append([start,end,abs(start-end)+1])
        elif len(gems_dict) < len(sorted_gems):
            if end == len(gems):
                break
            gems_dict[gems[end]] += 1
            end += 1
    return sorted(answer, key=lambda x: x[2])[0][0:2]


print(solution(gems))
