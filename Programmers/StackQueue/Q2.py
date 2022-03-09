from collections import deque

priorities = [1, 2, 9, 1, 1, 1]
location = 0

def solution(priorities, location):
    answer = 0
    d = deque([(v,i) for i,v in enumerate(priorities)])

    while d:
        item = d.popleft()
        print(d)
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer


print(solution(priorities, location))