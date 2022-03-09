def solution(progresses, speeds):
    answer = []
    day = 0
    count = 0
    while progresses:
        if (progresses[0] + day*speeds[0] < 100):
            if count > 0:
                answer.append(count)
                count = 0
            day += 1
        else:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
    answer.append(count)
    return answer