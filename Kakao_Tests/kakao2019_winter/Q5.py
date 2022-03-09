stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

def solution(stones, k):
    start = 0
    end = max(stones)
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        tmp = []
        zero_in_row = 0
        max_zero = 0
        for i in range(len(stones)):
            if stones[i] <= mid:
                tmp.append(0)
            else:
                tmp.append(stones[i])
            if tmp[i] == 0:
                zero_in_row += 1
            else:
                max_zero = max(max_zero, zero_in_row)
                zero_in_row = 0
            max_zero = max(max_zero, zero_in_row)
        if max_zero >= k:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1
    return answer

print(solution(stones,k))